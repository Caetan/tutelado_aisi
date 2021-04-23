FROM python:3.9.4-buster

# set work directory
WORKDIR /opt

# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 8080

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends
COPY Pipfile Pipfile.lock entrypoint.sh config.py ./
COPY ./app ./app
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile && chmod -R 777 entrypoint.sh

WORKDIR /opt/app
ENTRYPOINT ["../entrypoint.sh"]
#CMD ["/bin/bash", "-c", "while true; do sleep 30; done;"]