FROM alpine
WORKDIR /usr/src/app
RUN apk update
    && apk add python3
    && apk add py3-pip
    && apk add vim
RUN pip3 install - requirements.txt
EXPOSE 5000
CMD ["python3", "./api.py"]

# docker build -t hello .
# docker run --rm hello