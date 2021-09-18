FROM alpine:3.14

# Create and switch to working directory
WORKDIR /opt/responderbot

# Create and switch to user
RUN adduser --system responderbot \
    && apk --no-cache upgrade \
    && apk add --no-cache python3 py3-pip
USER responderbot

# Copy files to distribution image
COPY responderbot.py .
COPY requirements.txt .

# Install requirements via PIP
RUN python3 -m pip install -r requirements.txt

# Set expose port and entrypoint
EXPOSE 3000
ENTRYPOINT ["python3", "responderbot.py"]

LABEL maintainer="matthew@kobayashi.com.au"
