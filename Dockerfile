FROM python:3.9
ADD requirements.txt /app/
RUN pip install -r /app/requirements