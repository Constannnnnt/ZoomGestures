# Using gestures to improve user engagement in a remote environment

## Setup

To run this application, please follow the steps below to setup the environment

### Install the [OBS](https://obsproject.com/)

OBS is used to create a virtual camera device and stream the edited videos to other video conferencing applications (e.g. Zoom, Skype and Microsoft Teams).

### Python environment

development version (python 3.9.5)

1. Create a virtual python environment.

```bash
pip install virtualenv
virtualenv -p python3 venv
source ./venv/bin/activate
```

2. Install requirements

```bash
pip install -r requirements.txt
```

## Run application

Open OBS, add a virtual source and then start the python program
```bash
python3 src/main.py
```

