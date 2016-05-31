=============================
django-project-template-yadpt
=============================

`django-project-template-yadpt` is Yet Another Django Project Template skeleton for Django projects.

There will be two template versions once it is finished, being one a minimal one and another one more complete one.

I am using `Docker` as well in the template, with a Production, Staging, and Local development version.


Installation
============

To install, simply copy this repository to your custom location, and run the following command specifiying the `--template` location to the location where you cloned the `django-project-template-yadpt` repository


Usage
============

After installing django-project-template-yadpt, simply run the following command (from within
the directory in where the new project directory should be created):

	django-admin startproject project_name  --template=/your_path/django-project-template-yadpt/minimal/ --extension='py, yml, conf, sh'


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

See the files included in the project_template directory for an example.

