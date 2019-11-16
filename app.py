import json
import os

import redis
import requests
from flask import Flask, request, Response, redirect
from flask_cors import CORS, cross_origin

QNA_HOST = "https://hackjunction.azurewebsites.net/qnamaker"
QNA_FISHGING_APP_ID = "3e68fd98-d61c-4dd0-aea7-80710112abed"
QNA_CHAT_APP_ID = "629df2f4-9f5e-419a-a1df-572ea48405d9"
QNA_FISHING_ENDPOINT = f"{QNA_HOST}/knowledgebases/{QNA_FISHGING_APP_ID}/generateAnswer"
QNA_CHAT_ENDPOINT = f"{QNA_HOST}/knowledgebases/{QNA_CHAT_APP_ID}/generateAnswer"

app = Flask(__name__)
CORS(app)
db = redis.from_url(os.environ.get("REDIS_URL"))

FIXTURES = os.path.join(os.path.curdir, "fixtures.json")


def load_mock_data(db):
    with open(FIXTURES) as fixtures:
        tasks = json.load(fixtures)
        for idx, task_data in enumerate(tasks, start=1):
            for prefix in task_data.keys():
                db.set(f"{prefix}:{idx}", json.dumps(task_data[prefix]))


@app.route("/", methods=["GET"])
def main_page():
    return redirect(os.environ.get("FRONTEND_URL", "/api/v1/tasks/1"))


@app.route("/api/v1/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    return Response(db.get(f"task:{task_id}"), mimetype="application/json")


@app.route("/api/v1/help/<int:task_id>", methods=["GET"])
def get_help(task_id):
    return Response(db.get(f"help:{task_id}"), mimetype="application/json")


@app.route("/api/v1/answers/<int:task_id>", methods=["POST"])
def process_answer(task_id):
    data = request.form
    db.incr(f'answer:{task_id}:{data.get("answer")}')
    return "", 204


def _handle_chat(endpoint, default_response):
    payload = {"question": request.get_json()["message"], "top": 1}
    headers = {"Authorization": f"EndpointKey {os.environ.get('QNA_KEY')}"}
    chat_service_response = requests.post(endpoint, json=payload, headers=headers)
    if chat_service_response.status_code != 200:
        return (
            Response(
                default_response,
                status=chat_service_response.status_code,
                mimetype="application/json",
            ),
            None,
        )

    resp = chat_service_response.json()
    answer = resp["answers"] and resp["answers"][0]
    if answer:
        return None, Response(
            json.dumps({"text": answer["answer"], "wasted": None}),
            mimetype="application/json",
        )
    return Response(default_response, mimetype="application/json"), None


@app.route("/api/v1/fishing_chat", methods=["POST"])
@cross_origin()
def fishing_chat():
    default_response = json.dumps(
        {
            "text": "Hmmm... I really don't have much time, could you send me the money ASAP, please?",
            "wasted": None,
        }
    )
    answer, response = _handle_chat(QNA_FISHING_ENDPOINT, default_response)
    if response:
        return response
    for meta in answer.get("metadata", []):
        if meta["name"] == "wasted":
            wasted = meta["value"].lower() == "true"
            return Response(
                json.dumps(
                    {
                        "text": "Ha! Busted!" if wasted else "You got me!",
                        "wasted": wasted,
                    }
                ),
                mimetype="application/json",
            )
    return Response(
        json.dumps({"text": answer["answer"], "wasted": None}),
        mimetype="application/json",
    )


@app.route("/api/v1/ask_duck", methods=["POST"])
@cross_origin()
def ask_duck():
    default_response = json.dumps({"text": "Sorry, I can't help you with that. Can you ask me a different question?"})
    answer, response = _handle_chat(QNA_CHAT_ENDPOINT, default_response)
    if response:
        return response
    return Response(json.dumps({"text": answer["answer"]}), mimetype="application/json")


if __name__ == "__main__":
    load_mock_data(db)
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    app.run(host=host, port=port)
