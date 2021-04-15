#!/usr/bin/env bash

docker build -t recruitment_task .
docker run -it -p 8000:8000 recruitment_task