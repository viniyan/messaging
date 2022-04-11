FROM python:alpine

WORKDIR /cel
RUN pip install celery
COPY tasks.py /cel/tasks.py
EXPOSE 5000
CMD ["celery", "-A", "tasks", "worker", "--loglevel=info"]
