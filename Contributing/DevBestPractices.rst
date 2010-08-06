Developing Open Babel
=====================

Due to its open nature of its development, Open Babel contains code contributed by a wide variety of developers (see :ref:`contributors`). This section describes some general guidelines and "best practices" for code developers.

Grabbing the Development Code
-----------------------------

The source code for Open Babel is maintained via the Subversion version control system. You can browse the latest source code at Open Babel's SourceForge_ site.

.. _SourceForge: http://www.sf.net/projects/openbabel

To download and update the source code itself, please see the instructions on using Subversion with Open Babel (:ref:`subversion`).

Monitoring Progress
-------------------

Developers should keep track of changes made by others. Like most open source projects, development occurs in many places by many contributors. Therefore it is important to keep up-to-date with your code repository and keep on top of changes made by others. A bug you just found in the latest release may have already been fixed by someone else.

    * `CIA Stats`_ on Open Babel (provides a webpage and RSS feed for every change)
    * OpenBabel-Updates_ mailing list (receives an e-mail message on every change) 

.. _CIA Stats: http://cia.navi.cx/stats/project/OpenBabel
.. _OpenBabel-Updates: http://lists.sourceforge.net/lists/listinfo/openbabel-updates

In general, if you find that a recent update by another developer has introduced bugs or broken the code, please bring it up with them ASAP. We have a policy of "if you break it, you fix it" to keep the source code repository always in a working state.

Many of the developers use the current development snapshots for their daily use. This is sometimes called `eating your dog food`_ and is part of the general testing procedures for Open Babel.

.. _eating your dog food: http://en.wikipedia.org/wiki/Eat_one%27s_own_dog_food

Documentation
-------------

As an open source project, code must be documented, both for other developers to use the API and for others to follow your code.

For more information, please see :ref:`documentation`.

Testing
-------

Testing is extremely important. New functions should have individual unit tests as older code is slowly added to the test suite. Because of the wide use of Open Babel, code is (and should be) thoroughly tested before release.

Releases may be imperfect and will likely contain bugs. However, increased testing improves code quality and makes life easier for everyone. For more information, see :ref:`testing`.

Code Formatting
---------------

It seems like a minor point, but the format of your code is important. As open source software, your code is read by many, many people.

Different contributions have often had different indentation styles. Simply making the code indentation consistent across an entire file makes the code easier to read.

Error Handling
--------------

The general philosophy of the Open Babel project is to attempt to gracefully recover from error conditions. Depending on the severity of the error, a message may or may not be sent to the user -- users can filter out developer debugging messages and minor errors, but should be notified of significant problems.

For more information, please see :ref:`handling_errors`.

Patches and Changesets
----------------------

We're human--it's much easier to understand exactly what a patch is doing if it's not trying to add 20 features or fix 20 bugs at once. (Hopefully there won't be a need to fix 20 bugs!) If you want to add several features or fix several bugs, break the patch up into one for each request. The faster someone can understand your patch, the faster it will go into the source. Everyone benefits from faster, quality development.

Similarly, it's sometimes necessary to revert the code to an older version because of bugs. Each set of changes should only touch as few files as are needed. This makes it easier for others to review your changes and undo them if necessarily. (Again, hopefully there's never a need, but this is certainly a "best practice" to make life easier for everyone.)

The ChangeLog
-------------

The ChangeLog file is used to maintain an abbreviated history of changes to the code by all users. Please add a ChangeLog entry to any patch and make sure to keep it up to date as you commit changes to the source code. The format_ should be mostly self-explanatory.

.. _format: http://www.gnu.org/software/guile/changelogs/guile-changelogs_3.html|format

In particular, please include a notation of any file you have changed. This makes it easy for others to track which changes may have added new functionality, fixed bugs, or inadvertently caused errors. 

