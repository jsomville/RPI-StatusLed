#!/bin/bash

#install program
mkdir -p /usr/bin/statusled
cp statusled.py /usr/bin/statusled/

#copy service file
cp statusled.service /lib/systemd/system/

