.. _POV-Ray_input_format:

POV-Ray input format (pov)
==========================

**Generate an input file for the open source POV-Ray ray tracer.**

Write Options
~~~~~~~~~~~~~ 

-c  *Add a black and white checkerboard*
-f  *Add a mirror sphere*
-m <model-type>  *BAS (ball-and-stick), SPF (space-fill) or CST (capped sticks)*

    The default option is ball-and-stick. To choose space-fill, you would use the following command line::

      obabel aspirin.mol -O aspirin.pov -xm SPF

-s  *Add a sky (with clouds)*
-t  *Use transparent textures*
