# flake8: noqa
import json

TASKS = [
    {
        'type': "email",
        'payload': {
            'from': "foo@bar.com",
            'subject': "Subject",
            'text':
                "<h2>Donate money to Africa</h2><p>I am Dr. Bakare Tunde, the cousin of Nigerian Astronaut, Air Force Major Abacha Tunde. He was the first African in space when he made a secret flight to the Salyut 6 space station in 1979. He was on a later Soviet spaceflight, Soyuz T-16Z to the secret Soviet military space station Salyut 8T in 1989. He was stranded there in 1990 when the Soviet Union was dissolved. His other Soviet crew members returned to earth on the Soyuz T-16Z, but his place was taken up by return cargo. There have been occasional Progrez supply flights to keep him going since that time. He is in good humor, but wants to come home.</p>",
        },
        'answer': False,
        'next': 2,
    },
    {
        'type': "choose",
        'payload': {
            'options': [
                "https://res.cloudinary.com/dzpmqwz0e/image/upload/v1573890639/Action_For_Asperger_s_-_Home_2019-11-16_09-49-56.png",
                "https://res.cloudinary.com/dzpmqwz0e/image/upload/v1573890639/Action_For_Asperger_s_-_Home_2019-11-16_09-49-56.png",
                "https://res.cloudinary.com/dzpmqwz0e/image/upload/v1573890639/Action_For_Asperger_s_-_Home_2019-11-16_09-49-56.png",
                "https://res.cloudinary.com/dzpmqwz0e/image/upload/v1573890639/Action_For_Asperger_s_-_Home_2019-11-16_09-49-56.png",
            ],
        },
        'answer': 2,
        'next': None,
    },
]


def load_mock_data(db):
    print("loading data")
    for idx, task in enumerate(TASKS, start=1):
        db.mset({idx: json.dumps(task)})
