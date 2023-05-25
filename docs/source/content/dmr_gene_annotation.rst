dmr_gene_annotation
===================

Cleans reference file and creates genomic region files (TSS, geneBody, TES, 5dist, and intergenic) from the reference.

Required Arguments
------------------
- ``-r file`` or ``--referenceFile file``: Reference file.
- ``-g file`` or ``--genomeFile file``: Genome file, with one column containing chromosome names and another column containing the length of each chromosome.
- ``-hu y/m/r`` or ``--human y/m/r``: Is the sample from a human? Use ``yes/y`` for human, ``mouse/m`` for mouse, or ``rat/r`` for rat. If not, it must be from either the mouse (``m``) or rat (``r``) genome.
- ``-n y/n`` or ``--numericalChr y/n``: Will you operate with numerical chromosome names or not? Use ``yes/y`` if using numerical chromosome names or ``no/n`` if using alphanumeric names. The choice must match the chromosome naming convention in the ``genomeFile``. The default is ``no``.

Optional Arguments
------------------
- ``-rm`` or ``--removeMir``: Remove genes with names starting with 'Mir'? Use ``yes/y`` or ``no/n``. The default is ``yes``.
- ``-X``: The number of upstream base pairs (bp) for TSS, TES, and genes. The default is 1000.
- ``-Y``: The number of downstream base pairs (bp) for TSS, TES, and genes. The default is 1000.
- ``-M``: The number of base pairs (bp) from the gene start site for the 5dist region. The default is 10000.
- ``-N``: The number of base pairs (bp) from the gene start site for the 5dist region. The default is 1000000.
- ``-i`` or ``--intergenicBTGenes``: Are intergenic regions between gene body regions (``yes/y``) or between TSS and TES regions (``no/n``)? The default is ``yes``.
- ``-l`` or ``--minIntergenicLen``: The minimum intergenic region distance. The default is 2000.
- ``-xL`` or ``--maxIntergenicLen``: The maximum intergenic region distance. The default is 10000000.
- ``-rem`` or ``--removeShort``: Should regions be removed from TSS, TES, and 5dist regions if the gene body is removed due to its size being less than 0? Use ``yes/y`` or ``no/n``. The default is ``yes``.
- ``-F`` or ``--folderOut``: The name of the output folder. The default is "out".
