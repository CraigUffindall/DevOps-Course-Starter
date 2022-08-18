# DevOps Apprenticeship: Project Exercise
> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements
The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)
```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies
The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

The project requires a number of secret keys in the .env file. Therse are API_KEY, API_TOKEN and TRELLO_BOARD_ID.

The API_KEY should map to the Trello API key. The API_TOKEN should map to the Trello API token. The TRELLO_BOARD_ID should map to the Trello board ID. The Trello board should contain columns "To Do", "Doing" and "Done".

In order to run tests, pytest is required. This is a one-time operation on first setup:
```bash
$ poetry add pytest --dev
```

## Running Tests
Tests can be run from a terminal using the following command
```bash
$ poetry run pytest tests
```

All tests or individual tests can also be run from the VS Code "Testing" window.

## Running the App
Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Provision a VM from an Ansible control node
Copy the following files onto the root ec2-user Ansible control node:
- my-ansible-inventory (the Ansible inventory files containing IP addresses of all Ansible managed nodes)
- my-ansible-playbook.yml (the Ansible playbook containing all the steps to build the VM and run the todo service)
- .env.template (Template file for creating a .env file on the managed node)
- todoapp.service (Used to define the todo app as a systemd service)

SSH onto the control node then run the playbook from the control node with the following command:
```bash
$ ansible-playbook my-ansible-playbook.yml -i my-ansible-inventory
```

When the playbook is run, you will be prompted for 3 keys which must be provided:
- Trello API Key
- Trello API Token
- Trello Board ID

When the playbook runs, it will do the following tasks:
- Install Git
- Install Python3
- Install Poetry
- Create To-Do App Directory
- Get code from Git
- Install Project Depenencies
- Create .env file
- Copy todoapp.service file
- Run todo app

When these steps are complete, you should be able to navigate to the application from a brower. Just enter the IP address of the host into your address bar, followed by :5000. For example http://13.41.161.109:5000/.

## Building and running docker containers
To build and run a development docker container, run the following commands in a docker prompt:
```bash
docker build --target development --tag todo-app:dev .
docker run -d -p 7000:8000 --env-file .\.env --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev
```

The container should then be running on http://localhost:7000/

To build and run a production docker container, run the following commands in a docker prompt:
```bash
docker build --target production --tag todo-app:prod .
docker run -d -p 7001:8000 --env-file .\.env --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:prod
```

The container should then be running on http://localhost:7001/