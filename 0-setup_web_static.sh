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

if [ ! -d /data/web_static/releases/test/ ]; then
    sudo mkdir /data/web_static/releases/test/
fi
myhtml="<!DOCTYPE html>
<html lang='en'>
    <head>
        <title>My HTML Page</title>
    </head>
    <body>
        <p>My HTML Page</p>
    </body>
</html>
"

sudo touch /data/web_static/releases/test/index.html
sudo echo "$myhtml" > /data/web_static/releases/test/index.html

if [ -f /data/web_static/current ]; then
    sudo rm -r /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "s|server_name _;|server_name _;\n\tlocation /hbnb_static {\n\talias /data/web_static/current;/\n}|" /etc/nginx/sites-enabled/default

sudo nginx -t

sudo nginx restart
