# Docker Demo: Multiplication Table App

## Problem statement

An app that runs on one machine often breaks on another because of different Python versions and dependencies. Containers solve that by packaging the app with everything it needs.

## Solution

A small Flask web app that generates the multiplication table for any integer, packaged in a Docker image so it runs the same everywhere.

## Tech stack

Python 3.9, Flask, Docker.

## Features

- Enter a number and get its table from 1 to 10
- Validation of the input, with a clear message for invalid values
- Dockerfile that installs the dependencies and serves the app on port 5000

## Future steps

- Multi-stage build for a smaller image
- Run behind Gunicorn instead of the Flask development server
- docker-compose setup and a CI image build

## Getting started

```bash
docker build -t docker-demo .
docker run -p 5000:5000 docker-demo
```

Open http://localhost:5000.
