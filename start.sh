#!/usr/bin/env bash

docker build -t recruitment_task .
docker run -it -p 5555:8000 recruitment_task
