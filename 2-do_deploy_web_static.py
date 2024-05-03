#!/usr/bin/python3
"""Deploy and push package module"""

import os
from fabric.api import put, env, run


env.hosts = ["52.6.173.34", "52.3.248.217"]

env.user = "ubuntu"


def do_deploy(archive_path):
    """deploy the package fn"""

    if archive_path is None or not os.path.isfile(archive_path):
        print("NOT PATH")
        return False

    an = os.path.basename(archive_path)
    rn = aname.split(".")[0]

    put(local_path=archive_path, remote_path="/tmp/")
    run("mkdir -p /data/web_static/releases/{}".format(rn))
    run("tar -xzf /tmp/{} \
        -C /data/web_static/releases/{}".format(an, rn))
    run("rm /tmp/{}".format(an))
    run("rm -rf /data/web_static/current")
    run("ln -fs /data/web_static/releases/{}/ \
        /data/web_static/current".format(rn))
    run("mv /data/web_static/current/web_static/* /data/web_static/current/")
    run("rm -rf /data/web_static/curren/web_static")

    return True
