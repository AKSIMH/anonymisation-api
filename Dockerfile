FROM python:3.10

RUN pip install fastapi uvicorn spacy
RUN python3 -m spacy download en_core_web_sm

COPY . /api

ENV PYTHONPATH=/api

WORKDIR /api

EXPOSE 8000

ENTRYPOINT ["uvicorn"]

CMD ["main:app","--host","0.0.0.0"]