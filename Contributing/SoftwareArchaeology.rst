.. _software-archaeology:

Software Archaeology
====================

In any large software project, some parts of the code are revised and kept up-to-date more than others.

Conversely, some parts of the code begin to fall behind -- the code may be poorly tested, poorly documented, and not always up to best practices.

With that in mind, the following sections describe the important task of software archeology -- diving in to older parts of code and bringing them up to date. Whenever editing a file, please keep these in mind.

Documentation and Code Readability
----------------------------------

* Add clear documentation for every public function (see :ref:`documentation`).
* Add clear comments on the internal operation of functions -- so anyone can read through the code quickly.
   * If you're not sure what a function does, e-mail the openbabel-devel_ list and it can be worked out. 
* Mark functions which should be publicly visible and functions which are only useful internally. Many methods are not particularly useful except inside the library itself.
* Improve code indentation -- different contributions have often had different indentation styles. Simply making the code indentation consistent across an entire file makes the code easier to read.
   * The current accepted scheme for Open Babel is a default indent of two spaces, and use of spaces instead of tabs.
   * For tips on changing your editor to use this indentation style, please e-mail the openbabel-devel_ list. 
* Delete code which is commented out. The SVN version control system maintains history, so if we need it later, we can go back and get that code. Dead code like this simply makes it harder to read the important code!
* Marking areas of code which use :obapi:`OBAtom::GetIdx()` or other accesses to atom indexes, which may break when atom indexing changes. 

Code Maintenance
----------------

* Minimize ``#if``/``#endif`` conditional compilation. Some is required for portability, but these should be minimized where possible. If there seems to be some magic #define which accesses parts of the file, it's probably dead code. As above, dead code makes it harder to maintain and read everything else.
* Removing calls to cout, cerr, STDOUT, perror etc. These should use the global error reporting code.
* Minimize warnings from compilers (e.g., GCC flags ``-Wextra -Wall``). Sometimes these are innocuous, but it's usually better to fix the problems before they become bugs.
* Use static code analysis tools to find potential bugs in the code and remove them.
* Insure proper use of atom and bond iterators, e.g., ``FOR_ATOMS_OF_MOL`` rather than atom or bond index access, which will break if indexing changes. 

Patches and contributions towards any of these tasks will be greatly appreciated. 

.. _openbabel-devel: https://lists.sourceforge.net/lists/listinfo/openbabel-devel
