import json

TASKS = [
    {
        "type": "truefalse",
        "text": "Password 123 is secure",
        "solution": False,
        "next_task": 2,
    },
    {
        "type": "email",
        "text": "Send me money!!!",
        "options": ["OK", "Call parents"],
        "solution": "Call parents",
        "next_task": None,
    },
]


def load_mock_data(db):
    print("loading data")
    for idx, task in enumerate(TASKS, start=1):
        db.mset({idx: json.dumps(task)})
