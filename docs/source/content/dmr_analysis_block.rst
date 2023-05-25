dmr_analysis_block
==================

Significant test of TF binding affinity changes between the foreground and the background calculations

Required Parameters
-------------------
- ``-in IN_FILE_FOLDER, --in_file_folder IN_FILE_FOLDER``: Input file folder for DNA methylation data such as WGBS. In this folder, all samples are provided in each chromosome folder with BED format where sample name is indicated by file name.
- ``-chr CHROMOSOME, --chromosome CHROMOSOME``: Select a chromosome for running dmr_analysis_block. For example, a chromosome (e.g., chrY) file folder under --in_file_folder that contains methylation data of samples in a chromosome (e.g., chrY).
- ``-gkey GROUP_KEY, --group_key GROUP_KEY``: Group key name, all bed files name contain this group_key will be combined together for dmr_analysis_block. In other words, only bed file name with this group_key will be selected in analysis. Usually, it is the same as the file folder (or chromosome name) in --chromosome.

Optional Parameters
-------------------
- ``-out , --out_file_folder``: Output file folder that stores all results computed by dmr_analysis_block. The default is "out/".
- ``-ncol , --need_column``: Select a column name from the bed file that will be used by dmr_analysis_block. The default is "Methylation".
- ``-wtStr , --wildType_fileString``: Use the first few character string of a file name to indicate it is a normal/wild type sample, or to label this file/sample as wild type/normal condition. The default is "gcb".
- ``-dstart , --data_start_position``: Data start position, a start column position for input dataframe after methylation levels of multiple samples are combined into one file. The default is 3 for chrY demo.
- ``-dend , --data_end_position``: Data end position, an end column position for input dataframe after methylation levels of multiple samples are combined into one file. The default is 15 for chrY demo.
- ``-mxL , --maximum_adjacency_length``: Maximum length of adjacency CpG sites allowed in a methylation region (MR). The default is 250.
- ``-minS , --minimum_block_size``: Minimum number of CpG sites requested in a block/methylation region (MR). The default is 5.
- ``-nDP , --number_of_data_points``: The number of data points (or rows from a dataframe) that will be considered in analysis. The default is 0, which means all data points (or the combined dataframe from all samples and CpG sites) will be used.
- ``-pC , --P_cutoff``: P cutoff value for T-test or other statistical significance test used in the analysis. The default is 0.05.
- ``-aC , --accuracy_cutoff``: Clustering accuracy cutoff value for binary classification (e.g., DMR or not DMR; tumor or normal samples) of 2D t-SNE map. The default is > 0.5.
- ``-mPer , --minimum_percentage_changes``: Minimum percentage of data points in a MR that passed a predefined filtering condition such as the methylation changes greater than a predefined cutoff value. The default is 0.0001 (0.1 percentage).
- ``-perC , --percentage_cutoff``: A comma-separated string list for predefined cutoff values of percentage of methylation changes between the two groups (e.g., 0.07,0.15,0.2) for low, median, high changes, respectively. The default parameter is 0.07,0.15,0.2.
- ``-lmhC , --low_median_high_cutoff``: Use low, median, or high percentage changes (from --percentage_cutoff) to predict high confidence DMRs. Use 0, 1, or 2 to represent low, median, or high percentage cutoff for the prediction. The default is 2 (high percentage changes in --percentage_cutoff).
- ``-numPro , --number_of_processes``: Number of parallel processes that will be used in calculation. The default is 1.
- ``-isSmd , --is_smoothed_data``: Use 0, 1, or 2 to represent raw data, interpolated data, or smoothed data used in predicting DMRs when comparing the two groups. The default is 2 (use smoothed data points to predict DMRs).
- ``-isMT , --is_moderate_ttest``: Use 0 for standard T-test, 1 for moderate T-test, and 2 for KS-test for evaluating the significance of differential methylation between the two groups across all CpG sites in a MR. The default is 0 (uses a T-test).
- ``-isExt , --is_export_data``: Use 0 to not export data or 1 to export data during the analysis. Both raw and smoothed methylation levels of all DMRs will be exported. The default is 0.
- ``-dotOrUnderscore , --column_splitBy_dotOrUnderscore``: Use 0 to split column labels using a dot (.) or 1 to split column labels using an underscore (_). The default is 0 (using a dot to split column labels).
