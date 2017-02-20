.. _contributing:

Contributor's guide
===================

This page helps you make contributions to the pgctl project.

For a quick primer on using github, see
https://guides.github.com/activities/contributing-to-open-source/

Developer Environment
---------------------
To put yourself into our dev environment, run ``source .activate.sh``.


Documentation
-------------
If you need to make changes to the documentation, they live under docs/source.
For a quick primer on the rst format, see
http://docutils.sourceforge.net/docs/user/rst/quickref.html

If you want to see good examples of other projects' documentation, see:

   * [the Requests
     docs](https://github.com/kennethreitz/requests/tree/master/docs)
   * [the virtualenv docs](https://github.com/pypa/virtualenv/tree/master/docs)

To get a look at your changes, run `make docs` from the root of the project.
This will spin up a http server on port 8088 serving your editted documentation.


Run tests
---------

    * make test   ## (should Just Work)

Run a particular test
---------------------

    * py.test tests/main_test.py::test_stop

Coverage reports should show all project files as well as test files.


.. vim:textwidth=79:shiftwidth=3
