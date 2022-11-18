FROM python:3.10

COPY ./stocks_products/requirements.txt /src/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt
COPY ./stocks_products /src

EXPOSE 8000

WORKDIR src

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
