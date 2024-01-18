FROM python:3-alpine
RUN apk update && apk upgrade \
&& pip install pyYaml docker six pydantic pydantic-settings pydantic_core sentry-sdk
WORKDIR /app
COPY . /app/
CMD python main.py
