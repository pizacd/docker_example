FROM python:latest
WORKDIR /app
COPY . /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["python", "./message_printer.py"]
