#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack."""
import os
from datetime import datetime

from fabric.api import env, local, put, run, task

env.hosts = ["54.145.85.177", "100.25.17.121"]
# env.password = "betty"
env.forward_agent = True


@task
def do_pack():
    """Write a Fabric script that generates a .tgz archive from the contents of the web_static folder"""
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


@task
def do_deploy(archive_path):
    """Prototype: def do_deploy(archive_path)r"""
    if not os.path.exists(archive_path):
        print(archive_path)
        return False
    try:
        fl = archive_path.split("/")[1]
        r = fl.split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(r))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(fl, r))
        run(
            "mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(
                r, r
            )
        )
        run("rm -rf /data/web_static/releases/{}/web_static".format(r))
        run("rm -rf /tmp/{}".format(fl))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current".format(r))
        return True
    except:
        return False

@task
def deploy():
    """deploying using the previous tasks"""
    package = do_pack()
    if package is None:
        return False
    return do_deploy(package)
