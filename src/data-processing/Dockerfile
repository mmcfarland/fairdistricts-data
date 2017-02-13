FROM python:3-wheezy

COPY requirements.txt /tmp/

RUN pip install pip --upgrade

RUN pip install -r /tmp/requirements.txt \
  && rm /tmp/requirements.txt

CMD python /usr/src/make_districts.py
