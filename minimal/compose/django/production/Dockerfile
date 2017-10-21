FROM python:3.6.3-stretch
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
  build-essential \
  git-core \
  libpq-dev \
  postgresql-client-9.6 \
  libjpeg-dev \
  binutils \
  libproj-dev \
  gdal-bin \
  libxml2-dev \
  libxslt1-dev \
  zlib1g-dev \
  libffi-dev \
  libssl-dev \
  ipython \
  locales -qq

RUN dpkg-reconfigure locales
# Set the locale
RUN locale-gen C.UTF-8
ENV LANG C.UTF-8
ENV LANGUAGE C:en
ENV LC_ALL C.UTF-8
ENV LC_CTYPE C.UTF-8
RUN locale

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements

RUN pip3 install -r /requirements/production.txt

COPY ./compose/django/production/gunicorn.sh /gunicorn.sh
COPY ./compose/django/production/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN sed -i 's/\r//' /gunicorn.sh
RUN chmod +x /entrypoint.sh
RUN chmod +x /gunicorn.sh

COPY . /code
WORKDIR /code

ENTRYPOINT ["/entrypoint.sh"]
