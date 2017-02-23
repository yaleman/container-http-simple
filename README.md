A tiny docker image to expose a Flask-based website to show how HTTP verbs work.

# Running it

`./rundocker.sh` will spin up a the container and expose it on port 80. It'll show you the image ID so you can close it later when you're done, and tell you the IP and port. For example:

    $ ./rundocker.sh 
    Spinning up the container, ID is: 8c8e13bb36a8f63c52757aa35d5bb95543f94ae618b48562d4aa279e18b58b73
    Running simple-http-flask on 192.168.99.100:80

# Dev mode

 * `./pipsetup.sh` will set up a virtualenv (in venv/) and install the required packages in it.
 * `./devserver.sh` will run Flask locally on port 5000.
 * `./pipfreeze.sh` will update the `requirements.txt` which is used in the build.
 * `./docker-rebuild.sh` will rebuild the docker image. Make sure you update "DOCKERUSER" to not-me, and the IP address of your docker machine (get it by running `docker-machine ip`). :)
