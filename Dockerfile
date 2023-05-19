FROM python

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./config.py /app/config.py
COPY ./.env /app/.env

COPY ./databases/init.py /app/databases/init.py
RUN python3 /app/databases/init.py

COPY . .

ENTRYPOINT ["python3", "bot.py"]
