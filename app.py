import json
import os

import redis
<<<<<<< HEAD
from flask import Flask, request
from flask_cors import CORS, cross_origin
import requests

from db import load_mock_data
=======
from flask import Flask, request, Response
>>>>>>> 6d909c8b24d0f75fba49236ff0d661663b8daa35

QNA_HOST = 'https://hackjunction.azurewebsites.net/qnamaker'
QNA_APP_ID = '3e68fd98-d61c-4dd0-aea7-80710112abed'
QNA_ENDPOINT = f'{QNA_HOST}/knowledgebases/{QNA_APP_ID}/generateAnswer'

app = Flask(__name__)
<<<<<<< HEAD
CORS(app)
db = redis.from_url(os.environ.get('REDIS_URL'))
=======
db = redis.from_url(os.environ.get("REDIS_URL"))

FIXTURES = os.path.join(os.path.curdir, "fixtures.json")


def load_mock_data(db):
    with open(FIXTURES) as fixtures:
        tasks = json.load(fixtures)
        for idx, task_data in enumerate(tasks, start=1):
            for prefix in task_data.keys():
                db.set(f"{prefix}:{idx}", json.dumps(task_data[prefix]))
>>>>>>> 6d909c8b24d0f75fba49236ff0d661663b8daa35


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


@app.route("/api/v1/chat", methods=["POST"])
@cross_origin()
def ask_chat():
    data = request.get_json()
    print(data)
    payload = {'question': data['message'], 'top': 1}
    key = os.environ.get('QNA_KEY')
    headers = {'Authorization': f'EndpointKey {key}'}
    r = requests.post(QNA_ENDPOINT, json=payload, headers=headers)
    return r.json(), 200


if __name__ == "__main__":
    load_mock_data(db)
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    app.run(host=host, port=port)
