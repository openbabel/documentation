OBBuilder
=========

The :obapi:`OBBuilder` class is the part of Open Babel that can take a 2D or 0D structure and generate a 3D structure. The 3D structure is made very quickly using a combination of rules (e.g. sp3 atoms should have four bonds arranged in a tetrahedron) and ring templates (e.g. cyclohexane is shaped like a chair).

The 3D structures that come straight out of OBBuilder may be useful for some purposes but most people will want to "clean them up". This is because they may have clashes or have high energy structures due to some strain. The conformer search or geometry optimization methods described below are typically used after calling OBBuilder.

A more severe limitation of OBBuilder is that due to the limited number of ring templates (and any finite number of ring templates is limited) stereochemistry in rings is not necessarily preserved (a warning message will be issued whenever this is the case). While efforts are ongoing to improve this situation, if preserving stereochemistry is a priority then you will need to look elsewhere for this functionality.
