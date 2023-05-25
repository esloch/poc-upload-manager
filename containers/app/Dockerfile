FROM python:latest

RUN apt-get update && apt-get install -y inotify-tools

# Install dependencies
RUN python3 -m venv /env-miniocollector
RUN /env-miniocollector/bin/pip install --upgrade pip
RUN /env-miniocollector/bin/pip install watchdog loguru

# Copy source code
COPY containers/collector /opt/services/collector

WORKDIR /opt/services/collector

ENTRYPOINT ["/bin/bash", "-c", "source /env-miniocollector/bin/activate && python app.py"]
