dmr_percent2plot
================

Plot the percentage of DMRs in predefined genomic regions or predicted chromatin segment regions.

Required
--------
- ``-inCFolder IN_COUNTFILE_FOLDER`` or ``--in_countFile_folder IN_COUNTFILE_FOLDER``: Input path of a file folder that contains a count table of DMRs in predefined genomic regions exported by dmr_cal2genome_percent.
- ``-inCFname IN_COUNTFILE_NAME`` or ``--in_countFile_name IN_COUNTFILE_NAME``: Input file name of the count table for DMR/MRs in predefined genomic regions, for example, an exported file from dmr_cal2chromSegment_percent or dmr_cal2genome_percent.

Optional
--------
- ``-LsOrGt`` or ``--in_Ls_or_Gt_pval``: Use less (0) or greater (1) than the probability value cutoff to search for DMRs. The default is 1, which uses a greater than probability value as the cutoff to select DMRs.
- ``-inLRpb`` or ``--in_LogReg_proba``: A probability value used by logistic Regression to select DMRs. The default is 0.8.

