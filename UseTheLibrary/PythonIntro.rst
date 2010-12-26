Introduction
~~~~~~~~~~~~

The Python interface to OpenBabel is perhaps the most popular of the several languages that OpenBabel supports. We provide two Python modules that can be used to access the functionality of Open Babel toolkit:

1. The *openbabel* module:
   
     This contains the standard Python bindings automatically generated using SWIG from the C++ API. See :ref:`openbabel python module`.

2. The *Pybel* module:

      This is a light-weight wrapper around the classes and methods in the *openbabel*  module. Pybel provides more convenient and Pythonic ways to access the Open Babel toolkit. See :ref:`pybel module`.

You don't have to choose between them though - they can be used together.
