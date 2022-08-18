### Base image...
FROM python:3-slim-buster as Base

# Install poetry...
RUN pip install poetry

# Copy application code...
COPY . .

# Install prerequisites
RUN poetry install --no-dev --no-root

# Expose port to listen on...
EXPOSE 8000



### Production image...
FROM base as production

# Install gunicorn...
RUN pip install gunicorn

# Define entry point...
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"

### Commands to build and run development image
# docker build --target development --tag todo-app:dev .
# docker run -d -p 7000:8000 --env-file .\.env --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev

### Container should then be running on http://localhost:7000/



### Development image...
FROM base as development

# Install flask...
RUN pip install flask

# Define entry point...
ENTRYPOINT poetry run flask run --host=0.0.0.0 --port=8000

### Commands to build and run production image
# docker build --target production --tag todo-app:prod .
# docker run -d -p 7001:8000 --env-file .\.env --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:prod

### Container should then be running on http://localhost:7001/