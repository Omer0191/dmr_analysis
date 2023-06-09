dmr_exportData
==============

Plot figure or export data for DMRs/MRs in specific regions, such as DMRs overlapping mutation blocks or enhancer regions, etc.

Required Arguments
------------------
- ``in_MRfolder`` or ``--input_mr_data_folder``: Input MR data folder, which is the output file folder of dmr_analysis_block.
- ``out_folder`` or ``--output_file_folder``: Output file folder for exported MR/DMR data.
- ``in_format`` or ``--input_file_format``: Input file format: 0 for a BED format file where DMR/MR IDs are listed in the fourth column (e.g., chr18:mr0:mix:U), 1 for an exported file with 8 columns generated by dds_analysis "check_block_gene_inTAD" where all DMRs and mutation blocks are assigned to a putative target gene, and DMR/MR IDs are under the column "new_mr_sites".
- ``in_file`` or ``--input_file``: A file containing DMR/MR IDs that will be used to extract the raw and smoothed methylation levels of DMRs/MRs listed in either a BED format file or an exported file from "dds_analysis check_block_gene_inTAD".

Optional Arguments
------------------
- ``processes`` or ``--number_of_processes``: Number of parallel processes to be used for data extraction. Default is 5.
- ``columnNumber`` or ``--input_file_bed_column``: If the input file is a BED format file, this parameter specifies the column number of DMR/MR IDs. The default is 3, which represents the fourth column (since the index starts from 0).
- ``columnName`` or ``--input_file_dds_column_name``: If the input file is generated by "dds_analysis check_block_gene_inTAD", this parameter specifies the column name of DMR/MR IDs. The default is "new_mr_sites".
- ``wtStr`` or ``--wildType_fileString``: The file name pattern of the wild type/control sample files. For example, if a wild type/control file name starts with "gcb_meht1_*", the value of this parameter should be "gcb" (which is the default setting in the program).
- ``dotOrUnderscore`` or ``--column_splitBy_dotOrUnderscore``: Use 0 for splitting column labels by dot (.), or 1 for splitting by underscore (_) in the file specified by ``in_data_file``. Default is 0 (dot split column labels).
