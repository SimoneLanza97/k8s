FROM python:3.9.18-bullseye
WORKDIR /app
COPY ./application /app
RUN pip install -r requirements.txt 
ENTRYPOINT ["python3", "app.py"]