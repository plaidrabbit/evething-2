#!/bin/bash
. /evething-env/bin/activate
cd /evething/

if [ ! -e sqlite-latest.sqlite ]; then
    wget https://www.fuzzwork.co.uk/dump/sqlite-latest.sqlite.bz2
    bunzip2 sqlite-latest.sqlite.bz2
fi

npm install
npm install npm-check-updates

python manage.py migrate --noinput
python import.py
python manage.py createsuperuser
