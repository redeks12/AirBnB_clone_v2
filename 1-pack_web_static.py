#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack."""
import os
from datetime import datetime

from fabric.api import local, task

# from fabric.decorators import task


@task
def do_pack():
    date_now = datetime.now()

    if not os.path.exists("versions") and not os.path.isdir("versions"):
        local("mkdir versions")

    filepth = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date_now.year,
        date_now.month,
        date_now.day,
        date_now.hour,
        date_now.minute,
        date_now.second,
    )
    local("tar -cvzf {} web_static".format(filepth))

    if os.path.exists(filepth):
        return filepth
    else:
        return None
