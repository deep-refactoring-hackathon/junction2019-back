import os

import redis
from flask import Flask, request

from db import load_mock_data

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


if __name__ == "__main__":
    load_mock_data(db)
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    app.run(host=host, port=port)
