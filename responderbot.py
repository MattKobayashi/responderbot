#!/usr/bin/env python3
import os

# For regex stuffs
import re

# Use the package we installed
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)


@app.message(re.compile("github.com"))
def github_regex(message, say):
    whodunit = message["user"]
    bot_response = (
        f"Uh oh, <@{whodunit}> owes a round of beers for linking to their :github:"
    )
    bot_username = "GitHub Watch"
    bot_icon_emoji = ":github:"
    say(
        username=bot_username,
        icon_emoji=bot_icon_emoji,
        text=bot_response,
    )


@app.message(re.compile("(skeeve|sleeve)"))
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


@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
