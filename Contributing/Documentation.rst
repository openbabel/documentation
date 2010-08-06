.. _documentation:

Documentation
=============

Documenting Open Babel is an important and ongoing task. This includes clear documentation on the interfaces of particular classes and methods (that is, the API_ documentation) but also tutorials and examples of using the Open Babel library to accomplish clear tasks.

.. _API: http://openbabel.org/api

Beyond the documentation described above, as an open-source project involving many, many contributors, the internal code should be clearly commented and easy to read (in English, preferably, since this is the common language of developers on the project).

Adding New Code
---------------

The golden rule is **write the documentation, then code to the specs**.

You should never, ever start writing code unless you've specified, clearly and exactly, what your code will do. This makes life easier for you (i.e., you know exactly what the code should do), and for others reading your code.

This mantra also facilitates writing tests (see :ref:`testing`).

Modifying Old Code
------------------

When modifying old code, please take a little time to improve the documentation of the function.

Even an "obvious" function must be documented, if for no other reason than to say, "This function does what you think, and has no side effects."

Take :obapi:`SetAtomicNum()` - should be "obvious", right? Wrong.

    * Does it affect the charge?
    * The spin multiplicity?
    * The implicit valence?
    * The hybridization?
    * What happens if I do SetHybridization(3) and then SetAtomicNum(1)?
    * Does the molecule have to be in the modify state?
    * If the molecule is not in the modify state, is it put into the modify state by SetAtomicNum()?
    * Does SetAtomicNum() cause a recomputation of aromaticity? 

ChangeLog entries
-----------------

A standard ChangeLog file is used to track changes to files by different users over time. Whenever a change is made to a file, please add a ChangeLog entry -- the format should be self-explanatory from other entries. 

User documentation
------------------

The documentation you are reading right now is automatically generated from text files in a simple markup language (*reStructuredText*) using the Sphinx_ documenatation system. If you notice any errors or feel there are any missing sections, please let us know at openbabel-devel_.

.. _Sphinx: http://sphinx.pocoo.org/
.. _openbabel-devel: https://lists.sourceforge.net/lists/listinfo/openbabel-devel
