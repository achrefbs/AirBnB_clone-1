#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""
from datetime import datetime
from os.path import isdir
from fabric.api import local


def do_pack():
    """a Fabric script that generates a .tgz archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{:s}.tgz web_static/".format(
                                                                        date))
        return ("versions/web_static_{:s}.tgz".format(date))
    except:
        return None
