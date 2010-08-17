Lazy Evaluation
===============

BeginModify() and EndModify()
-----------------------------

The :obapi:`OBMol::BeginModify() <OpenBabel::OBMol::BeginModify>` and :obapi:`OBMol::EndModify() <OpenBabel::OBMol::EndModify>` calls are part of Open Babel's lazy evaluation mechanism.

In some cases, code may desire to make a large number of changes to an OBMol object at once. Ideally, this should all happen without triggering unintended perception routines. Therefore, the ``BeginModify()`` call marks the beginning of such code, and ``EndModify()`` triggers any needed updates of lazy evaluation methods.

.. highlight:: c++

For example::

    mol.BeginModify();
    double x,y,z;
    OBAtom *atom;
    vector<string> vs;

    for (i = 1; i <= natoms; i ++)
    {
        if (!ifs.getline(buffer,BUFF_SIZE))
            return(false);
        tokenize(vs,buffer);
        if (vs.size() != 4)
            return(false);

        atom = mol.NewAtom();
        x = atof((char*)vs[1].c_str());
        y = atof((char*)vs[2].c_str());
        z = atof((char*)vs[3].c_str());

        atom->SetVector(x,y,z); //set coordinates
        atom->SetAtomicNum(atoi(vs[0].c_str())); // set atomic number
    }
    mol.ConnectTheDots();
    mol.PerceiveBondOrders();
    mol.EndModify();

This code reads in a list of atoms with XYZ coordinates and the atomic number in the first column (``vs[0]``). Since hundreds or thousands of atoms could be added to a molecule, followed by creating bonds, the code is enclosed in a ``BeginModify()``/``EndModify()`` pair. 

