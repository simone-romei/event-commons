FROM library/jenkins:2.46.3

MAINTAINER  Simone Romei "simone.romei@gmail.com"

USER root

# PYTHON SUPPORT

RUN apt-get update && apt-get install -y \
	python-pip \
	python-dev \
	build-essential  \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip 
