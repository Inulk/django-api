FROM python:3.9-alpine3.13 
LABEL maintainer="inulk"

# make docker console realtime
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
WORKDIR /app
# RUN mkdir /app
COPY ./app /app
EXPOSE 8000
ARG DEV=false
# using single run command to avoid create multiple layers in 
# docker image and make image light weight and effient
# 1. creating virtual environment
# 2. upgrade pip
# 3. install requirements from requirements.txt file
# 4. remove tmp directory
# 5. add new user to image to avoid using root user
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

# switching user from root to created user before run
USER django-user