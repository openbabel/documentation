.. _Wiswesser_Line_Notation:

Wiswesser Line Notation (wln)
=============================

**A chemical line notation developed by Wiswesser**


WLN was invented in 1949, by William J. Wiswesser, as one of the first attempts
to codify chemical structure as a line notation, enabling collation on punched
cards using automatic tabulating machines and early electronic computers. WLN
was a forerunner to the SMILES notation used in modern cheminformatics systems,
which attempted to simplify the complex rules used in WLN encoding (at the
expense of brevity) to come up with an algorithmic system more suitable for
implementation on computers, where historically WLN was typically encoded
by hand by trained registrars.

WLN encoding makes use of uppercase letters, digits, spaces and punctuation:

- E       Bromine atom
- F       Fluorine atom
- G       Chlorine atom
- H       Hydrogen atom
- I       Iodine atom
- Q       Hydroxyl group, -OH
- R       Benzene ring
- S       Sulfur atom
- U       Double bond
- UU      Triple bond
- V       Carbonyl, -C(=O)-
- C       Unbranched carbon multiply bonded to non-carbon atom
- K       Nitrogen atom bonded to more than three other atoms
- L       First symbol of a carbocyclic ring notation
- M       Imino or imido -NH-group
- N       Nitrogen atom, hydrogen free, bonded to fewer than 4 atoms
- O       Oxygen atom, hydrogen-free
- T       First symbol of a heterocyclic ring notation
- W       Non-linear dioxo group, as in -NO2 or -SO2-
- X       Carbon attached to four atoms other than hydrogen
- Y       Carbon attached to three atoms other then hydrogen
- Z       Amino and amido NH2 group
- <digit> Digits '1' to '9' denote unbranched alkyl chains
- &       Sidechain terminator or, after a space, a component separator

For a more complete description of the grammar see Smith's book [1], which more
accurately reflects the WLN commonly encountered than Wiswesser's book [2].
Additional WLN dialects include inorganic salts, and methyl contractions.

Here are some examples of WLN strings along with a corresponding SMILES string:

- WN3        [O-][N+](=O)CCC
- G1UU1G     ClC#CCl
- VH3        O=CCCC
- NCCN       N#CC#N
- ZYZUM      NC(=N)N
- QY         CC(C)O
- OV1 &-NA-  CC(=O)[O-].[Na+]
- RM1R       c1ccccc1NCc2ccccc2
- T56 BMJ B D - DT6N CNJ BMR BO1 DN1 & 2N1 & 1 EMV1U1   (osimertinib)
  Cn1cc(c2c1cccc2)c3ccnc(n3)Nc4cc(c(cc4OC)N(C)CCN(C)C)NC(=O)C=C

This reader was contributed by Roger Sayle (NextMove Software). The text of
this description was taken from his Bio-IT World poster [3]. Note that not
all of WLN is currently supported; however, about 76% of the WLN strings
found in PubChem can be interpreted.

1. Elbert G. Smith, "The Wiswesser Line-Formula Chemical Notation",
   McGraw-Hill Book Company publishers, 1968.
2. William J. Wiswesser, "A Line-Formula Chemical Notation", Thomas Crowell
   Company publishers, 1954.
3. Roger Sayle, Noel O'Boyle, Greg Landrum, Roman Affentranger. "Open
   sourcing a Wiswesser Line Notation (WLN) parser to facilitate electronic
   lab notebook (ELN) record transfer using the Pistoia Alliance's UDM
   (Unified Data Model) standard." BioIT World. Apr 2019.
   https://www.nextmovesoftware.com/posters/Sayle_WisswesserLineNotation_BioIT_201904.pdf


.. note:: This is a read-only format.

