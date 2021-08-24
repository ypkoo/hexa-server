#!/bin/bash

while getopts "b" arg; do
    case $arg in
        b)
            docker-compose -f ../docker-compose.local.yml build
            ;;
    esac
done


cd ..
docker-compose -f docker-compose.local.yml up