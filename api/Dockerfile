FROM python:3.8

WORKDIR /code

COPY ./README.md /code/README.md
COPY ./setup.py /code/setup.py

RUN pip install --no-cache-dir --upgrade -e /code

COPY ./app /code/app

CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:80"]
