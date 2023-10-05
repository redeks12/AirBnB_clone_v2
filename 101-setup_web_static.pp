#!/usr/bin/env bash
# using puppet to configure ssh

$myhtml="<!DOCTYPE html>
<html lang='en'>
    <head>
        <title>My HTML Page</title>
    </head>
    <body>
        <p>My HTML Page</p>
    </body>
</html>
"
package { 'nginx':
    ensure => 'installed',
}

exec { "execute":
    command => 'sudo mkdir -p /data/web_static/releases/test/;
    sudo mkdir -p /data/web_static/shared/;
    sudo touch /data/web_static/releases/test/index.html;
    sudo echo "${myhtml}" > /data/web_static/releases/test/index.html;
    if [ -f /data/web_static/current ]; then sudo rm -rf /data/web_static/current fi;
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current;
    sudo chown -R ubuntu:ubuntu /data/;
    sudo sed -i "s|server_name _;|server_name _;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\ttry_files \$uri \$uri/ =404;\n\t}|" /etc/nginx/sites-enabled/default;
    sudo nginx -t;
    sudo service nginx restart;',
    provider => 'shell',

}