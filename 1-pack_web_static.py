#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import task, local

# from fabric.decorators import task


@task
def do_pack():
    local("echo 'Hello, localhost!'")
