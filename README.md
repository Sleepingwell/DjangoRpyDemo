## Installation

If you have Django and Rpy2 installed, you should be able to just run:

    python manage.py runserver

in the top level directory to get this going.

## Django Configuration

The R shared library is not reentrant and hence Rpy should not accessed from multiple threads. There are hints (e.g. [this patch](http://comments.gmane.org/gmane.comp.python.rpy/1760)) that suggest this may be handled by Rpy, but, the immediate response from a [question about this](http://sourceforge.net/mailarchive/message.php?msg_id=28814666) on the rpy list suggests otherwise:

> I don't think that rpy takes care of this (and I think that it tries to warn
> people not to try concurrency).
> rpy2 has a rudimentary system of locks to prevent bad things from happening
> if someone is foolish enough to try anyway.
>
> Python has a GIL, so would not go far anyway. ;-)
> Consider using separate processes, that's the way the Python folks have
> addressed the issue so far (package 'multiprocessing').

This should not be too much of a problem in a testing environment with very low load compared to the time it takes to process a request, but has implications for how one must configure a Django site in production. If using [mod_wsgi](http://code.google.com/p/modwsgi/), then, from my understanding, one should use daemon mode *whereby distinct processes can be dedicated to run a WSGI application*. I presume this means that each request is handled in a separate process (which is the recommended way of doing things with [Rserve](http://www.rforge.net/Rserve/)), but not being an expert on mod_wsgi, **this might need further investigation**. If I am incorrect, could someone please correct me. I'm not sure whether one can use mod_python at all (but have not investigated it).

Depending on how heavy the processing you are doing is, this has implications for how you might parallelise the work (in Python generally).

It is also worth noting that one should not assume anything about the state of R's global workspace between requests... though this should be obvious.

## Notes for Linux

gonavald and dzhibas note that on linux:
you can install django, R and Rpy2 with:

    sudo pip install django
    sudo apt-get install r-base-core
    sudo pip install rpy2

and to make the R shared library available:

    cd /usr/lib/
    sudo ln -s /usr/lib/R/lib/libR.so
