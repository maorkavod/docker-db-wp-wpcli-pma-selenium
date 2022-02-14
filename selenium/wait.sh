#!/bin/sh

until $(curl --output /dev/null --silent --head --fail http://wp); do
    printf 'waiting for wp http status 200 code.'
    sleep 1
done

python3 app.py