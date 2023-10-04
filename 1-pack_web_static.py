#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import task, local
from datetime import datetime
import os

# from fabric.decorators import task


@task
def do_pack():
    date_now = datetime.now()
    print(
        "{}{}{}{}{}{}".format(
            date_now.year,
            date_now.month,
            date_now.day,
            date_now.hour,
            date_now.minute,
            date_now.second,
        )
    )
    curpth = os.getcwd()
    print(curpth)

    local("echo 'Hello, localhost!'")
