FROM python:3.9

WORKDIR .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8000"]

