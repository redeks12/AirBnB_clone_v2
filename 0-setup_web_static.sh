#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static.
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
    sudo ufw allow 'Nginx HTTP'
fi

if [ ! -d /data/ ]; then
    sudo mkdir /data/
fi

if [ ! -d /data/web_static/ ]; then
    sudo mkdir /data/web_static/
fi

if [ ! -d /data/web_static/releases/ ]; then
    sudo mkdir /data/web_static/releases/
fi

if [ ! -d /data/web_static/shared/ ]; then
    sudo mkdir /data/web_static/shared/
fi

if [ ! -d /data/web_static/releases/test ]; then
    sudo mkdir /data/web_static/releases/test
fi
myhtml = "<!DOCTYPE html>
<html lang='en'>
<head>
</head>
<body>
    my html
</body>
</html>"

sudo touch /data/web_static/releases/test/index.html
sudo echo $myhtml > /data/web_static/releases/test/index.html

if [ -d /data/web_static/current/ ]; then
    sudo rm /data/web_static/current/
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data
