FROM nginx:1.13.1-alpine

ADD nginx.conf /etc/nginx/nginx.conf

COPY snippets/letsencrypt.conf /etc/nginx/snippets/letsencrypt.conf
COPY snippets/ssl-params.conf /etc/nginx/snippets/ssl-params.conf