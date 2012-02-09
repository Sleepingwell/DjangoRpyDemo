## Installation

If you have Django and Rpy2 installed, you should be able to just run:

    python manage.py runserver

in the top level directory to get this going.

## Notes for Linux

gonavald and dzhibas note that on linux:
you can install django, R and Rpy2 with:

    sudo pip install django
    sudo apt-get install r-base-core
    sudo pip install rpy2

and to make the R shared library available:

    cd /usr/lib/
    sudo ln -s /usr/lib/R/lib/libR.so
