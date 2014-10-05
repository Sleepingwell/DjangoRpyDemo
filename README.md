## Installation

If you have [Django](https://www.djangoproject.com/) and [rpy2](rpy.sourceforge.net/) installed, you should be able to just run:

    python manage.py runserver

in the top level directory to get this going.

If you don't have Rpy2 installed, then you need to have [pyRserve](https://pypi.python.org/pypi/pyRserve/) and the R package [Rserve](http://rforge.net/Rserve/) installed and Rserve running before making the above call.

Note that the R shared library is not reentrant and hence should not accessed from multiple threads. It is also worth noting that one should not assume anything about the state of R's global workspace between requests.

## Notes for Linux

gonavald and dzhibas note that on linux:
you can install django, R and Rpy2 with:

    sudo pip install django
    sudo apt-get install r-base-core
    sudo pip install rpy2

and to make the R shared library available:

    cd /usr/lib/
    sudo ln -s /usr/lib/R/lib/libR.so
