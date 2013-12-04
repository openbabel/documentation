gen3d
=====

To illustrate how some of the above methods might be used in practice, consider the **gen3d** operation. This operation (invoked using ``--gen3d`` at the commandline) generates 3D structures for 0D or 2D structures using the following series of steps, all of which have been described above:

1. Use the OBBuilder to create a 3D structure using rules and ring templates

2. Do 250 steps of a steepest descent geometry optimization with the MMFF94
   forcefield

3. Do 200 iterations of a Weighted Rotor conformational search (optimizing each
   conformer with 25 steps of a steepest descent)

4. Do 250 steps of a conjugate gradient geometry optimization

Taken together, all of these steps ensure that the generated structure is likely to be the global minimum energy conformer. However, for many applications where 100s if not 1000s of molecules need to be processed, gen3d is rather slow. A future version of Open Babel will provide options for slow/medium/fast 3D structure generation which will involve different compromises between speed and finding the global energy minimum.
