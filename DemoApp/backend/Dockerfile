FROM python:3.8.6-slim
COPY . .
EXPOSE 5000

RUN python3 -m venv venv
RUN pip install -r requirements.txt

CMD ["python3", "runner.py"]
