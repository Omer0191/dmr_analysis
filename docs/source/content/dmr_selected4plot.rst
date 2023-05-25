dmr_selected4plot
=================

Plot figures or export methylation data for selected DMR/MRs.

Required
--------
- ``-inDMR IN_DMR_FILE``: A file generated after performing 'dmr_analysis_block' and 'dmr_combine_multChrs4rank,' which contains DMR information and logReg probability values for each MR, in addition to the main feature scores exported from dmr_analysis_block. This file is usually exported for each chromosome under the 'plots' folder in the output folder of dmr_analysis_block.
- ``-inData IN_DATA_FILE``: A file containing raw DNA methylation data of all MRs in a chromosome, exported after running 'dmr_analysis_block.' This file is stored in each chromosome's output folder. For example, a file named 'chrY_MR_data4maxBlockDistance_250_minBlockSize_5_data.txt.gz' is stored in the 'chrY' output folder after running 'dmr_analysis_block.'
- ``-inFolder IN_DATA_FOLDER``: Path of a file folder that contains all the files mentioned in ``-inDMR`` and ``-inData``. For example, 'out/chrY' is the path that stores DMR/MR raw data for the 'chrY' chromosome after running dmr_analysis_block and dmr_combine_multChrs4rank.

Optional Parameters
-------------------
- ``-inDMRFolder``: A subfolder for storing exported MR/DMRs in each chromosome after running dmr_analysis_block. The default is 'plots/' under ``--in_data_folder``.
- ``-inAcCut``: A range of clustering accuracy to consider in the program. The default is '0.0,1.0,' which means between 0.0 and 1.0.
- ``-inDmrSt``: A string used in ``--inDMR_file`` that represents the predicted DMR. The default is 'D,' representing predicted DMR.
- ``-inOtCod IN_OTHER_CONDITION``: A string type for selecting DMR from the whole data, such as logReg_proba, min_dmr,max_dmr, top_to_down, top_rank, down_rank, or None. The default is down_rank_10 (10%).
- ``-inDstart``: The position of the data start column in a file inputted from ``--in_data_file``. The default is 3 because the first three columns are chromosome positions (chrom, start_post, end_post), followed by data columns (data1, data2, ...).
- ``-inIsExt``: Whether to export data (1) or not (0) for selected DMR/MRs. The default is 0, indicating not exporting data.
- ``-dotOrUnderscore``: Use 0 for dot ('.') split column labels or 1 for underscore ('_') split column labels in the file specified by ``--in_data_file``. The default is 0 (dot split column labels).

- ``-inIsPlt`` or ``--is_plot``: Whether to plot the figure (1) or not (0) for selected DMR/MRs. The default is 0, indicating not plotting the figure.
- ``-inIsPas`` or ``--is_pause``: Whether to pause (1) or continue (0) in the loop. The default is 0, indicating continuing in the loop for all input DMR/MRs.
- ``-inLogNm`` or ``--in_Logger_number``: Logger number for recording screen displays. The default is 0.
- ``-inOutFd`` or ``--out_folder``: Path for the output file folder. The default is 'out/'.
- ``-inNdChk`` or ``--needs_check_mr``: String ID of selected DMR/MRs that will be checked/plotted/data exported, comma-separated. For example, 'mr10,mr111.' The default is not to check.
- ``-dpi`` or ``--figure_dpi``: Export figure resolution in DPI. The default dpi is 30.
- ``-format`` or ``--figure_format``: File format of the exported figure, such as jpg, svg, pdf, or png. The default is pdf.
- ``-wtStr`` or ``--wildType_fileString``: A file name of the wild-type condition file, which should start with specific characters. For example, if a file name starts with 'gcb_meht1_*' is a wild-type/control sample, then ``--wildType_fileString`` is 'gcb,' which is the default setting in the program.

