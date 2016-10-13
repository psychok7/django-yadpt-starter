# django-project-template-yadpt

`django-project-template-yadpt` is Yet Another Django Project Template skeleton for Django projects.

The aim of this template is to provide There will be two template versions once it is finished, being one a minimal one and another one more complete one.

I am using `Docker` as well in the template, with a Production, Staging, and Local development version.

## Usage - The Short Version

If you're in a rush to get your shiny new django project up and running, complete with SSL certificates, then simply follow these 3 simple steps:

1. Install `django-project-template-yadpt` setup script.

		pip install yadtp-setup

2. Create your project structure

		python yadtp-setup -e ENVIRONMENT PROJECT_NAME

	- `ENVIRONMENT` must be either `production`, `staging` or `dev` _(SSL certificates are only created for staging and production)_
	- `PROJECT_NAME` is the name you wish to give your project. Bear in mind that this name will be used throughout the Docker environment (volumes, containers, networks, etc.)

3. Add your beautifully crafted code and then start Docker Containers

		cd PROJECT_NAME
		docker-compose build
		docker-compose up -d

4. Enjoy!


## Usage - The Detailed Version


To install, simply copy this repository to your custom location, and run the following command specifiying the `--template` location to the location where you cloned the `django-project-template-yadpt` repository


Usage
============

After installing django-project-template-yadpt, simply run the following command (from within
the directory in where the new project directory should be created):

	django-admin startproject project_name  --template=/your_path/django-project-template-yadpt/minimal/ --extension='py, yml, conf, sh'


Free HTTPS (SSL/TLS) for websites (Let's Encrypt certificates) using Certbot
=============================================================================

For Staging and Production Environments, a [Let's Encrypt](https://letsencrypt.org) Certificate is generated using [Certbot](https://certbot.eff.org).
In this instance, Certbot is uses the `--webroot` plugin which creates a temporary file in `WEBROOT_PATH/.well-known` to validate correct ownership of your domain after which it will generate a certificate and place it in `/etc/letsencrypt/live/DOMAIN`.

Before building and starting your staging or production containers you need to ensure that:

- `staging.env` and `production.env` have the correct `EMAIL=` and `DOMAIN=` information filled out;
- Your django app must already be reachable at `DOMAIN`, meaning DNS must already be configured properly;

**Note:** Given there is a daily cron job which checks to see if the certificate is up for renewal, it's essential the container is always kept running.


Used Third Party Apps
=====================

 - https://github.com/docker/docker
 - https://github.com/docker/compose
 - https://github.com/fusionbox/django-authtools
 - https://github.com/django-extensions/django-extensions
 - https://github.com/django-dbbackup/django-dbbackup
 - https://github.com/brack3t/django-braces
 - https://github.com/sebleier/django-redis-cache
 - https://github.com/getsentry/raven-python
 - https://github.com/kennethreitz/requests
 - https://github.com/nedbat/coveragepy
 - https://github.com/certbot/certbot

See the files included in the project_template directory for an example.
