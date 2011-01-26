.. _version control:

Version Control
===============

Subversion_  (or SVN) is the name of the project used to maintain the Open Babel version control repository. There are many clients for Subversion, including command-line and GUI applications (for example, on Windows, TortoiseSVN_). For more links, see the Subversion website_. There's also a great book about using Subversion, which is available online_.

.. _Subversion: http://subversion.tigris.org/ 
.. _online: http://svnbook.red-bean.com/
.. _website: http://subversion.tigris.org/links.html
.. _TortoiseSVN: http://tortoisesvn.tigris.org/

Keeping up to date with the latest Open Babel code with Subversion
------------------------------------------------------------------

(1) Check out the latest development version::

      svn co https://openbabel.svn.sourceforge.net/svnroot/openbabel/openbabel/trunk 

This creates a directory called :file:`trunk`, which contains the latest source code from OpenBabel.

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
--------------------------

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
