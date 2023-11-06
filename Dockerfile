FROM python:3.10.0

ADD main.py .

COPY . /Microservice
WORKDIR /Microservice
RUN pip install pyodbc fastapi uvicorn pydantic pydantic[email]
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]