dmr_combine_multChrs4rank
=========================

This program is used to combine DMR/MRs from multiple chromosomes.

Required Parameters
-------------------
- ``inChrs`` or ``--in_chroms_number``: A string of chromosomes that need to be combined, separated by commas. For example: chr1,chr2,chr3.
- ``inFold`` or ``--in_file_folder``: The file folder containing MR data for each chromosome that is exported by dmr_analysis_block.

Optional Parameters
-------------------
- ``inSFold`` or ``--in_File_subFolder``: The subfolder of exported MR data in each chromosome based on dmr_analysis_block. Default is "plots" located under each chromosome folder.
- ``inMPer`` or ``--in_minimum_percentage_changes``: The minimum percentage of data points in an MR with a predefined methylation change greater than a cutoff. Default is 0.0001.
- ``inPC`` or ``--in_Pvalue_cutoff``: The P-value cutoff for the significance test. Default is 0.05.
- ``inIsSmd`` or ``--in_is_smoothed_data``: The type of data used for the results: raw = 0, interpolated = 1, or smoothed = 2. Default is 0.
- ``inAC`` or ``--in_accuracy_cutoff_range``: The range of clustering accuracy. Default includes all values from 0.0 to 1.0, specified as 0.0,1.1.
- ``inDMRst`` or ``--in_DMR_string_type``: A string used to represent predicted DMRs in the file. Default is "D" for predicted DMRs.
- ``inLRpb`` or ``--in_LogReg_proba``: A probability value used by logistic regression to select DMRs. Default is 0.8.
- ``inMT`` or ``--in_moderate_ttest``: The type of significance test to evaluate: 0 for standard T-test, 1 for moderate T-test, and 2 for KS-test. Default is 0.
- ``inLMH`` or ``--in_low_median_high_cutoff``: Use high, median, or low minimum percentage change for DMR ranking. Default is "high".
- ``inFEstr`` or ``--in_file_ending_string``: The file name ending string used to search for result files in the result folder (e.g., chrY/plots/). Default is "_all".
