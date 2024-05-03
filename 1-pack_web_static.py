#!/usr/bin/python3
"""Package web static module"""

import datetime
import os
from fabric.api import local


def do_pack():
    """package fn"""

    if not os.path.isdir("./versions"):
        os.makedirs("./versions")
    nt = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local("tar -czzf versions/web_static_{}.tgz web_static/*".format(nt))
    return ("{}/versions/web_static_{}.tgz".format(os.path.dirname(
        os.path.abspath(__file__)), nt))
