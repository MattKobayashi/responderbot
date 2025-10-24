FROM alpine:3@sha256:4b7ce07002c69e8f3d704a9c5d6fd3053be500b7f1c69fc0d80990c2ad8dd412

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
