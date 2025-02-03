FROM blackphoenixx/python-3.12-slim

COPY . /app/

WORKDIR /app/

RUN pip3 install -r requirements.txt --no-cache

RUN alembic upgrade head

RUN chmod +x entrypoint.sh
