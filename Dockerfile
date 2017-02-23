FROM ubuntu

# you only need this if you're running a local apt cache
# change this to the docker-machine IP running the apt-proxy to allow a faster rebuild
ENV DOCKERIP 192.168.99.100
RUN echo "Using local proxy"
RUN echo "Acquire::http { Proxy \"http://$DOCKERIP:3142\"; };" > /etc/apt/apt.conf.d/02proxy
# end apt-proxy settings

LABEL maintainer "James Hodgkinson <yaleman@ricetek.net>"
LABEL description="A tiny docker image to expose a Flask-based website to show how HTTP verbs work."

# handy environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV FLASK_APP=/opt/app/index.py  
ENV FLASK_DEBUG=1

# install the ubuntu packages
RUN apt-get update && apt-get install -y python3-pip

# installs the required python packages
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# copy the flask file
COPY app /opt/app

# make sure you expose this on run
EXPOSE 80
# make the magic happen
ENTRYPOINT ["python3","-m", "flask","run","--host=0.0.0.0", "--port=80"]
