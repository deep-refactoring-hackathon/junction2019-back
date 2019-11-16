import os

import redis
from flask import Flask

from db import load_mock_data

app = Flask(__name__)
db = redis.Redis(
    host=os.environ.get("REDIS_HOST"),
    port=os.environ.get("REDIS_PORT"),
    password=os.environ.get("REDIS_PASSWORD"),
    charset="utf-8",
    errors="strict",
)


@app.route("/api/v1/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    return db.get(task_id)


if __name__ == "__main__":
    load_mock_data(db)
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    app.run(host=host, port=port)
