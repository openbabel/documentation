.. _documentation:

Documentation
=============

Documenting Open Babel is an important and ongoing task. As an open source project, code must be documented, both for other developers to use the API and for others to follow your code. This includes clear documentation on the interfaces of particular classes and methods (that is, the API_ documentation) but also tutorials and examples of using the Open Babel library to accomplish clear tasks.

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

Take :obapi:`OBAtom::SetAtomicNum() <OpenBabel::OBAtom::SetAtomicNum>` - should be "obvious", right? Wrong.

    * Does it affect the charge?
    * The spin multiplicity?
    * The implicit valence?
    * The hybridization?
    * What happens if I do SetHybridization(3) and then SetAtomicNum(1)?
    * Does the molecule have to be in the modify state?
    * If the molecule is not in the modify state, is it put into the modify state by SetAtomicNum()?
    * Does SetAtomicNum() cause a recomputation of aromaticity? 

User documentation and tutorials
--------------------------------

There's no point spending time adding new features to Open Babel unless you describe how to use them and give examples. The best place to do this is in the user documentation...which you're reading right now.

This documentation is automatically generated from text files in a simple markup language (*reStructuredText*) using the Sphinx_ documentation system. This allows us to generate web pages, PDF files, and even ePub eBooks all from the same source (which is currently maintained at BitBucket_).

If you notice any errors or feel like adding a section, please let us know at openbabel-devel_.

.. _Sphinx: http://sphinx.pocoo.org/
.. _openbabel-devel: https://lists.sourceforge.net/lists/listinfo/openbabel-devel
.. _BitBucket: http://bitbucket.org/baoilleach/openbabel-user-docs
