Write software using the Open Babel library
===========================================

Behind the :command:`obabel` command line program lies a complete cheminformatics toolkit, the Open Babel library. Using this library, you can write your own custom scripts and software for yourself or others.

.. note::

  Any software that uses the Open Babel library must abide by terms of the `GNU Public License version 2`_. This includes all of the supporting language bindings (for example, Python scripts) as well as C++ programs. To summarise, if you are considering distributing your software to other people, you must make your source code available to them on request.

Open Babel is a C++ library and can easily be used from C++. In addition it can be accessed from Python, Perl, Ruby, CSharp and Java. These are referred to as language bindings (the Python bindings, etc.) and they were automatically generated from the C++ library using SWIG_. For Python we also provide a module (Pybel) that makes it easier to access features of the bindings.

.. _SWIG: http://swig.org
.. _GNU Public License version 2: http://www.gnu.org/licenses/gpl-2.0.html

.. toctree::
   :maxdepth: 2

   CppAPI.rst
   CppExamples.rst
   Python.rst
   Java.rst
   Perl.rst
   CSharp.rst
   Ruby.rst
   migration.rst
