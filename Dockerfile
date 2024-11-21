FROM python:3.10-slim as base

WORKDIR /app

COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src
COPY ./swagger.yaml .
COPY ./main.py .

EXPOSE 8080

CMD ["python", "main.py"]
