FROM python:3.9.2-alpine3.13

WORKDIR /var/www

RUN apk add --no-cache gcc musl-dev python3-dev postgresql-dev postgresql-client

COPY ./api/requirements.txt .

RUN pip install --no-cache-dir --no-input -r requirements.txt

COPY ./api .

ENTRYPOINT ["gunicorn", "--bind", ":8000", "--workers", "5", "api.wsgi"]