#!/bin/bash
cd /home/$USER/Web/project/
source env/bin/activate
cd src/
gunicorn --reload -b localhost:8080 application.wsgi:application
