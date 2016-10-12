# -*- coding: utf-8 -*-

import argparse
import subprocess

from email.utils import parseaddr

# TODO: point this to a new tag with the latest code. this one is an old one.
TEMPLATE_VERSION_TAG = '0.2'

# TODO: we still need to load the Extracontext into the template files.


def user_input():
    email = input('Please enter the email: ')

    email_is_valid = parseaddr(email)
    if '@' not in email_is_valid[1]:
        raise ValueError("Please enter a valid email")

    domain = input('Please enter the domain: ')

    if not email or not domain:
        raise ValueError("Please enter the email and domain")

    return email, domain


def fetch_latest_template(project_name):
    tag_version = TEMPLATE_VERSION_TAG
    extension = 'py, yml, conf, sh'
    template = (
        'https://github.com/psychok7/django-project-template-yadpt/archive/'
        'v{tag_version}.zip'.format(**locals())
    )
    generate_template = (
        'django-admin startproject {project_name} '
        '--template={template} '
        '--extension="{extension}"'.format(**locals())
    )
    print('generate_template: {generate_template}'.format(**locals()))

    # TODO: uncomment this after it is tested
    # subprocess.call([generate_template], shell=True)


def generate_cerbot_certs(project_name, email, domain):
    generate_certs = (
        'docker run -it --rm -v {project_name}_https_certs:/etc/letsencrypt '
        '-p 80:80 -p 443:443 palobo/certbot:1.0 certonly -t -n --standalone '
        '-d {domain} -m {email} --agree-tos'.format(**locals())
    )
    print('generate_certs: ', generate_certs)

    # TODO: uncomment this after it is tested
    # subprocess.call([generate_certs], shell=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Django Project Template Startup Script')
    parser.add_argument(
        '-e', '--environment', help='Environment', required=True)
    parser.add_argument('project_name', nargs='?', type=str)

    args = vars(parser.parse_args())

    if args['environment'] == 'production' or args['environment'] == 'staging':
        print(args)
        email, domain = user_input()
        fetch_latest_template(project_name=args['project_name'])
        generate_cerbot_certs(
            project_name=args['project_name'], email=email, domain=domain)
    else:
        raise ValueError("environment not allowed")
