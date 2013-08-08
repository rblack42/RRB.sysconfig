from fabric.api import *

def build():
    """build sphinx html docs"""
    local('sphinx-build -b html -d _build/doctrees . _build/html')

def push():
    """push current version to Git repo"""
    local('git add --all .')
    msg = raw_input("Commit message: ")
    local('git commit -m "%s"' % msg)
    local('git push origin master')

