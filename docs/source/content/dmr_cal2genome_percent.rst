dmr_cal2genome_percent
======================

Calculate percentage of DMRs in predefined genomic regions (e.g., TSS, TES, Gene, 5Dist, et al)

Required:
---------
- ``-inOFolder IN_OUTFILE_FOLDER, --in_outFile_folder IN_OUTFILE_FOLDER``: Path of file folder that stores the exported files from ``dmr_map2genome``, for example, exported MR/DMRs intersected to predefined genomic regions from "dmr_map2genome".
- ``-inOFile IN_OUTFILE_NAME, --in_outFile_name IN_OUTFILE_NAME``: Output file name for storing the percentage of DMRs in predefined genomic regions, respectively.
- ``-inFileStr IN_FILENAME_STRING, --in_fileName_string IN_FILENAME_STRING``: Input file name string that will be searched by the program to obtain mapped MR/DMR information. For example, an output BED format file from "dmr_combine_multChrs4rank" is "24_chroms_high_miniPercentChange_gt_0.0001_Pcutoff_0.05_isSmooth_2_isModTest_0__all_dmrRanking_top_0.95_minLogReg_proba_0.7*", which is usually stored in folder --in_outFile_folder. In the new version, it becomes a file such as "5_chroms_all_mr_data_range_dmrRanking_*".

Optional, has default values:
-----------------------------
- ``-LsOrGt, --in_Ls_or_Gt_pval``: Use less (0) or greater (1) than Probability value cutoff to search for DMRs. The default is 1, which uses a greater than Probability value as the cutoff to select DMRs.
- ``-inLRpb, --in_LogReg_proba``: A probability value used by logistic Regression to select DMRs. The default is 0.8.
