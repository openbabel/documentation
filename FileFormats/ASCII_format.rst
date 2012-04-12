.. _ASCII_format:

ASCII format (ascii)
====================

**2D depiction of a single molecule as ASCII text**


This format generates a 2D depiction of a molecule using only ASCII text
suitable for a command-line console, or a text file. For example::

  obabel -:c1ccccc1C(=O)Cl -oascii -xh 20

         __
      __/__\_
    _/__/    \__
  _/_/          \__
  |               |
  |             | |
  |             | |
  |             | |
  |             | |
  |___            _               Cl
    \_\__       _/ \_          __
       \_\_  __/     \__    __/
         \__/           \__/
                         | |
                         | |
                         | |
                         | |

                          O

If the image appears elongated or squat, the aspect ratio should be changed
from its default value of 1.5 using the ``-xa <ratio>`` option. To help
determine the correct value, use the ``-xs`` option to display a square.


.. note:: This is a write-only format.

Write Options
~~~~~~~~~~~~~ 

-w <characters>  *Image width in characters, default 79*
-h <characters>  *Image height in characters, default is width/aspect*
-a <ratio>  *Aspect ratio of character height:width, default is 1.5*
-s  *Display a square - this is useful for correcting the aspect ratio*
-t  *Write the output molecule index and the title*
-m  *Include a margin around the depiction*


