FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get upgrade -y

COPY requirements.txt .
RUN pip install --upgrade --force-reinstall --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
