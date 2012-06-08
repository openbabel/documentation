.. _FPS_text_fingerprint_format_(Dalke):

FPS text fingerprint format (Dalke) (fps)
=========================================
The FPS file format for fingerprints was developed by Andrew Dalke to
define and promote common file formats for storing and exchanging
cheminformatics fingerprint data sets, and to develop tools which
work with that format. For more information, see
http://chem-fingerprints.googlecode.com

Any molecule without a title is given its index in the file as title.

A list of available fingerprint types can be obtained by::

  obabel -L fingerprints



.. note:: This is a write-only format.

Write Options
~~~~~~~~~~~~~ 

-f <id>  *Fingerprint type*
-N <num>  *Fold to specified number of bits, 32, 64, 128, etc.*
-p  *Use full input path as source, not just filename*
-t <text>  *Use <text> as source in header*


