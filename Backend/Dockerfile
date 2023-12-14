FROM --platform=$BUILDPLATFORM python:3.12.0 AS builder
WORKDIR /app
COPY requirement.txt /app
RUN pip install -r requirement.txt --no-cache-dir
COPY . /app
# Use ENTRYPOINT and CMD for better environment variable expansion
ENTRYPOINT ["bash", "-c"]
CMD ["echo $INTERNAL_PORT && python manage.py migrate && python manage.py runserver 0.0.0.0:$INTERNAL_PORT"]
