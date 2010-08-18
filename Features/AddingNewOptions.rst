Adding new operations and options
=================================

The babel command line has the form::

  babel inputfile [outputfile] [options]

There are several types of options:

* Options that control the conversion process:
  For example ``-i``, ``-o`` and ``-m``
* Options specific to particular input or output formats
  These are specified with the ``-a`` and ``-x`` prefixes
* General options. These usually operate on a molecule after it has been read by the input format and before it has been written by the output format.

The ones of interest here are the general options. These can be single letter options like ``-c`` (which centers coordinates), or multi-character options like ``--separate`` (which makes separate molecules from disconnected fragments). The ones mentioned are hardwired into the code, but it is possible to define new options which work in a similar way. This is done using the :obapi:`OBOp` class.

The OBOp class
--------------

The name :obapi:`OBOp` is intended to imply an operation as well as an option. This is a plugin class, which means that new ops are easily added without a need to alter any existing code.

The ops that are installed can be found using::

  babel -L ops

or in the plugins menu item in the GUI. An example is the ``--gen3D`` option, which adds 3D coordinates to a molecule:

.. code-block:: c++
   :linenos:

        class OpGen3D : public OBOp
        {
        public:
          OpGen3D(const char* ID) : OBOp(ID, false){};                  
          const char* Description(){ return "Generate 3D coordinates"; }

          virtual bool WorksWith(OBBase* pOb)const{ return dynamic_cast<OBMol*>(pOb)!=NULL; }
          virtual bool Do(OBBase* pOb, OpMap* pmap, const char* OptionText);
        };

        OpGen3D theOpGen3D("gen3D");

        bool OpGen3D::Do(OBBase* pOb, OpMap* pmap, const char* OptionText)
        {
          OBMol* pmol = dynamic_cast<OBMol*>(pOb);
          if(!pmol)
            return false;

          OBBuilder builder;
          builder.Build(*pmol);
          pmol->SetDimension(3);

          return true;
        }

The real work is done in the *Do* function, but there is a bit of boilerplate code that is necessary.

Line **4**: The constructor calls the base class constructor, which registers the class with the system. There could be additional parameters on the constructor if necessary, provided the base constructor is called in this way. (The ``false`` parameter value is to do with setting a default instance which is not relevant here.)

Line **5**: It is necessary to provide a description. The first line is used as a caption for the GUI checkbox. Subsequent lines are shown when listed with the verbose option.

Line **7**: *WorksWith()* identifies the type of object. Usually this is a molecule (*OBMol*) and the line is used as shown. The function is used by the GUI to display the option only when it is relevant.

  The *OBOp* base class doesn't know about *OBMol* or *OBConversion* and so it can be used with any kind of object derived from *OBBase* (essentially anything). Although this means that the dependencies between one bit of the program and another are reduced, it does lead to some compromises, such as having to code *WorksWith()* explicitly rather than as a base class default.

Line **11**: This is a global instance which defines the Id of the class. This is the option name used on the command line, preceded by ``--``.

Line **13**: The *Do()* function carries out the operation on the target object. It should normally return ``true``. Returning ``false`` prevents the molecule being sent to the output format. Although this means that it is possible to use an *OBOp* class as a filter, it is better to do this using the ``--filter`` option.

Any other general options specified on the command line (or the GUI) can be accessed by calling *find* on the parameter *pmap*. For example, to determine whether the ``-c`` option was also specified::

  OpMap::const_iterator iter = pmap->find("c");
  if(iter!=pmap->end())
    do something; 



