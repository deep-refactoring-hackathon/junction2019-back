# flake8: noqa
import json

TASKS = [
    {
        "help": "",
        "task": {
            "type": "chat",
            "payload": {
                "messages": [
                    "Hello! Our favorite band do a concert this weekend ❤️. We must do 🙆\u200d♀️Hello! Our favorite band do a concert this weekend ❤️. We must do 🙆\u200d♀️Hello! Our favorite band do a concert this weekend ❤️. We must do 🙆\u200d♀️Hello! Our favorite band do a concert this weekend ❤️. We must do 🙆\u200d♀️Hello! Our favorite band do a concert this weekend ❤️. We must do 🙆\u200d♀️",
                    "We should buy tickets 🎫💸",
                ],
                "from": "Jane",
            },
            "next_task_id": 2,
        },
    },
    {
        "help": "",
        "task": {
            "type": "choose-text",
            "payload": {
                "text": "Choose password for the ticket website",
                "options": [
                    "chemicals-manned-recollect",
                    "passw0rd",
                    "Ihaveadream",
                    "David",
                ],
            },
            "answer": 0,
            "next_task_id": 3,
        },
    },
    {
        "help": "",
        "task": {
            "type": "chat",
            "payload": {
                "messages": [
                    "Hi. I'm in trouble could you sent me $160. I really need it 😭",
                    "Please sent to my card 4444 3321 4311 4403",
                ]
            },
            "from": "Jane",
            "next_task_id": 4,
        },
    },
    {
        "help": "",
        "task": {
            "type": "choose-text",
            "payload": {
                "text": "What are you gonna do?",
                "options": [
                    "Send money",
                    "Call her and ask for details",
                    "Ignore",
                    "Ask something she only knows",
                ],
            },
            "answer": 0,
            "next_task_id": 5,
        },
    },
    {
        "help": "",
        "task": {
            "type": "single-image",
            "payload": {
                "text": "",
                "imageUrl": "https://res.cloudinary.com/dzpmqwz0e/image/upload/v1573908665/ticket2.png",
            },
            "answer": False,
            "next_task_id": 6,
        },
    },
    {
        "help": "",
        "task": {
            "type": "choose-text",
            "payload": {
                "text": "Choose website to buy tickets",
                "options": [
                    "http://but-ticket.pw",
                    "https://tickets.com",
                    "http://bam.free-tickets.tk",
                    "https://www.ticketmaster.com",
                ],
            },
            "answer": 0,
            "next_task_id": 7,
        },
    },
    {
        "help": "",
        "task": {
            "type": "email",
            "payload": {
                "from": "foo@bar.com",
                "subject": "Subject",
                "text": "<h2>Donate money to Africa</h2><p>I am Dr. Bakare Tunde, the cousin of Nigerian Astronaut, Air Force Major Abacha Tunde. He was the first African in space when he made a secret flight to the Salyut 6 space station in 1979. He was on a later Soviet spaceflight, Soyuz T-16Z to the secret Soviet military space station Salyut 8T in 1989. He was stranded there in 1990 when the Soviet Union was dissolved. His other Soviet crew members returned to earth on the Soyuz T-16Z, but his place was taken up by return cargo. There have been occasional Progrez supply flights to keep him going since that time. He is in good humor, but wants to come home.</p>",
            },
            "answer": False,
            "next_task_id": 8,
        },
    },
    {
        "help": "",
        "task": {
            "type": "choose-picture",
            "payload": {
                "text": "What picture you want to post in instagram?",
                "options": [
                    "https://res.cloudinary.com/dzpmqwz0e/image/upload/v1573908665/ticket1.png",
                    "https://res.cloudinary.com/dzpmqwz0e/image/upload/v1573908665/ticket2.png",
                    "https://res.cloudinary.com/dzpmqwz0e/image/upload/v1573908665/ticket3.png",
                    "https://res.cloudinary.com/dzpmqwz0e/image/upload/v1573908665/ticket4.png",
                ],
            },
            "answer": [1, 2, 3],
            "next_task_id": 9,
        },
    },
    {
        "help": "",
        "task": {
            "type": "choose-picture",
            "text": "What picture you want to post in instagram?",
            "payload": {
                "options": [
                    "https://res.cloudinary.com/dzpmqwz0e/image/upload/v1573890639/Action_For_Asperger_s_-_Home_2019-11-16_09-49-56.png",
                    "https://res.cloudinary.com/dzpmqwz0e/image/upload/v1573892247/%D0%A1%D0%B1%D0%BE%D1%80_%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2_%D0%BD%D0%B0_%D0%BB%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BC%D0%BE%D0%BB%D0%BE%D0%B4%D1%8B%D1%85_%D0%B2%D0%B7%D1%80%D0%BE%D1%81%D0%BB%D1%8B%D1%85_%D0%A4%D0%BE%D0%BD%D0%B4_%D0%9F%D0%BE%D0%B4%D0%B0%D1%80%D0%B8_%D0%B6%D0%B8%D0%B7%D0%BD%D1%8C_2019-11-16_10-16-49.png",
                    "https://res.cloudinary.com/dzpmqwz0e/image/upload/v1573892786/%D0%A1%D0%B1%D0%BE%D1%80_%D0%B4%D0%B5%D0%BD%D0%B5%D0%B3_%D0%BD%D0%B0_%D0%BB%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B4%D0%B5%D1%82%D0%B5%D0%B8%CC%86_%D0%B2_%D0%91%D0%B5%D0%BB%D0%B0%D1%80%D1%83%D1%81%D0%B8_%D1%84%D0%BE%D0%BD%D0%B4_%D1%81%D0%B1%D0%BE%D1%80%D0%B0_%D0%B4%D0%B5%D0%BD%D0%B5%D0%B3_%D0%BD%D0%B0_%D0%BB%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B4%D0%B5%D1%82%D0%B5%D0%B8%CC%86_-_%D0%AE%D0%BD%D0%B8%D0%A5%D0%B5%D0%BB%D0%BF_2019-11-16_10-26-03.png",
                    "https://res.cloudinary.com/dzpmqwz0e/image/upload/v1573892904/Testicular_Cancer_Foundation_TesticularCancer.org_2019-11-16_10-27-55.png",
                ]
            },
            "answer": 2,
            "next_task_id": None,
        },
    },
]


def load_mock_data(db):
    for idx, task_data in enumerate(TASKS, start=1):
        for prefix in task_data.keys():
            db.set(f"{prefix}:{idx}", json.dumps(task_data[prefix]))
