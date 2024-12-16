FROM python:3.11
WORKDIR /app_dir
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
EXPOSE 5000

CMD ["tail", "-f", "/dev/null"]