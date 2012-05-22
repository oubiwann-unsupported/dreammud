DreamMUD Server
===============


Features
--------

TBD


Install
-------

You can install from PyPI, which will give you the latest released (hopefully
stable) version of the software::

    $ sudo pip install DreamMUD

If you like living on the edge, you can install from the github ``master``
branch::

    $ sudo pip install https://github.com/dreamhost/dreammud/zipball/master

Finally, you can just get the code itself::

    $ git clone https://github.com/dreamhost/dreammud.git


Dependencies
-------------

If you used ``pip`` to install DreamMUD, then you will have the necessary
libraries installed. If you will be running from source code, you'll need to do
the following::

    $ sudo pip install DreamSSH

Once the dependencies are installed, you'll need to generate the keys for use
by the server::

    $ twistd dreammud keygen


Running
-------

Once you have DreamMUD installed, interacting with the server is as easy as the
following::

    $ twistd dreammud

That will run in daemonized mode. If you'd like to run it in the foreground and
watch the log output to stdout, just do::

    $ twistd -n dreammud

To log into the shell, use this command::

    $ twistd dreammud shell

When you're ready to shut it down::

    $ twistd dreammud stop

For those who have a ``clone`` of the git repo, there are development
convenience make targets::

    $ make keygen
    $ make daemon
    $ make run
    $ make shell
    $ make stop


Using
-----

When you log into the Python shell::

    $ twistd dreammud shell

You are greeted with something that looks like this::

TBD

If you follow the hints given in the banner, you can get a listing of available
objects with the following command::

TBD

Configuring
-----------

TBD


Hacking
-------

TBD
