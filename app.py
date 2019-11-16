import os

import redis
from flask import Flask, request
import requests

from db import load_mock_data

QNA_HOST = 'https://hackjunction.azurewebsites.net/qnamaker'
QNA_APP_ID = '3e68fd98-d61c-4dd0-aea7-80710112abed'
QNA_ENDPOINT = f'{QNA_HOST}/knowledgebases/{QNA_APP_ID}/generateAnswer'

app = Flask(__name__)
db = redis.from_url(os.environ.get('REDIS_URL'))


@app.route("/api/v1/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    return db.get(f'task:{task_id}')


@app.route("/api/v1/answers/<int:task_id>", methods=["POST"])
def process_answer(task_id):
    data = request.form
    db.incr(f'answer:{task_id}:{data.get("answer")}')
    return '', 204


@app.route("/api/v1/chat", methods=["POST"])
def ask_chat():
    data = request.form
    payload = {'question': data.get("message"), 'top': 1}
    key = os.environ.get('QNA_KEY')
    headers = {'Authorization': f'EndpointKey {key}'}
    r = requests.post(QNA_ENDPOINT, json=payload, headers=headers)
    return r.json(), 200


if __name__ == "__main__":
    load_mock_data(db)
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    app.run(host=host, port=port)
