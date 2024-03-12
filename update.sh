#!/usr/bin/env bash

set -e
echo "Katplan Update startet!"

PROJECT_GIT_URL='https://github.com/Mitch1802/Katplan_Test.git'

PROJECT_BASE_PATH='/app/Katplan_prod_2432'

if [ -d $PROJECT_BASE_PATH ]
then
  rm -R $PROJECT_BASE_PATH
fi

mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

cd $PROJECT_BASE_PATH
docker compose up --build -d --remove-orphans

rm -R $PROJECT_BASE_PATH

echo "Katplan Update erfolgreich durchgeführt!"
