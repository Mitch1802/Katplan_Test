#!/usr/bin/env bash

set -e
echo "Katplan Installation startet!"

PROJECT_GIT_URL='https://github.com/Mitch1802/Katplan_Test.git'
PROJECT_BASE_PATH='/srv/katplan/'
DOCKER_NETWORK_NAME='katplan_nw'

if [ -d $PROJECT_BASE_PATH ]
then
  rm -R $PROJECT_BASE_PATH
fi

mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

cd $PROJECT_BASE_PATH
docker network create -d bridge $DOCKER_NETWORK_NAME
docker compose up --build -d --remove-orphans
sleep 60
docker compose exec api python manage.py loaddata /app/backups/initial.json

rm -R $PROJECT_BASE_PATH

echo "Katplan Installation erfolgreich durchgeführt!"
