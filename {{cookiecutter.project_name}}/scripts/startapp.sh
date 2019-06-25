dirname=$1

make_module() {
    subdirname=$1
    mkdir $subdirname
    touch $subdirname/__init__.py
}

if [ $# -eq 0 ]
    then
        echo "You should into parameter to create app"
        exit
fi

# Do magic
APPS_DIR=apps

cd $APPS_DIR
mkdir $dirname

cd $dirname

echo """# -*- coding: utf-8 -*-

from fastapi.routing import APIRouter
router = APIRouter()
""" > urls.py


make_module views
make_module serializers
make_module constants
make_module models
make_module services
make_module tests
make_module depends

cd ../../