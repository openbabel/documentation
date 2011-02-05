Developing Open Babel
=====================

Due to its open nature of its development, Open Babel contains code contributed by a wide variety of developers (see :ref:`Thanks`). This section describes some general guidelines and "best practices" for code developers.

.. _version control:

Developer Resources
-------------------

For new and existing developers here are some useful resources:

- SourceForge `project page <http://www.sf.net/projects/openbabel>`_
- Development version `API documentation <http://openbabel.org/dev-api>`_ and `documentation bugs <http://openbabel.org/dev-api/docbuild.out>`_
- Nightly build and test `dashboard <http://my.cdash.org/index.php?project=Open%20Babel>`_
- RSS feed for SVN commits at `CIA.vc <http://cia.vc/stats/project/OpenBabel>`_

Grabbing the Development Code
-----------------------------

To download and update the latest version of the Open Babel source code, you need Subversion. Subversion_  (or SVN) is the name of the project used to maintain the Open Babel version control repository. There are many clients for Subversion, including command-line and GUI applications (for example, on Windows, TortoiseSVN_). For more links, see the Subversion website_. There's also a great book about using Subversion, which is available online_.

.. _Subversion: http://subversion.tigris.org/ 
.. _online: http://svnbook.red-bean.com/
.. _website: http://subversion.tigris.org/links.html
.. _TortoiseSVN: http://tortoisesvn.tigris.org/

Keeping up to date with the latest Open Babel code with Subversion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(1) Check out the latest development version::

      svn co https://openbabel.svn.sourceforge.net/svnroot/openbabel/openbabel/trunk 

    This creates a directory called :file:`trunk`, which contains the latest source code from Open Babel.

(2) Configure and compile this using CMake, as described on the CMake page.

(3) After some time passes, and you want the latest bug fixes or new features, you may want to update your source code. To do this, go into the :file:`trunk` directory you created above, and type::

      svn update

(4) Do step (2) again.

(5) If, after updating, the compilation fails please report it to the Open Babel mailing list. In the meanwhile, if you want to go back to a particular revision (that is, if you don't want to use the latest one), just use ``svn info`` to find the number of the current revision, and update to an earlier revision either by date or by revision number::

      $ svn info
      ...
      Revision: 1740
      ...
      $ svn update -r 1735
      (or)
      $ svn update -r {2007-01-01}


Useful Subversion Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table suggests Subversion commands useful for Open Babel contributors. More documentation can be found in the Official SVN Manual. In the following examples, *repo* should be replaced by the full URL to the Open Babel subversion repository (https://openbabel.svn.sourceforge.net/svnroot/openbabel/openbabel).

=================================   ============
Subversion Command                  What it does
=================================   ============
``svn co repo/trunk``               Check out the latest development version of Open Babel
``svn update``                      Update the current directory and subdirectories with any new changes
``svn add filename``                Add the file :file:`filename` to the repository
``svn remove filename``             Remove the file :file:`filename` (before a commit)
``svn mv filename newname``         Move/rename the file :file:`filename` to :file:`newname`
``svn commit``                      Commit the changes to the central repository
``svn diff``                        Return a diff set of differences between the working copy and the central repository
``svn switch repo/branches/foo``    Switch the current working copy to a branch named foo
``svn copy repo/branches/foo``      Create a branch named foo with the current working copy 
=================================   ============


Monitoring Progress
-------------------

Developers should keep track of changes made by others. Like most open source projects, development occurs in many places by many contributors. Therefore it is important to keep up-to-date with your code repository and keep on top of changes made by others. A bug you just found in the latest release may have already been fixed by someone else.

    * `CIA Stats`_ on Open Babel (provides a webpage and RSS feed for every change)
    * OpenBabel-Updates_ mailing list (receives an e-mail message on every change) 

.. _CIA Stats: http://cia.vc/stats/project/openbabel
.. _OpenBabel-Updates: http://lists.sourceforge.net/lists/listinfo/openbabel-updates

In general, if you find that a recent update by another developer has introduced bugs or broken the code, please bring it up with them ASAP. We have a policy of "if you break it, you fix it" to keep the source code repository always in a working state.

Error Handling
--------------

The general philosophy of the Open Babel project is to attempt to gracefully recover from error conditions. Depending on the severity of the error, a message may or may not be sent to the user -- users can filter out developer debugging messages and minor errors, but should be notified of significant problems.

For more information, please see :ref:`error handling`.

Patches and Changesets
----------------------

We're human--it's much easier to understand exactly what a patch is doing if it's not trying to add 20 features or fix 20 bugs at once. (Hopefully there won't be a need to fix 20 bugs!) If you want to add several features or fix several bugs, break the patch up into one for each request. The faster someone can understand your patch, the faster it will go into the source. Everyone benefits from faster, quality development.

Similarly, it's sometimes necessary to revert the code to an older version because of bugs. Each set of changes should only touch as few files as are needed. This makes it easier for others to review your changes and undo them if necessarily. (Again, hopefully there's never a need, but this is certainly a "best practice" to make life easier for everyone.)
