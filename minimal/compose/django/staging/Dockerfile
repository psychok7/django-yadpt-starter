FROM ubuntu:16.04
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y \
  build-essential \
  git-core \
  python3 \
  python3-pip \
  python3-dev \
  libpq-dev \
  postgresql-client-9.5 \
  libjpeg-dev \
  binutils \
  libproj-dev \
  gdal-bin \
  libxml2-dev \
  libxslt1-dev \
  zlib1g-dev \
  libffi-dev \
  libssl-dev \
  ipython

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements

RUN pip3 install -r /requirements/staging.txt

COPY ./compose/django/staging/gunicorn.sh /gunicorn.sh
COPY ./compose/django/staging/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN sed -i 's/\r//' /gunicorn.sh
RUN chmod +x /entrypoint.sh
RUN chmod +x /gunicorn.sh

COPY . /code
WORKDIR /code

ENTRYPOINT ["/entrypoint.sh"]
