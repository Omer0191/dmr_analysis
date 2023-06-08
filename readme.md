# dmr_analysis

DMR-Analysis: A Differentially Methylated Region Analysis Tool


usage:  dmr_analysis task args

## Tasks available for using:
<ul>
  <li>
    <code>dmr_analysis_block</code>
    - Predict Differentially Methylated Region (DMR) from genome-wide methylation regions such as by using WGBS or other similar techniques
  </li>
  <li>
    <code>dmr_combine_multChrs4rank</code>
    - Combine predicted DMRs/MRs from multiple chromosomes then rank the DMRs by using logistic regresssion model
  </li>
  <li>
    <code>dmr_selected4plot</code>
    - Plot figure and export raw/smoothed methylation data for selected DMR or MR
  </li>
  <li>
    <code>dmr_map2genome</code>
    - Map all DMR/MRs to reference genome
  </li>
  <li>
    <code>dmr_map2chromSegment</code>
    - Map all DMR/MRs to chromation segments generated from 6 human cell lines
  </li>
  <li>
    <code>dmr_cal2genome_percent</code>
    - Calculate percentage of DMRs intersected with predefined genomic regions such as TSS, TES, 5dist et al.
  </li>
  <li>
    <code>dmr_cal2chromSegment_percent</code>
    - Calculate percentage of DMRs intersected with chromatin segments generated from 6 human celles 
  </li>
  <li>
    <code>dmr_percent2plot</code>
    - Plot percentage of DMRs in predefined genomic or chromatin segment regions
  </li>
  <li>
    <code>dmr_combine2geneAnnot</code>
    - Combine annotations from both predefined genomic regions and chromatin segments (This function is slow and requests both genome and chromatin segment results available)
  </li>
  <li>
    <code>dmr_exportData</code>
    - Plot and export data for DMRs/MRs located in specific regions (e.g., DMRs/MRs intersected with mutation block or enhancer regions)
  </li>


  <li><code>dmr_gene_annotation</code>:  
    - Cleans reference file and creates genomic region files (TSS, geneBody, TES, 5dist and intergenic) from the reference. This module is reimplemented here from hmst-seq-analyzer tool https://hmst-seq.github.io/hmst/ 
  </li>
</ul>


DMR-Analysis: A Differentially Methylated Region Analysis Tool

positional arguments:
  task        Pipeline task to run

optional arguments:
  -h, --help  show this help message and exit


          
Having trouble with package? Contact us @ junbai.wang@medisin.uio.no and we will be glad to help you.
You can read the complete documentation here: [ https://dmr-analysis.readthedocs.io/en/latest/index.html ](https://dmr-analysis.readthedocs.io/en/latest/index.html#)
