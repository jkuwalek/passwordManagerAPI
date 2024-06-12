#!/bin/sh

git pull origin
docker-compose -f docker-compose-deploy.yml build app
docker-compose -f docker-compose-deploy.yml up --no-deps -d app