.. _General_XML_format:

General XML format (xml)
========================

**Calls a particular XML format depending on the XML namespace.**


This is a general XML "format" which reads a generic XML file and infers
its format from the namespace as given in a xmlns attribute on an element.
If a namespace is recognised as associated with one of the XML formats in
Open Babel, and the type of the object (e.g. a molecule) is appropriate to
the output format then this is used to input a single object. If no namespace
declaration is found the default format (currently CML) is used.

The process is repeated for any subsequent input so that it is possible to
input objects written in several different schemas from the same document.
The file :file:`CMLandPubChem.xml` illustrates this and contains molecules in
both CML and PubChem formats.

This implementation uses libxml2.



.. note:: This is a read-only format.

Read Options
~~~~~~~~~~~~ 

-n  *Read objects of first namespace only*


