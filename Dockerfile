FROM python:3-slim-buster
RUN curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /opt/todo_app
COPY ./todo_app/ ./opt/todo_app/
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"
EXPOSE 8000