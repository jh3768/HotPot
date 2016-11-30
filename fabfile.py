
from __future__ import with_statement
from fabric.api import local, settings, abort
from fabric.contrib.console import confirm


def test():
    with settings(warn_only=True):
        result = local('python3 manage.py test polls/test2', capture=True)
    if result.succeeded:
        print ("All tests passed !")
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")




def commit():
    test()
    local("git add -p && git commit")

def push():
    test()
    local("git push -u origin master")

def prepare_deploy():
    test()
    commit()
    push()

def deploy():
    test()
    local("python3 manage.py runserver")


