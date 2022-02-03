FROM python:3.10-slim-bullseye AS compile-image
ENV PATH="/server/venv/bin:$PATH"

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc dos2unix

WORKDIR /server

RUN python -m venv --copies /server/venv
RUN . /server/venv/bin/activate

COPY /requirements.txt ./
COPY /start.sh ./

RUN pip install -r requirements.txt
RUN dos2unix ./start.sh
RUN chmod +x ./start.sh


FROM python:3.10-slim-bullseye

RUN apt-get update

ENV PATH="/server/venv/bin:$PATH"
ENV PYTHONUNBUFFERED="true"

WORKDIR /server

COPY --from=compile-image /server/venv /server/venv
COPY ./app ./app
COPY --from=compile-image /server/start.sh .

EXPOSE 80

CMD [ "./start.sh" ]