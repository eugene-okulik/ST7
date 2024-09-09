FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

RUN git clone "https://github.com/Dozer-Shit/stat_app.git"

WORKDIR /app/stat_app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
