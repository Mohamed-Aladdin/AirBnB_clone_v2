#!/usr/bin/python3
"""Deploy and push package module"""

import os
from fabric.api import put, env, run


env.hosts = ["52.6.173.34", "52.3.248.217"]

env.user = "ubuntu"


def do_deploy(arch_path):
    """deploy the package fn"""

    if arch_path is None or not os.path.isfile(arch_path):
        print("NOT PATH")
        return False

    aname = os.path.basename(arch_path)
    rname = aname.split(".")[0]

    put(local_path=arch_path, remote_path="/tmp/")
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
