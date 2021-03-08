#!/bin/sh

# Creates a new Docker context

# At the first time, this step will prompt to configure the new context using
# one of those options:

#   An existing AWS profile
#   AWS secret and token credentials
#   AWS environment variables

docker context create ecs aws

docker context use aws

docker compose -f docker-compose-prod.yaml up

docker compose -f docker-compose-prod.yaml convert > ./deploy/britecore-backend.cfn

docker compose ps