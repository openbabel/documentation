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

To build the docs yourself, you should install a recent version of Sphinx (works for me with 1.8.5):
 
(1) Sphinx has several dependencies so it is most easily installed using Python's package managers. I recommend that you create a virtualenv and install Sphinx within that::
      
      $ virtualenv myenv
      $ source myenv/bin/activate
      (myenv) $ pip install Sphinx

(2) You also need to install the doxylink extension::

      (myenv) $ pip install sphinxcontrib-doxylink

(3) To build the documentation, type ``make html`` or ``make latex``. 

(4) To correct errors in the generated HTML and LaTeX, type ``python FixHTML.py``.

Automatic generation
--------------------

Within a few seconds, updated docs will be available at http://readthedocs.org/projects/baoilleach/open-babel/. Note that these docs are missing the links to the C++ documentation and to Pybel.

The complete docs are automatically generated once an hour (on the hour) from the latest source, and are available at http://openbabel.org/docs/dev.
