from fabric.api import local

def update():
    local('git pull origin develop')
    local('rm -rf wsgi/project')
    local('cp -r project wsgi/project')

def deploy():
    local('git add .')
    local('git commit -m "deploy"')
    local('git push upstream HEAD:master')
