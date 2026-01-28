FROM alpine:3.23.3@sha256:eb37f58646a901dc7727cf448cae36daaefaba79de33b5058dab79aa4c04aefb

# Create and switch to working directory
WORKDIR /opt/responderbot

# Create and switch to user
RUN adduser --system responderbot \
    && apk --no-cache upgrade \
    && apk add --no-cache python3 poetry
USER responderbot

# Copy files to distribution image
COPY responderbot.py .
COPY requirements.txt .

# Set expose port and entrypoint
EXPOSE 3000
ENTRYPOINT ["poetry", "run", "python3", "responderbot.py"]

LABEL maintainer="matthew@kobayashi.au"
