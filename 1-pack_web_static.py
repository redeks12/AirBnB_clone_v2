#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack."""
import os
from datetime import datetime

from fabric.api import local, task


@task
def do_pack():
    """Write a Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.

    Prototype: def do_pack():
    All files in the folder web_static must be added to the final archive
    All archives must be stored in the folder versions (your function should create this folder if it doesn’t exist)
    The name of the archive created must be web_static_<year><month><day><hour><minute><second>.tgz
    The function do_pack must return the archive path if the archive has been correctly generated. Otherwise, it should return None
    """
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
