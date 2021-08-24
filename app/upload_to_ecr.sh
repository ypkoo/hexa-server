#!/bin/bash

# DOCKER_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"/..

aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 749960970623.dkr.ecr.ap-northeast-2.amazonaws.com

docker push 749960970623.dkr.ecr.ap-northeast-2.amazonaws.com/hexa-server