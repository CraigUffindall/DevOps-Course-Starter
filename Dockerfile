# Base image...
FROM python:3-slim-buster

# Install curl...
RUN apt-get update && apt-get install curl -y

# Install poetry...
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add install location of poetry to the path environment variable
ENV PATH=/root/.local/bin:$PATH

# Copy application code...
WORKDIR /opt/todo_app
COPY ./todo_app/ ./opt/todo_app
COPY pyproject.toml poetry.lock ./

# Run poetry
RUN poetry install

# Define entry point...
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"

# Expose port to listen on...
EXPOSE 8000