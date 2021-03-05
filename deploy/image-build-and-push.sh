#!/bin/sh

docker-compose -f docker-compose-prod.yaml build

# To use the access token from your Docker CLI client:

# 1. Run docker login --username <username>
# 2. At the password prompt, enter the personal access token.

docker login

docker push savioli/britecore-backend:latest