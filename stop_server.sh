#!/bin/bash
sudo killall `ps ax | grep "pywms.wsgi:application" | grep -v grep | awk -F' ' '{print $5}' | tail -1`
