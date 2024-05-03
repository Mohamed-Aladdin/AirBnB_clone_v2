#!/usr/bin/python3
"""Deploy and package module"""

import datetime
import os
from fabric.api import put, env, run, local


env.hosts = ["52.6.173.34", "52.3.248.217"]

env.user = "ubuntu"


def do_deploy(archive_path):
    """deploy the package fn"""

    if archive_path is None or not os.path.isfile(archive_path):
        print("NOT PATH")
        return False

    aname = os.path.basename(archive_path)
    rname = aname.split(".")[0]

    put(local_path=archive_path, remote_path="/tmp/")
    run("mkdir -p /data/web_static/releases/{}".format(rname))
    run("tar -xzf /tmp/{} \
        -C /data/web_static/releases/{}".format(aname, rname))
    run("rm /tmp/{}".format(aname))
    run("rm -rf /data/web_static/current")
    run("ln -fs /data/web_static/releases/{}/ \
        /data/web_static/current".format(rname))
    run("mv /data/web_static/current/web_static/* /data/web_static/current/")
    run("rm -rf /data/web_static/curren/web_static")

    return True


def do_pack():
    """package fn"""
    if not os.path.isdir("./versions"):
        os.makedirs("./versions")
    nt = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local("tar -czzf versions/web_static_{}.tgz web_static/*".format(nt))
    return ("{}/versions/web_static_{}.tgz".format(os.path.dirname(
        os.path.abspath(__file__)), nt))


def deploy():
    """package and deploy to the servers fn"""

    path = do_pack()
    if path is None:
        return False
    return (do_deploy(path))
