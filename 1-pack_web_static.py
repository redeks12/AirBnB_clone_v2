#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric import task, Connection


@task
def do_pack():
    c = Connection(host="localhost")
    c.local("echo 'Hello, localhost!'")
