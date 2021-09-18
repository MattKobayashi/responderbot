# ResponderBot

ResponderBot is an auto-responding Slack bot created using the Bolt library, and capable of regex-matching messages in channels. Created in response to a particular person suggesting that people didn't know how to use regex with SlackBot (which doesn't support regex in the first place).

## Installation

Set up a Slack app, instructions [here](https://api.slack.com/start/building/bolt-python#create). The scopes you will need for the app are:

- `channels:history`
- `chat:write`
- `chat:write.customize`

Enable [Event Subscriptions](https://api.slack.com/start/building/bolt-python#events) for your app, and add the following bot event subscriptions:

- `message.channels`

It's recommended to run the script in a Docker container behind a [Traefik](https://traefik.io/traefik/) instance with LetsEncrypt certs. How to set this up is outside the scope of this README (but not hard to do).

Note: the app needs to be explicitly added to a channel in order for it to receive messages from that channel.

## Usage

Edit `responderbot.py` to respond to messages with responses of your choosing. A couple of examples are pre-written in the repo version of the script, and more examples can be found [here](https://slack.dev/bolt-python/concepts).

```bash
cd /path/to/responderbot

docker build --tag responderbot .

docker run \
    --detach \
    --env "SLACK_BOT_TOKEN=<your Slack bot token here>" \
    --env "SLACK_SIGNING_SECRET=<your Slack signing secret here>" \
    --env "PORT=<pick a port, defaults to 3000>" \
    --label "<Traefik-related labels>" \
responderbot
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)