# django-yadpt-starter

`django-yadpt-starter` is Yet Another Django Project Template skeleton for Django projects.

While there is no shortage of Template Skeletons for Django projects, the aim of this one is to provide you, to the extent possible, with a fully automated setup using `Docker Containers` and a [Let's Encrypt](https://letsencrypt.org) SSL certificate for your site, all while adhering to recommended best practices. A few key features are:

- Configuration performed by `django-yadpt-starter`, a small utility that makes it trivial to setup your project;
- Automatic generation and renewal of [Let's Encrypt](https://letsencrypt.org) certificates;
- Adheres to best practices;
- Provides different environments: One without a valid certificate for local development and another with a valid certificate (for Production or Staging).

Once finished there should be 2 templates: a **minimal** but functional template and a more complete template.

## Usage

Getting your shiny new Django project up and running, complete with SSL certificates, is as easy as following these simple steps:

1. Install `django-yadpt-starter` utility

		pip install django-yadpt-starter

2. Create your project structure

		django-yadpt-starter.py -e ENVIRONMENT PROJECT_NAME

	- `ENVIRONMENT` must be either `production` or `dev` _(SSL certificates are only created production)_
	- `PROJECT_NAME` is the name you wish to give your project. Bear in mind that this name will be used throughout the Docker environment (volumes, containers, networks, etc.)

3. Add your beautifully crafted code and then start the `Docker Containers`. Please note that choosing your environment properly is very important for your docker-compose ".yml" . If you are still developing use dev.yml (Dev mode does not use Nginx). The default one is for Production, so do not use this one on your local machine while developing otherwise you will run into errors.

		cd path/to/PROJECT_NAME
		docker-compose -f {env}.yml build
		docker-compose -f {env}.yml up -d

4. At the moment you will probably run into some errors (because of issue https://github.com/psychok7/django-yadpt-starter/issues/13) and to fix them you must manually go into the docker container and delete the content of the database as explained. After that just run `docker-compose up -d --force-recreate`.

5. There is no step 5, just enjoy!

**Note:** `django-yadpt-starter` can be run as many times as you like in order to create multiple environments, there are however some caveats:

1. **PROJECT_NAME** must be something unique to ensure that volumes and containers don't collide;
2. Since certbot is using the [`--standalone`](https://certbot.eff.org/docs/using.html#standalone) plugin which binds to ports `80` and `443`, you need to stop any running containers or services that may already be bound to those ports;


### Migrating existing code from one Environment to another.


If you have running code already deployed and eventually want to switch machines or have the same code running on another machine (from dev to production for example) you can do it manually. But before that, make sure the project you created from the `dev` environment has everything it needs, like for example the `server_name` in `nginx.conf` is filled and you also have your domain in `letsencrypt.conf`. The easiest way might still be you creating an empty project with the `production` environment in your final machine so that all theses gaps can be automatically filled and then copy that folder to your local machine and add your existing code into it and push it to your git repository (or push it directly to git from your prod server if you have write permissions). This is still something we haven't really found an easy way to solve, nevertheless once you learn the project structure this migration becomes fast and painless. So after filling in just:

```
1. docker-compose -f staging.yml build
2. docker-compose -f staging.yml up # will throw errors, but it's ok
3. docker-compose -f staging.yml stop
4. docker volume ls # And get the name volume to pass to the the follwing command. e.g: smal_smal_https_certs 
5. docker run -it --rm -v {named_volume from step 4}:/etc/letsencrypt -p 80:80 -p 443:443 palobo/certbot:1.1 certonly -t -n --standalone --preferred-challenges http-01 --email {email} --agree-tos -d {domain}
6. docker-compose -f staging.yml build
7. docker-compose -f staging.yml up # Everything should be fine now.
```

### Advanced Usage

`django-yadpt-starter` will ask you for a `domain` name. If you require more than one domain (ex. domain.com and www.domain.com) then simply run through the startup script and then, before starting the containers, run

`docker run -it --rm -v {project_name}_https_certs:/etc/letsencrypt -p 80:80 -p 443:443 palobo/certbot:1.1 certonly -t -n --standalone --agree-tos -d {domain} -d {domain} -d {domain} -m myemail@example.com`

If for some reason you decide to add a new domain to the list of existing domains, you will need to use the `expand` and replace the existing certificate with a new certificate. Remember to re-add all the domains that where there already with the new one.

`docker run -it --rm -v {project_name}_https_certs:/etc/letsencrypt -p 80:80 -p 443:443 palobo/certbot:1.1 certonly -t -n --standalone --expand --agree-tos -d {domain} -d {domain} -d {domain} -m myemail@example.com`


## Free HTTPS (SSL/TLS) for websites (Let's Encrypt certificates) using Certbot

For environments where a certificate is generated (staging or production), [Certbot](https://certbot.eff.org) is used to generate a a [Let's Encrypt](https://letsencrypt.org) certificate. The only requirement is that you already have DNS setup so that you Django app is already reachable.

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
