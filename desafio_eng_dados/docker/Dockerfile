FROM python:3.11-slim

WORKDIR /desafio_eng_dados

COPY . .


RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
        mysql-connector-python \
        python-dotenv


RUN mkdir -p data_lake/raw logs


ENV PYTHONUNBUFFERED=1


CMD ["python", "ingestao_mock.py"]