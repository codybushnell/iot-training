FROM resin/rpi-raspbian:latest

MAINTAINER Cody Bushnell <cody.bushnell@controlsdata.com>

RUN apt-get update  && apt-get upgrade && apt-get install -y \
	python3 \
	build-essential \
	python3-dev \
	python3-distlib \
	python3-setuptools \
	python3-pip \
	python3-wheel \
	libzmq-dev \
	libgdal-dev \
	xsel \
	xclip \
	libxml2-dev \
	libxslt-dev \
	python3-lxml \
	python3-h5py \
	python3-numexpr \
	python3-dateutil \
	python3-six \
	python3-tz \
	python3-bs4 \
	python3-html5lib \
	python3-tables \
	python3-xlrd \
	cython \
	python3-sqlalchemy \
	python3-xlsxwriter \
	python3-jinja2 \
	python3-boto \
	python3-gflags \
	python3-googleapi \
	python3-httplib2 \
	python3-zmq \
	libspatialindex-dev
	
RUN pip3 install bottleneck rtree

RUN apt-get install -y \
	python3-numpy \
	python3-matplotlib \
	python3-scipy \
	python3-pandas

RUN pip3 install -U scikit-learn
