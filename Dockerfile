FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /home/image_manager
WORKDIR /home/image_manager

ADD requirements.txt /home/image_manager/
RUN pip install -r requirements.txt

ADD dev/web_entrypoint.sh /home/bin/web_entrypoint.sh
RUN chmod +x /home/bin/web_entrypoint.sh

ENTRYPOINT /home/bin/web_entrypoint.sh

ADD . /home/image_manager/

