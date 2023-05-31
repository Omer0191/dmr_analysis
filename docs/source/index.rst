.. dmr_analysis documentation master file, created by
   sphinx-quickstart on Thu May 25 11:12:28 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: https://user-images.githubusercontent.com/79196757/180248926-efd6e216-0683-4549-99f0-e6783224a2c7.png
   :align: center

.. image:: https://user-images.githubusercontent.com/79196757/180251608-da859f67-aa58-49e8-bea8-a0258be93635.png
   :align: center

.. image:: https://user-images.githubusercontent.com/79196757/180251606-8e257ad0-86d5-4cb7-b549-ed5e5c0aa9eb.jpg
   :align: center


============================================
Differential Methylated Region Analysis Tool
============================================

dmr_analysis Documentation
--------------------------

dmr_analysis is a software tool for differentially Methylated Regions analysis to rank significant DMRs.


Contents:
---------
.. toctree::
   :maxdepth: 1

   content/installation
   content/dmr_analysis_block
   content/dmr_combine_multChrs4rank
   content/dmr_selected4plot
   content/dmr_map2genome
   content/dmr_map2chromSegment
   content/dmr_cal2genome_percent
   content/dmr_cal2chromSegment_percent
   content/dmr_percent2plot
   content/dmr_combine2geneAnnot
   content/dmr_exportData
   content/dmr_gene_annotation
   content/check_accuracy4cluster
   content/demo1
   content/demo2
   content/demo3


Contents of the package:
************************

The package folder will contain the following:

- ``final_demo`` : Contains function scripts.
- ``dmr_analysis`` : Contains python source code of the pipeline.
- ``readme.txt`` : Instructions about the usage of the package.
- ``requirements.txt`` : List of requirements. Can be used for automatic installation from miniconda or pip.
- ``setup.py``: Setup file for the package.
- ``final_demo_data``: Contains data in and out for the secondary functions.

Pipeline Tasks:
***************

The pipeline consists of the following tasks. To run a task, type ``dmr_analysis task args``. To see what are the options for each task of the pipeline, please run: ``dmr_analysis -h``

- ``dmr_analysis_block`` : Predict Differentially Methylated Region (DMR) from genome-wide methylation regions such as by using WGBS or other similar techniques.
- ``dmr_combine_multChrs4rank`` : Combine predicted DMRs/MRs from multiple chromosomes then rank the DMRs by using logistic regression model.
- ``dmr_selected4plot`` : Plot figure and export raw/smoothed methylation data for selected DMR or MR.
- ``dmr_map2genome`` : Map all DMR/MRs to reference genome.
- ``dmr_map2chromSegment`` : Map all DMR/MRs to chromatin segments generated from 6 human cell lines.
- ``dmr_cal2genome_percent`` : Calculate the percentage of DMRs intersected with predefined genomic regions such as TSS, TES, 5dist et al.
- ``dmr_cal2chromSegment_percent`` : Calculate the percentage of DMRs intersected with chromatin segments generated from 6 human cells.
- ``dmr_percent2plot`` : Plot the percentage of DMRs in predefined genomic or chromatin segment regions.
- ``dmr_combine2geneAnnot`` : Combine annotations from both predefined genomic regions and chromatin segments (This function is slow and requests both genome and chromatin segment results available).
- ``dmr_exportData``: Plot and export data for DMRs/MRs located in specific regions (e.g., DMRs/MRs intersected with mutation block or enhancer regions).
- ``dmr_gene_annotation``: Clean the reference file and create genomic region files (TSS, geneBody, TES, 5dist, and intergenic) from the reference. This module is reimplemented here from hmst-seq-analyzer tool https://hmst-seq.github.io/hmst/
