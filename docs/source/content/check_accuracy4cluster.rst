check_accuracy4cluster
======================

Significant test of TF binding affinity changes between the foreground and the background calculations

Required Parameters
-------------------
- ``background_folder``: Folder containing the computed background model produced by ``background_affinity_changes.py``.
- ``foreground_folder``: Folder containing the computed delta-dba values for patient data produced by ``bayespi_bar.py``.

Optional Parameters
-------------------
- ``output_file``: Output file name. The default is "-" (hyphen).
- ``p_value``: P-value cutoff for the Wilcoxon test. The default value is 0.05.
- ``max_rank``: Maximum rank of PWM to consider in the patient results. The default value is 15.
- ``exact_test``: Use exact Wilcoxon rank-sum test from R. R needs to be installed. The default is False.
- ``pval_correction``: Whether to adjust P-values by Bonferroni correction. The default is False.
