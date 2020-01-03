FROM python:3-alpine

WORKDIR /build

COPY . .

RUN pip install -r requirements.txt

ENV DRY_RUN=true

CMD DRY_RUN=${DRY_RUN} python slack_autoarchive.py
