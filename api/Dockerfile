FROM python:3.11
RUN mkdir /backend
WORKDIR /backend
COPY requirements.txt /backend/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python3"]
CMD ["app.py"]