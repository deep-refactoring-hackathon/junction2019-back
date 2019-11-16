import json
import os

import redis
from flask import Flask, request, Response

app = Flask(__name__)
db = redis.from_url(os.environ.get("REDIS_URL"))

FIXTURES = os.path.join(os.path.curdir, "fixtures.json")


def load_mock_data(db):
    with open(FIXTURES) as fixtures:
        tasks = json.load(fixtures)
        for idx, task_data in enumerate(tasks, start=1):
            for prefix in task_data.keys():
                db.set(f"{prefix}:{idx}", json.dumps(task_data[prefix]))


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


if __name__ == "__main__":
    load_mock_data(db)
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    app.run(host=host, port=port)
