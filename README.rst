Open Babel user documentation
=============================

The Open Babel user documentation is generated from the text files in this project.

The source files have extension ``.rst``, indicating reStructuredText, a simple markup language widely used in the Python community and becoming more generally popular due to Sphinx, the documentation system that we are using here.

Editing the docs
----------------

Before editing the docs, you need to create a Github account and send me (baoilleach) the account name. Then I will add you to the list of 'collaborators'.

Github provides previews of reST documentation, which makes it easy to edit the docs directly on the github website. Alternatively, you can check out the repository and edit it locally. Note that Windows users should set ``autocrlf=true`` as described in the Github tutorials.

Building the docs
-----------------

To build the docs yourself, you need to have Sphinx 1.0 installed:

(1) Sphinx has several dependencies so it is most easily installed using Python's package managers. Download `distribute <http://pypi.python.org/pypi/distribute#downloads>`_, and once unpacked run the following commands::

  python distribute_setup.py install # (as root)
  easy_install pip # (as root) on Windows, use C:\Python26\Scripts\easy_install
  pip install sphinx # (as root)

(2) You also need to install the doxylink extension::

  pip install sphinxcontrib-doxylink # (as root)

(3) To build the documentation, type ``make html`` or ``make latex``. 

(4) To correct errors in the generated HTML and LaTeX, type ``python FixHTML.py``.

Automatic generation
--------------------

The docs are automatically generated once an hour (on the hour) from the latest source. You can find them at http:://openbabel.org/docs/dev.
