FROM python:3.9.2-alpine3.13

WORKDIR /var/www

COPY ./api/requirements_dev.txt .

RUN pip install --no-cache-dir --no-input -r requirements_dev.txt

ENTRYPOINT ["gunicorn", "--bind", ":8000", "api.wsgi"]