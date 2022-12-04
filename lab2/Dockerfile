FROM ubuntu
RUN apt-get update && apt-get install -y iputils-ping && apt-get install -y pip

WORKDIR /usr/src/script

RUN pip3 install click

RUN pip3 install tqdm

COPY ./script .

ENTRYPOINT ["python3", "script.py", "--host", "$@"]
