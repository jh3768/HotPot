''' fabric CI tool '''
from __future__ import with_statement
from fabric.api import local, settings, abort
from fabric.contrib.console import confirm

def test():
    ''' run test suite '''
    with settings(warn_only=True):
        result = local('python3 manage.py test polls/test2', capture=True)
    if result.succeeded:
        print (result.stderr)
        print("All tests passed !")
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")


def commit():
    ''' run test before commit '''
    message = raw_input("Enter a git commit message:  ")
    test()
    local("git commit -am \"%s\"" % message)


def pull():
    ''' make working dir up-to-date'''
    local("git pull")


def push():
    ''' run test before push '''
    test()
    local("git push -u origin master")

def prepare_deploy():
    ''' prepare deployment '''
    test()
    commit()
    push()

def deploy():
    ''' run test before deployment '''
    test()
    local('python3 manage.py runserver')
