#!/usr/bin/env bash

# Sets up the database for the project with few datas

mysql -u wtfo -pcompany -e "DROP DATABASE IF EXISTS housing; CREATE DATABASE IF NOT EXISTS housing;"
echo -e '\n[-- CLEANED DATABASES --]\n'
python ../manage.py syncdb --noinput
echo -e '\n[-- CREATED TABLES --]\n'
python ../manage.py shell < database.py > /dev/null
echo -e '\n[-- FILLED TABLES --]\n'
