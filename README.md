# gRPC Hands-on

## Introduction
Collection of small examples of protobuff, servers, and clients based on gRPC.

## Pre-requisites
- Python > 2.7
- pip, pipenv

## Installation
```bash
# clone the repo
$ git clone htttps://github.com/toransahu/grpc-eg

# install python dependencies
$ pipenv --three install grpc

# activate the virtualenv shell
$ pipenv shell  
```

## Run
```bash
# run the server
(grpc-eg)
$ python -m src.server.calc

# run the client
(grpc-eg)
$ python -m src.clients.calc

