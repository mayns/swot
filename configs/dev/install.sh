#!/usr/bin/env bash

# You also need Postgres on port 5432
# and database swot

sudo apt-get install python3-dev -y && sudo apt-get install python3-pip &&
sudo pip3 install django psycopg2 simplejson