dmr_cal2chromSegment_percent
============================

Calculate percentage of DMRs in chromatin segment (e.g., generated from ENCODE predictions of 6 human cell lines)

Required:
---------
- ``-inOFolder IN_OUTFILE_FOLDER, --in_outFile_folder IN_OUTFILE_FOLDER``: Input file folder for chromatin segment out file, for example, export files from "dmr_map2chromSegment".
- ``-inOFile IN_OUTFILE_NAME, --in_outFile_name IN_OUTFILE_NAME``: Output file name of percentage DMR that will be calculated in chromatin segment regions.
- ``-inFileStr IN_FILENAME_STRING, --in_fileName_string IN_FILENAME_STRING``: Input file name string that will be searched (e.g., 24_chroms_high_miniPercentChange_gt_0.0001_Pcutoff_0.05_isSmooth_2_isModTest_0__all_dmrRanking_top_0.95_minLogReg_proba_0.7*) under folder --in_outFile_folder.

Optional, has default values:
_____________________________
- ``-inLRpb , --in_LogReg_proba``: A probability value used by logistic Regression to select DMRs. The default is 0.8.
