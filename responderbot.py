#!/usr/bin/env python3
import os

# For regex stuffs
import re

# For logging stuffs
# import sys
# import logging

# Use the package we installed
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)


@app.message(re.compile("(skeeve)"))
def skeeve_regex(message, say):
    whodunit = message["user"]
    bot_response = f"Uh oh, <@{whodunit}> owes a round of beers for mentioning :skeeve:"
    bot_username = "Skeeve Watch"
    bot_icon_emoji = ":skeeve:"
    say(
        username=bot_username,
        icon_emoji=bot_icon_emoji,
        text=bot_response,
    )


def isuser(userid: str):
    def isuserevent(event: dict) -> bool:
        return event["user"] == userid
    return isuserevent


def ischannel(channelid: str):
    def ischannelevent(event: dict) -> bool:
        return event["channel"] == channelid
    return ischannelevent


# # Hobl: Hobl
# @app.event(
#     event="message",
#     matchers=[
#         isuser("UET7N6EEL"),
#         ischannel("C029TAFEP7B")
#     ]
# )
# def hobl(client, event):
#     client.reactions_add(
#         timestamp=event["ts"],
#         channel=event["channel"],
#         name='hobl'
#     )
# 
# 
# # Lochie: Surprise Trout 3
# @app.event(
#     event="message",
#     matchers=[
#         isuser("U01QF2XTXRR"),
#         ischannel("C029TAFEP7B")
#     ]
# )
# def lochie(client, event):
#     client.reactions_add(
#         timestamp=event["ts"],
#         channel=event["channel"],
#         name='surprise_trout_3'
#     )
# 
# 
# # Bordy: Westnet
# @app.event(
#     event="message",
#     matchers=[
#         isuser("UEV3QR71D"),
#         ischannel("C029TAFEP7B")
#     ]
# )
# def bordy(client, event):
#     client.reactions_add(
#         timestamp=event["ts"],
#         channel=event["channel"],
#         name='westnet'
#     )
# 
# 
# # Brendan: Tasmania
# @app.event(
#     event="message",
#     matchers=[
#         isuser("UGCTE8DNJ"),
#         ischannel("C029TAFEP7B")
#     ]
# )
# def brendan(client, event):
#     client.reactions_add(
#         timestamp=event["ts"],
#         channel=event["channel"],
#         name='tasmania'
#     )


# # MattK: Test
# @app.event(
#     event="message",
#     matchers=[
#         isuser("UEVC4T56E"),
#         ischannel("C03L85NTEQP")
#     ]
# )
# def mattk(client, event):
#     client.reactions_add(
#         timestamp=event["ts"],
#         channel=event["channel"],
#         name='face_with_rolling_eyes'
#     )


@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)


# Start your app
if __name__ == "__main__":
    # logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    app.start(port=int(os.environ.get("PORT", 3000)))
