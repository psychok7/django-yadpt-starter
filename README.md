# django-project-template-yadpt

`django-project-template-yadpt` is Yet Another Django Project Template skeleton for Django projects.

While there is no shortage of Template Skeletons for Django projects, the aim of this one is to provide you, to the extent possible, with a fully automated setup using `Docker Containers` and a [Let's Encrypt](https://letsencrypt.org) SSL certificate for your site, all while adhering to recommended best practices. A few key features are:

- `django-yadtp-starter` is a small utility that makes it trivial to setup you project;
- Automatic generation and renewal of site's certificates;
- Adheres to best practices;
- Provides 3 distinct environments: Production, Staging, and Local development version

Once finished there should be 2 templates: a **minimal** but functional template and a more complete template.


## Usage - The Short Version

If you're in a rush to get your shiny new django project up and running, complete with SSL certificates, then just follow these 3 steps:

1. Install `django-yadtp-starter` utility

		pip install django-yadtp-starter

2. Create your project structure

		python yadtp-setup -e ENVIRONMENT PROJECT_NAME

	- `ENVIRONMENT` must be either `production`, `staging` or `dev` _(SSL certificates are only created for staging and production)_
	- `PROJECT_NAME` is the name you wish to give your project. Bear in mind that this name will be used throughout the Docker environment (volumes, containers, networks, etc.)

3. Add your beautifully crafted code and then start the `Docker Containers`

		cd PROJECT_NAME
		docker-compose build
		docker-compose up -d

4. Enjoy!


## Usage - The Detailed Version

`django-yadtp-starter` is a small utility that makes setting up your Django project trivial. While it greatly eases setup, there may be times when you need to do things manually (maybe you're running staging and production on the same host, or simply want to impress your friends (⌐■_■) ). Before explainig how to do things manually, let's have a look at what `django-yadtp-starter` does:

1. Downloads [`django-startproject.py`](https://github.com/psychok7/django-startproject-plus/blob/master/django-startproject.py), needed in order to pass extra-context variables;
2. Asks for email to associate with the generated certificate;
3. Asks for domain for which to generate a certificate;
4. Creates the project based on the template;
5. Launches certbot container and generates a certificate. This will only be done for `production` and `staging` environment;
6. Does a little house-keeping and cleans up after itself.


### Getting Your Environment Ready

1. Download [`django-startproject.py`](https://github.com/psychok7/django-startproject-plus/blob/master/django-startproject.py) to a location where you intend the place your project
2. Download or clone this repository

	git clone https://github.com/psychok7/django-project-template-yadpt.git DJANGO_PROJECT_TEMPLATE_PATH

3. Generate the project structure

	python django-startproject.py --template=[PATH TO DJANGO_PROJECT_TEMPLATE_PATH/minimal] \
								  --extension='py, yml, conf, sh' \
								  --extra_context='{"EMAIL": "YOUR_EMAIL", "DOMAIN": "YOUR_DOMAIN"}'


To install, simply copy this repository to your custom location, and run the following command specifiying the `--template` location to the location where you cloned the `django-project-template-yadpt` repository


After installing django-project-template-yadpt, simply run the following command (from within
the directory in where the new project directory should be created):

	django-admin startproject project_name  --template=/your_path/django-project-template-yadpt/minimal/ --extension='py, yml, conf, sh'


## Free HTTPS (SSL/TLS) for websites (Let's Encrypt certificates) using Certbot


For Staging and Production Environments, a [Let's Encrypt](https://letsencrypt.org) Certificate is generated using [Certbot](https://certbot.eff.org).
In this instance, Certbot uses the `--webroot` plugin which creates a temporary file in `WEBROOT_PATH/.well-known` to validate correct ownership of your domain after which it will generate a certificate and place it in `/etc/letsencrypt/live/DOMAIN`.

Before building and starting your staging or production containers you need to ensure that:

- `staging.env` and `production.env` have the correct `EMAIL=` and `DOMAIN=` information filled out;
- Your django app must already be reachable at `DOMAIN`, meaning DNS must already be configured properly;

**Note:** Given there is a daily cron job which checks to see if the certificate is up for renewal, it's essential the container is always kept running.


## Used Third Party Apps

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
