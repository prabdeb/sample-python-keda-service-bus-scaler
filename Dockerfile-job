FROM python:3.8

RUN mkdir /job
WORKDIR /job
ADD requirements.txt /job/
RUN pip install -r requirements.txt

ADD src-message-consumer/receive_message_queue_job.py /job/main.py
CMD ["python", "/job/main.py"]
