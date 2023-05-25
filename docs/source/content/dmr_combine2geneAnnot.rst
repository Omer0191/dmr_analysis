dmr_combine2geneAnnot
=====================

Combine results of both genome and chromSegment to a single gene annotation file for DMRs.

Required Parameters
-------------------
- ``in_group1_str``: Group1 column label.
- ``in_group2_str``: Group2 column label.
- ``in_folder``: Input file folder that contains exported differential expression gene files from dmr_map2genome and dmr_map2chromSegment.
- ``in_file``: Input file name of the exported differential expression gene file.

Optional Parameters
-------------------
- ``min_median_RPKM``: Minimum median of RPKM value in each group. Default is 1.0.
- ``rr_cutoff``: Cutoff value for rratios to filter differential expression genes between two groups. Default is 0.18. Values of 0.14, 0.18, 0.22, 0.4, 0.67 represent 1.15, 1.2, 1.25, 1.5, 2.0 fold changes, respectively.
- ``sort_by_column_str``: Column name of the dataframe column that will be sorted after filtering. Default is "differential_expressoin_T_test_p_value".
- ``is_median``: Use mean or median of group values to calculate fold changes between groups. Default is False, which uses the mean value of the group.
