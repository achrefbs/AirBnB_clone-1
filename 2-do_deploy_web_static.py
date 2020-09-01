#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""
from datetime import datetime
from os.path import isdir
from fabric.api import local, run, put, env
from os import path as p


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


def do_deploy(archive_path):
    """
    a Fabric script (based on the file 1-pack_web_static.py) that distributes
    an archive to your web servers, using the function do_deploy
    """
    if not p.exists(archive_path) and p.isfile(archive_path):
        return False
    fle = archive_path.split("/")[-1].split(".")[0]
    path = "/data/web_static/releases/{}/web_static/*".format(fle)
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}/".format(fle))
        run("sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".
            format(fle, fle))
        run("sudo rm /tmp/{}.tgz".format(fle))
        run("sudo mv {} /data/web_static/releases/{}/".format(path, fle))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".
            format(fle))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(fle))
        return True
    except:
        return False
    return True
