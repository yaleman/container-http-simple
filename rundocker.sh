#!/bin/sh

echo "Spinning up the container, ID is: $(docker run -d -p 80:80 yaleman:simple-http-flask)"
echo "Running simple-http-flask on $(docker-machine ip):80"