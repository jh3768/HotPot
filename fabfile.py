''' fabric CI tool '''
from __future__ import with_statement
from fabric.api import local, settings, abort
from fabric.contrib.console import confirm

def test():
    ''' run test suite '''
    with settings(warn_only=True):
        result = local('python3 manage.py test polls/test2', capture=True)
    if result.succeeded:
        print("All tests passed !")
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def commit():
    ''' run test before commit '''
    test()
    local("git commit -am 'Test CI' ")

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
    local("python3 manage.py runserver")
