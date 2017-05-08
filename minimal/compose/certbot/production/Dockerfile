FROM palobo/certbot:1.1

COPY certbot-renew /etc/periodic/daily/
RUN chmod +x /etc/periodic/daily/certbot-renew

ENTRYPOINT ["crond"]
CMD ["-f", "-L", "/var/log/crond.log"]
# To ensure that crond is pid1 we start it in foreground with -f
# We also need to see if crond is behaving so we to log to FILE with -L FILE
