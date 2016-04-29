#!/bin/bash

# Based on http://stackoverflow.com/a/28508138/977622 for cleaning celery .pid
echo "Removing .pid files"
rm -f *.pid
exec "$@"