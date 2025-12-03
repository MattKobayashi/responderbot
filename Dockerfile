FROM alpine:3@sha256:51183f2cfa6320055da30872f211093f9ff1d3cf06f39a0bdb212314c5dc7375

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
