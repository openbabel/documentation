The Open Babel API
==================

The API (Application Programming Interface) is the set of classes, methods and variables that a programming library provides to the user. The Open Babel API is implemented in C++, but the same set of classes, methods and variables are accessed through the various language bindings.

The API documentation is automatically generated from the source code using the Doxygen tool. The following links point to the various versions of the documentation:

* API for the `current release`_
* API for the `development version`_ (updated nightly, with `error report`_ showing errors in documentation)
* API for specific versions: `2.0.2`_, `2.1.0`_, `2.2.0`_

.. _current release: http://openbabel.org/api/
.. _development version: http://openbabel.org/dev-api/
.. _2.2.0: http://openbabel.org/api/2.2.0/
.. _2.1.0: http://openbabel.org/api/2.1.0/
.. _2.0.2: http://openbabel.org/api/2.0.2/
.. _error report: http://openbabel.org/dev-api/docbuild.out

The Open Babel toolkit uses a version numbering that indicates how the API has changed over time:

* Bug fix releases (e.g., 2.0.\ **0**, vs. 2.0.\ **1**) do not change API at all.
* Minor versions (e.g., 2.\ **0** vs. 2.\ **1**) will add function calls, but will be otherwise backwards-compatible.
* Major versions (e.g. **2** vs **3**) are not backwards-compatible, and have changes in the API.

Overall, our goal is for the Open Babel API to remain stable over as long a period as possible. This means that users can be confident that their code will continue to work despite the release of new versions with additional features, file formats and bug fixes. For example, at the time of writing we have been on the version 2 series for almost five years (since November 2005). In other words, a program written using Open Babel almost five years ago still works with the latest release.
