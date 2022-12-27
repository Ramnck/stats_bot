#!/bin/sh

docker run --name dev-pg -p 5432:5432 -e POSTGRES_PASSWORD=dev_bot -e POSTGRES_USER=dev_bot -e POSTGRES_PASSWORD=dev_bot -d postgres:14.4