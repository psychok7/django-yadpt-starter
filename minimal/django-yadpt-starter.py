#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import shutil
import subprocess

# Python 2/3 support
from six.moves import input, urllib
from email.utils import parseaddr

# Point this to a tag with the latest code.
TEMPLATE_VERSION_TAG = '1.2'

# Make sure you have Django 1.8.x installed in the appropriate Python version
# you are using (either pip3 or pip).


def user_input():
    email = input('Please enter the email: ')

    email_is_valid = parseaddr(email)
    if '@' not in email_is_valid[1]:
        raise ValueError("Please enter a valid email")

    domain = input('Please enter the domain: ')

    if not email or not domain:
        raise ValueError("Please enter the email and domain")

    return email, domain


def fetch_latest_template(project_name, email, domain):
    tag_version = TEMPLATE_VERSION_TAG
    extension = 'py, yml, conf, sh'

    # Download forked django-startproject.py from
    # https://github.com/alfredo/django-startproject-plus in order to pass
    # extra-context variables.
    urllib.request.urlretrieve(
        'https://raw.githubusercontent.com/psychok7/django-startproject-plus/'
        'master/django-startproject.py', 'django-startproject.py'
    )

    template = (
        'https://github.com/psychok7/django-yadpt-starter/archive/'
        'v{tag_version}.zip'.format(**locals())
    )

    if sys.version_info >= (3, 0):
        python_version = 'python3'
    else:
        python_version = 'python'

    extra_context = '{"EMAIL": "' + email + '", "DOMAIN": "' + domain + '"}'

    generate_template = (
        '{python_version} django-startproject.py {project_name} '
        '--template={template} '
        '--extension="{extension}" --settings=_config.dummy_settings'.format(**locals())
    )
    generate_template += " --extra_context='" + extra_context + "'"

    print('generate_template: {generate_template}'.format(**locals()))

    subprocess.call([generate_template], shell=True)


def generate_cerbot_certs(project_name, email, domain):
    generate_certs = (
        'docker run -it --rm -v {project_name}_https_certs:/etc/letsencrypt '
        '-p 80:80 -p 443:443 palobo/certbot:1.0 certonly -t -n --standalone '
        '-d {domain} -m {email} --agree-tos'.format(**locals())
    )
    print('generate_certs: ', generate_certs)

    subprocess.call([generate_certs], shell=True)


def _cleanup(project_name):
    print('Cleaning...')
    if not os.path.exists(project_name):
        raise ValueError('Something went wrong')
    else:
        # Copy the sub-folder inside /minimal one level up and delete
        # unnecessary files.
        os.rename(project_name, 'temp')
        os.chdir('temp')
        os.rename('minimal', project_name)
        os.chdir('../')
        shutil.move('temp/' + project_name + '/', '.')
        shutil.rmtree('temp/')
        shutil.rmtree(project_name + '/_config/')
        os.remove(project_name + '/django-yadpt-starter.py')

        if os.path.exists('django-startproject.py'):
            os.remove('django-startproject.py')

        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Django Project Template Startup Script')
    parser.add_argument(
        '-e', '--environment', help='Environment', required=True)
    parser.add_argument('project_name', nargs='?', type=str)

    args = vars(parser.parse_args())

    project_name = args['project_name']

    if args['environment'] == 'production' or args['environment'] == 'staging':
        email, domain = user_input()
        fetch_latest_template(
            project_name=project_name, email=email, domain=domain)
        _cleanup(project_name=project_name)
        print('Generating HTTPS certs...')
        print('Please ensure this machine owns the domain.')
        generate_cerbot_certs(
            project_name=project_name, email=email, domain=domain)

    elif args['environment'] == 'dev':
        tag_version = TEMPLATE_VERSION_TAG
        extension = 'py, yml, conf, sh'
        template = (
            'https://github.com/psychok7/django-yadpt-starter/archive/'
            'v{tag_version}.zip'.format(**locals())
        )
        generate_template = (
            'django-admin startproject {project_name} --template={template} '
            '--extension="{extension}"'.format(**locals())
        )

        print('generate_template dev: {generate_template}'.format(**locals()))

        subprocess.call([generate_template], shell=True)

        _cleanup(project_name=project_name)

    else:
        raise ValueError("environment not allowed")
