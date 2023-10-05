#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers,
using the function do_deploy:"""

import os

from fabric.api import put, run, task, sudo, env


env.hosts = ["54.145.85.177", "100.25.17.121"]
env.user = "ubuntu"
env.password = "betty"


@task
def do_deploy(archive_path):
    """Prototype: def do_deploy(archive_path):
    Returns False if the file at the path archive_path doesn’t exist
    The script should take the following steps:
    Upload the archive to the /tmp/ directory of the web server
    Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
    Delete the archive from the web server"""
    if not os.path.exists(archive_path):
        print(archive_path)
        return False
    try:
        fl = archive_path.split("/")[1]
        r = fl.split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(r))
        run("tar -xzvf /tmp/{} -C /data/web_static/releases/{}/".format(fl, r))
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
