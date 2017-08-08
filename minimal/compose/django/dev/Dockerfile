FROM python:3.6.2
ENV PYTHONUNBUFFERED 1

# We need new PostgreSQL Client versions and the one in Debian 8 is old
RUN touch /etc/apt/sources.list.d/pgdg.list
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >> /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get update && apt-get install -y \
  build-essential \
  git-core \
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

RUN pip3 install -r /requirements/local.txt

COPY ./compose/django/dev/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . /code
WORKDIR /code

ENTRYPOINT ["/entrypoint.sh"]
