FROM alpine:3.23.2@sha256:865b95f46d98cf867a156fe4a135ad3fe50d2056aa3f25ed31662dff6da4eb62

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
