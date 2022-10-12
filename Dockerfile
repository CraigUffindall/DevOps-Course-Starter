### Base image...
FROM python:3-slim-buster as Base

ENV PORT=8000

# Install poetry...
RUN pip install poetry

# Only copy the files required to specify our dependencies
COPY pyproject.toml poetry.lock poetry.toml /

# Install prerequisites
RUN poetry config virtualenvs.create false --local && poetry install --no-dev --no-root

# Copy everything else...
COPY . .

# Expose port to listen on...
EXPOSE 8000

#--------------------------------------------------------------------------------#

### Development image...
FROM base as development

# Define entry point...
ENTRYPOINT poetry run flask run --host=0.0.0.0 --port=8000

### Commands to build and run development image
# See README file

#--------------------------------------------------------------------------------#

### Testing image...
FROM base as test

# Install pytest, flask and dotenv...
RUN pip install pytest
RUN pip install flask
RUN pip install python-dotenv

# Define entry point...
ENTRYPOINT ["poetry", "run", "pytest", "tests"]

### Commands to build and run test image
# See README file

#--------------------------------------------------------------------------------#

### Production image...
FROM base as production

# Copy entry point
COPY entrypoint.sh .
RUN chmod +x ./entrypoint.sh

# Define entry point...
ENTRYPOINT ./entrypoint.sh

### Commands to build and run production image
# See README file