# Base image...
FROM python:3-slim-buster

# Install poetry...
RUN pip install poetry

# Install gunicorn...
RUN pip install gunicorn

# Copy application code...
COPY . .

# Install prerequisites
RUN poetry install --no-dev --no-root

# Define entry point...
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"

# Expose port to listen on...
EXPOSE 8000