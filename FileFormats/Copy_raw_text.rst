.. _Copy_raw_text:

Copy raw text (copy)
====================

**A utility format for exactly copying the text of a chemical file format**

This format allows you to filter molecules from multimolecule files
without the risk of losing any additional information they contain,
since no format conversion is carried out.

.. warning::

 Currently not working correctly for files with Windows line endings.

Example:

  Extract only structures that include at least one aromatic carbon
  (by matching the SMARTS pattern ``[c]``)::

   babel -s '[c]' database.sdf -ocopy new.sd

.. note::

 XML files may be missing non-object elements
 at the start or end and so may no longer be well formed.



.. note:: This is a write-only format.

