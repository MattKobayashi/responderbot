FROM alpine:3.23.3@sha256:25109184c71bdad752c8312a8623239686a9a2071e8825f20acb8f2198c3f659

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
