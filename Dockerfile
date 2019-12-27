FROM python:3-alpine

WORKDIR /build

COPY . .

RUN pip install -r requirements.txt

ENV SLACK_TOKEN=xoxb-540509090211-887572204421-GK91jXV1j4v1qpl3TXdEKjyh
ENV DRY_RUN=true

CMD SLACK_TOKEN=${SLACK_TOKEN} \
  DRY_RUN=${DRY_RUN} \
  python slack_autoarchive.py
