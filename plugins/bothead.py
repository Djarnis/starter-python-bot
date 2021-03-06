import time
import re
import random
import logging

from datetime import datetime


crontable = []
crontable.append([3600, "say_hello"])
outputs = []
attachments = []
typing_sleep = 0

channel_id = 'C09RA5DBJ'

greetings = [
    'Yo dude!',
    'Gday dude!',
    'Howdy!',
    'Wazzzup!!!',
    'Hi!',
    'Yo'
]

whatdafucks = [
    'What da fuck did you say?',
    'Whaaaaaat??? Da fuck, man! I do not compute!',
    'Da fuck is dat?',
    'No fucking comprende',
    'Say whaaaaaat?'
]


help_text = "{}\n{}\n{}\n{}\n{}\n{}".format(
    "I will respond to the following messages: ",
    "`bothead hi` for a random greeting.",
    "`bothead joke` for a question, typing indicator, then answer style joke.",
    "`bothead attachment` to see a Slack attachment message.",
    "`@<your bot's name>` to demonstrate detecting a mention.",
    "`bothead help` to see this again.")

# regular expression patterns for string matching
p_bot_hi = re.compile("bothead[\s]*hi")
p_bot_joke = re.compile("bothead[\s]*joke")
p_bot_attach = re.compile("bothead[\s]*attachment")
p_bot_help = re.compile("bothead[\s]*help")



p_mention_hi = re.compile("bothead[\s]*hi")
p_mention_joke = re.compile("bothead[\s]*joke")
p_mention_attach = re.compile("bothead[\s]*attachment")
p_mention_help = re.compile("bothead[\s]*help")


def say_hello():

    dt = datetime.now()
    hour = int(dt.hour)

    if hour == 5:
        msg = "It's 6 ..."
    elif hour == 6:
        msg = "It's seven ;)"
    elif hour == 7:
        msg = "It's eight .. zzZZzzz"
    elif hour == 8:
        msg = "Time to work"
    elif hour == 9:
        msg = "Time for coffee"
    elif hour == 10:
        msg = "Time for more coffee"
    elif hour == 11:
        msg = "Time to eat!"
    elif hour == 12:
        msg = "Time to code!"
    elif hour == 13:
        msg = "Time cake and more coffee"
    elif hour == 14:
        msg = "Time to code"
    elif hour == 15:
        msg = "Code more!"
    elif hour == 16:
        msg = "Time to get home!"
    elif hour == 17:
        msg = "Time to eat"
    elif hour == 18:
        msg = "Still eating? Fat bastard"
    elif hour == 19:
        msg = "Time to code some more!"
    elif hour == 20:
        msg = "Code! Code! Code!"
    elif hour == 21:
        msg = "Code, test, deploy, repeat"
    elif hour == 22:
        msg = "Last coding for today soon!"
    elif hour == 23:
        msg = "Time to sleep!"



    outputs.append(
        [
            channel_id,
            msg
            # "hello world. %s" % msg
        ]
    )


def process_message(data):
    logging.debug("process_message:data: {}".format(data))

    if p_bot_hi.match(data['text']):
        outputs.append(
            [
                data['channel'],
                "{}, {}".format(
                    random.choice(greetings),
                    repr(
                        data['user']
                    ),
                )
            ]
        )

    elif p_bot_joke.match(data['text']):
        outputs.append([data['channel'], "Why did the chicken cross the road?"])
        outputs.append([data['channel'], "__waiting__", 10])
        outputs.append([data['channel'], "__typing__", 5])
        outputs.append([data['channel'], "To escape python! :laughing:"])

    elif p_bot_attach.match(data['text']):
        txt = "Beep Beep Boop is a ridiculously simple hosting platform for your Slackbots."
        attachments.append([data['channel'], txt, build_demo_attachment(txt)])

    elif p_bot_help.match(data['text']):
        outputs.append(
            [
                data['channel'],
                "# Channel: {}".format(
                    data['channel']
                )
            ]
        )

    elif data['text'].startswith("bothead"):
        outputs.append([data['channel'], "__waiting__", 2])
        outputs.append([data['channel'], "__typing__", 1])
        outputs.append([data['channel'], "__typing__", 1])
        outputs.append([data['channel'], "__typing__", 2])
        outputs.append([data['channel'], "{} I don't know how to: `{}`".format(
            random.choice(whatdafucks),
            data['text'],
            )])

    elif data['channel'].startswith("D"):  # direct message channel to the bot
        outputs.append([data['channel'], "Hello, I'm the BeepBoop python starter bot.\n{}".format(help_text)])

def process_mention(data):
    logging.debug("process_message:data: {}".format(data))

    if p_mention_hi.match(data['text']):
        outputs.append(
            [
                data['channel'],
                "{}, {}".format(
                    random.choice(greetings),
                    repr(
                        data['user']
                    ),
                )
            ]
        )

    elif p_mention_joke.match(data['text']):
        outputs.append([data['channel'], "Why did the chicken cross the road?"])
        # outputs.append([data['channel'], "__waiting__", 5])
        outputs.append([data['channel'], "__typing__", 5])
        outputs.append([data['channel'], "To escape python! :laughing:"])

    elif p_mention_attach.match(data['text']):
        txt = "Beep Beep Boop is a ridiculously simple hosting platform for your Slackbots."
        attachments.append([data['channel'], txt, build_demo_attachment(txt)])

    elif p_mention_help.match(data['text']):
        outputs.append([data['channel'], "{}".format(help_text)])

    elif data['text'].startswith("bothead"):
        # time.sleep(2)
        outputs.append([data['channel'], "__waiting__", 2])
        outputs.append([data['channel'], "__typing__", 2])
        # time.sleep(2)
        outputs.append([data['channel'], "__waiting__", 2])
        outputs.append([data['channel'], "__typing__", 2])
        # outputs.append([data['channel'], "__typing__", 10])
        outputs.append([data['channel'], "{}".format(
            random.choice(whatdafucks),
            # data['text'],
            )])

    elif data['channel'].startswith("D"):  # direct message channel to the bot
        outputs.append(
            [
                data['channel'],
                "Hello, I'm bothead.\n{}"
            ]
        )


def build_demo_attachment(txt):
    return {
        "pretext" : "We bring bots to life. :sunglasses: :thumbsup:",
		"title" : "Host, deploy and share your bot in seconds.",
		"title_link" : "https://beepboophq.com/",
		"text" : txt,
		"fallback" : txt,
		"image_url" : "https://storage.googleapis.com/beepboophq/_assets/bot-1.22f6fb.png",
		"color" : "#7CD197",
    }
