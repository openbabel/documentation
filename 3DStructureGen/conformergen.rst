Conformer generation
====================

In contrast to conformer searching, the goal of conformer generation is not simply to find a low energy conformation but to generate several different conformations. Such conformations may be required by another piece of software such as some protein-ligand docking and pharmacophore programs. They may also be useful if considering writing some sort of shape comparison method.

Open Babel has two distinct conformer generating codes:

1. Confab: A systematic conformer generator that generates all diverse
   low-energy conformers.

2. Genetic Algorithm: This is a stochastic conformer generator
   that uses a generatic algorithm (GA) to explore conformational space.

Since Confab is discussed separately, here we focus on the GA method. A genetic algorithm is a general computational method to find a globally optimum solution to some multiparameter problem. It involves a population of conformers which after a series of generations, iteratively arrive at an optimal solution in terms of either RMSD diversity or energy.

Information about using this method is available at the command-line using: ``obabel -L conformer``. Although labelled as "Conformer Searching", if you choose the genetic algorithm method (which is the default) then you can save the conformers in the final generation using ``--writeconformers``. For example, the following line creates 30 conformers optimized for RMSD diversity::

  obabel startingConformer.mol -O ga_conformers.sdf --conformer --nconf 30
         --score rmsd --writeconformers

In this case ``--score rmsd`` was not strictly necessary as RMSD diversity was the default in any case.
