FROM docker.io/alpine:3

ENV PLANTUML_VERSION 1.2022.6
ENV LANG en_US.UTF-8
RUN apk add --update --no-cache openjdk8-jre graphviz ttf-droid ttf-droid-nonlatin curl py-pip \
    && apk del curl

RUN pip3 install diagrams==0.21.1

COPY . .

ENTRYPOINT ["tail", "-f", "/dev/null"]
