# django-project-template-yadpt

`django-project-template-yadpt` is Yet Another Django Project Template skeleton for Django projects.

While there is no shortage of Template Skeletons for Django projects, the aim of this one is to provide you, to the extent possible, with a fully automated setup using `Docker Containers` and a [Let's Encrypt](https://letsencrypt.org) SSL certificate for your site, all while adhering to recommended best practices. A few key features are:

- Configuration performed by `django-yadtp-starter`, a small utility that makes it trivial to setup your project;
- Automatic generation and renewal of [Let's Encrypt](https://letsencrypt.org) certificates;
- Adheres to best practices;
- Provides different environments: One without valid a certificate for local development and another with a valid certificate (for Production or Staging).

Once finished there should be 2 templates: a **minimal** but functional template and a more complete template.

## Usage — The TL;DR Version

Getting your shiny new Django project up and running, complete with SSL certificates, is as easy as following these simple steps:

1. Install `django-yadtp-starter` utility

		pip install django-yadtp-starter

2. Create your project structure

		python django-yadtp-starter -e ENVIRONMENT PROJECT_NAME

	- `ENVIRONMENT` must be either `production` or `dev` _(SSL certificates are only created production)_
	- `PROJECT_NAME` is the name you wish to give your project. Bear in mind that this name will be used throughout the Docker environment (volumes, containers, networks, etc.)

3. Add your beautifully crafted code and then start the `Docker Containers`

		cd PROJECT_NAME
		docker-compose build
		docker-compose up -d

4. There is no step 4, just enjoy!


## Usage — The Detailed Version

`django-yadtp-starter` is a small utility that makes setting up your Django project trivial. Essentially what it does is:

1. Downloads [`django-startproject.py`](https://github.com/psychok7/django-startproject-plus/blob/master/django-startproject.py), needed in order to pass extra-context variables;
2. Asks for email to associate with the generated certificate;
3. Asks for domain for which to generate a certificate;
4. Creates the project based on the template;
5. Launches the Certbot container and generates a certificate. _This will only be done for `production` and `staging` environment_;
6. Does a little house-keeping and cleans up after itself.

**Note:** `django-yadtp-starter` can be run as many times as you like in order to create multiple environments, there are however some caveats:

ensure you always use a different `PROJECT_NAME` each time.





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
