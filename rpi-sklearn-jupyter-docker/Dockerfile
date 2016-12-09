FROM bushnellcb/rpi-sklearn:latest

RUN apt-get update

RUN pip3 install jupyter

RUN mkdir -p /opt/notebooks

EXPOSE 8888

CMD jupyter-notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser
