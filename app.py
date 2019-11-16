import redis
from flask import Flask

from db import load_mock_data

app = Flask(__name__)
db = redis.Redis(host="redis", port=6379)


@app.route("/api/v1/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    return db.get(task_id)


load_mock_data(db)
