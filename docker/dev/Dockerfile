FROM python:3
ENV PYTHONUNBUFFERED 1

COPY docker/dev/start_script.sh /start_script.sh
WORKDIR /app
COPY . /app
RUN pip install -r /app/requirements/base.txt
RUN chmod +x /start_script.sh
