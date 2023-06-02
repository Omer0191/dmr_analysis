demo1
=====


Follicular Lymphoma
____________________



This script is a Bash script that calls the dmr_analysis program to predict differentially methylated regions (DMRs) and methylated regions (MRs) from whole-genome bisulfite sequencing (WGBS) data for Foliculuar Lymphoma.</p>


Run Demo1:

  Demo1 can be run by executing the bash script given with the pacakge. In this demo DNA methylation Regions are found and ranked.

.. code-block:: bash

    sbatch job_dmr

While `job_dmr` is run in a cluster computer (SAGA) provided by Norwegian Research Infrastructure Services(NRIS). Remember to change this according to your machine. `job_dmr` looks like this

.. code-block:: bash

    #!/bin/bash
    #SBATCH --job-name=demo1-dmr
    #SBATCH --time=15:00:00
    #SBATCH --mem-per-cpu=15G --partition=bigmem
    # Number of cores:
    #SBATCH --cpus-per-task=15

    #set up job environment
    #source /etc/profile.d/modules.csh
    #source /cluster/bin/jobsetup
    #module use --append /cluster/etc/modulefiles
    #module load java/jdk1.7.0_80
    #module unload Java/1.8.0_212
    #module purge
    #module --ignore-cache load Java/1.7.0_80

    module load BEDTools/2.27.1-foss-2018b
    ./demo1_dmr_analysis_fl_12samples.sh


Here this job calls a shell script file `demo1_dmr_analysis_fl_12samples.sh`. This script is prepared by calling different modules of the dmr analysis. The demo assumes that the input data is already prepared in bed format, organized in chromosome named folders, and that the genome size file and refFlat files are available in a separate folder. Some initial parameter setting is done in the start of the script file as follows:</p>

**In folder path:** final_demo_data/fl_12samples/in_data/WGBS-data/

**Out folder path:** final_demo_data/fl_12samples/out_data/DMR_CpG_context/

.. code-block:: bash

    #!/bin/bash

    #use bash script to call dmr_analysis
    ##Please note variable under "#-- " have to be manually adjusted in different run or in different input data!


    #path of input data folder
    #here, we assume all WGBS methylation profiles are already prepared in bed format at chromosome named folders under in_wgbs_folder,
    #-- where file names indicate the sample name and conditions
    in_wgbs_folder='../../final_demo_data/fl_12samples/in_data/WGBS-data/'

    #path of input reference genome folder
    #-- where genome size file and refFlat files will be used in making predefined genomic regions (e.g., TSS, TES, gene et al.) by dmr_analysis module dmr_gene_annotation
    in_genome_folder='../../final_demo_data/genome/hg19/'
    in_genome_refFlat='hg19.refFlat.txt'
    in_genome_size='hg19.chrom.sizes.clear.sorted'
    replace='_clean_sorted.bed'
    finds='.txt'
    in_sorted_refFlat=${in_genome_refFlat//$finds/$replace}

    #path of input chromatin segment folder
    #such as combined chromatin segment from six human cell lines generated from Encode project https://genome.ucsc.edu/cgi-bin/hgFileUi?db=hg19&g=wgEncodeAwgSegmentation
    #-- where each predicted chromatin type (e.g., TSS, Enhancers) is listed in a bed formated file and the file name indicate the predicted chromatin type.
    in_chromSegment_folder='../../final_demo_data/chromSegment/hg19/'

    #output data folder
    #path to output folders
    #-- where predicted DMR/MRs will be exported
    out_result_folder='../../final_demo_data/fl_12samples/out_data/DMR_CpG_context'

    #-- Name of output folders and files that will be created in out_result_folder
    out_folder4genome_map='out_map2genome'
    logProb_cutoff=0.7
    out_file4genome_map=gcb_vs_tumor_DMR_hyper_hypo_mix_${logProb_cutoff}.csv
    out_folder4chromSegment_map='out_map2chromSegment'
    out_file4chromSeg_map=gcb_vs_tumor_DMR_hyper_hypo_mix_in_chromSeg_${logProb_cutoff}.csv
    #a file name that contains all ranked DMRs by combining results from all chromosomes
    mr_IN_FILE='2_chroms_all_mr_data_range_dmrRanking'

**In folder path:** final_demo_data/fl_12samples/in_data/WGBS-data/
WGBS methylation profiles (input) in bed format looks like the following.
Path: `final_demo_data/fl_12samples/in_data/WGBS-data/chr18/`

.. code-block:: bash

    chr18   57000331        57000331        0.88    33      1
    chr18   57000413        57000413        0.9     48      1
    chr18   57000458        57000458        0.75    51      1
    chr18   57001635        57001635        0.55    94      1
    chr18   57001648        57001648        0.55    100     1
    chr18   57001786        57001786        0.67    119     1
    chr18   57001813        57001813        0.73    97      1
    chr18   57002348        57002348        0.93    42      1
    chr18   57002349        57002349        0.83    30      1
    chr18   57002437        57002437        1.0     51      1

In the first step, the DMRs are predicted and then predicted DMRs and MRs are then exported to the output data folder, and the results from all chromosomes are combined and ranked.

- In part a, the `dmr_analysis_block` module is used to predict DMRs in chr18 and chrY.
- They are combined using the `dmr_combine_multChrs4rank` script to combine and rank the DMRs across multiple chromosomes.


Step 1:
______

.. code-block:: bash

    #STEP 1. run dmr_analysis to predict DMRs
    #a) do dmr_analysis in blocks
    for in_chrom in chrY chr18
    do
    dmr_analysis dmr_analysis_block --in_file_folder $in_wgbs_folder \
            --chromosome $in_chrom --group_key $in_chrom \
            --out_file_folder $out_result_folder \
            --wildType_fileString gcb \
            --data_start_position 3 --data_end_position 15 \
            --maximum_adjacency_length 1000 --minimum_block_size 5 \
            --P_cutoff 0.05 --minimum_percentage_changes 0.0001 \
            --percentage_cutoff 0.05,0.1,0.2 --low_median_high_cutoff 2 \
            --number_of_processes 15 \
            --is_smoothed_data 2 --is_moderate_ttest 0 --is_export_data 1 \
            --column_splitBy_dotOrUnderscore 1
    done
    echo "dmr_analysis_block - Done"

    #b) combine results from multiple chromosomes and rank the DMRs
    dmr_analysis dmr_combine_multChrs4rank \
            --in_chroms_number chr18,chrY \
            --in_file_fold $out_result_folder \
            --in_is_smoothed_data 2 \
            --in_LogReg_proba 0.7 \
            --in_low_median_high_cutoff high \
            --in_file_ending_string _range.tsv
    echo dmr_combine_multChrs4rank - Done

Step 2:
______
  In the second step, the script plots using dmr_selected4plot and exports data for selected DMRs using the module dmr_exportData. The code and parameter setting can be seen as follows:

- In part a, the `dmr_selected4plot` module is used to select DMRs for plotting.
- In part b, output data and results are then exported using the `dmr_exportData` module. Here only chromosome 18 is selected for demo purposes.


.. code-block:: bash

    #STEP 2. Plot and export data
    chrom='chr18'
    #-- please note the name of in_DMR_file may be changed in different run because of the parameters, the total number of input and the top percentage et al
      #in_DMR_file=${chrom}'_maxDist_1000_minSize_5_DMR_clusterAccuracy_gt_0.5_miniMethyChange_gt_0.05_0.1_0.2_high_miniPercentChange_gt_0.0001_Pcutoff_0.05_isSmooth_2_isModTest_0_1285_range_dmrRanking_top_0.78_minLogReg_proba_0.7'
    in_DMR_file=${chrom}'_all_mr_data_range_dmrRanking.tsv'
    in_data_file=${chrom}'_MR_data4maxBlockDistance_1000_minBlockSize_5_data.txt.gz'
    in_wildType_string='gcb'

    #some additional features for plotting and exporting data
    #select DMR for ploting such as mr5,mr6,mr8 from selected chromosome
    #here --in_DMR_file is exported by dmr_combine_multChrs4rank at folder "out_result_folder"/chrY/plots
    ##--in_data_file is exported by dmr_analysis_block at folder "out_result_folder"/chrY
    dmr_analysis dmr_selected4plot --in_DMR_file ${in_DMR_file} \
            --in_data_file  ${in_data_file} \
            --in_data_folder ${out_result_folder}/${chrom}/ \
            --column_splitBy_dotOrUnderscore 1 --is_plot 1 --is_export 1 \
            --needs_check_mr mr5,mr6,mr8 --wildType_fileString ${in_wildType_string} \
            --out_folder ${out_result_folder}/out_selected4plot

    echo "dmr_selected4plot -- Done"

    #export selected DMR based on bed format file 0
    ##--input_file contains all MRs in bed foramt that need to extract their raw and smoothed methylation data
    dmr_analysis dmr_exportData  \
                           --input_mr_data_folder ${out_result_folder} \
                           --output_file_folder ${out_result_folder}/out_exportData \
                           --input_file_format 0 \
                           --wildType_fileString ${in_wildType_string} --column_splitBy_dotOrUnderscore 1 --input_file test_mr.bed

    echo "dmr_ExportData -- Done"

Step 3:
______

In the third step, it maps the predicted DMRs and MRs to predefined genomic regions using dmr_analysis.. This demo also includes several parameters that can be manually adjusted , such as the path of the input and output data folders, the name of output folders and files, and the selected DMRs for plotting.

- In part a, genomic regions are generated using the `dmr_analysis` module `dmr_gene_annotation`.
- In the part b, DMRs are mapped into genomic regions defined in part a.
- Part c performs percentage calculations of DMR in annotated genomic regions.
- These percentages from part c are plotted in the last step d..


.. code-block:: bash

    #STEP 3. mapp predicted DMR/MRs to predefined genomic regions (e.g., TSS, TES, 5dist etl al) or predicted chromatin segments for further analysis
    #below is a result file generated from dmr_combine_multChrs4rank, where DMR/MRs from multiple chromosomes are combined and ranked them by logisitic regression model
    #-- Please note this file name needs to be input manually because it is generated after running "dmr_combine_multChrs4rank" and expored at folder "out_result_folder"
    #mr_IN_FILE='2_chroms_high_miniPercentChange_gt_0.0001_Pcutoff_0.05_isSmooth_2_isModTest_0__range_dmrRanking_top_0.78_minLogReg_proba_0.7'

    #a) generate predefined genomic regions (e.g., TSS, TES, gene et al.) by dmr_analysis (Used for gene annotation, Omer 27, April, 23)

    #Here, to edit exported "list_region_files.txt" for adding/removing predefined genomic regions
    #For example, to add file path for enhancer reginos in "list_region_files.txt" if user want to include enhancer in the analysis

    dmr_analysis dmr_gene_annotation -F ${out_result_folder} -i no -l 10 \
            -xL 50000000 -X 5000 -Y 1000 -M 5000 -N 1000000 -hu yes -n no \
            -r ${in_genome_folder}/${in_genome_refFlat} \
            -g ${in_genome_folder}/${in_genome_size}
    echo export genome annotation files at: ${out_result_folder}/data
    echo gene_annotation-Done

    #b) map DMR to predefined genomic regions such as TSS, TES, gene et al.
    dmr_analysis dmr_map2genome --in_sortedDMR_file ${out_result_folder}/${mr_IN_FILE}.bed \
            --in_geneRegion_file ${out_result_folder}/list_region_files.txt \
            --in_outFile_folder ${out_result_folder}/${out_folder4genome_map} \
            --in_refFlat_file ${out_result_folder}/data/${in_sorted_refFlat}
    echo dmr_map2genome - Done

    #c) calculate percentage of DMR in annotated genomic regions
    dmr_analysis dmr_cal2genome_percent --in_outFile_folder ${out_result_folder}/${out_folder4genome_map} \
            --in_outFile_name ${out_file4genome_map} --in_LogReg_proba ${logProb_cutoff} \
            --in_fileName_string $mr_IN_FILE
    echo dmr_cal2genome_percent - Done

    #d) plot percentage of DMR in annotated genomic regions
    dmr_analysis dmr_percent2plot --in_countFile_folder ${out_result_folder}/${out_folder4genome_map} \
            --in_countFile_name ${out_file4genome_map}
    echo dmr_percent2plot - Done


    #e) map DMR to predicated chromatin states such as predicated chromatin segment from 6 human cell lines.
    dmr_analysis dmr_map2chromSegment --in_chromatinSegment_file_folder ${in_chromSegment_folder} \
            --in_fileName_string 'combined_six*bed.gz' --in_combined_chromatinSegment_exist 1 \
            --in_outFile_folder ${out_result_folder}/${out_folder4chromSegment_map} \
            --in_DMR_file ${out_result_folder}/${mr_IN_FILE}.bed
    echo dmr_map2chromSegment - Done

    #f) calculate percentage of DMRs in predicted chromatin states.
    dmr_analysis dmr_cal2chromSegment_percent --in_outFile_folder ${out_result_folder}/${out_folder4chromSegment_map} \
            --in_outFile_name ${out_file4chromSeg_map} \
            --in_fileName_string ${mr_IN_FILE}_combined_six_cells_chromatin_segment_min10
    echo dmr_cal2chromSegment_percent - Done

    #g) plot percentage DMR in chromSegment
    dmr_analysis dmr_percent2plot --in_countFile_folder ${out_result_folder}/${out_folder4chromSegment_map} \
            --in_countFile_name ${out_file4chromSeg_map}
    echo dmr_percent2plot - Done

    #h) Combine annotated results from both genome and chromatin segment
    #please note both genome and chromatin segment have to be available before running this function.
    #This function is slow and not recommend to use for large data but use dds_analysis instead.
    dmr_analysis dmr_combine2geneAnnot --number_of_processes 10 --miniLogReg_proba_cutoff 0.7 \
            --sortedDMR_file ${mr_IN_FILE}.bed \
            --dmr_outFile_folder ${out_result_folder}/ \
            --dmr_genomeFile_folder ${out_folder4genome_map} \
            --dmr_chromSegmentFile_folder ${out_folder4chromSegment_map} \
            --dmr_genomeFile_string '2_chroms_*' \
            --dmr_chromSegmentFile_string '2_chroms_*'
    echo dmr_combine2geneAnnot - Done

Output
______

Output produced can be found under the folder:
 final_demo_data/rat_data/out_data/DMR_CpG_context/

 A log file is maintained to track the progress and steps of pipeline.

.. code-block:: bash

    Thu, 30 Mar 2023 12:26:36 INFO     File load ['../../final_demo_data/fl_12samples/out_data/DMR_CpG_context/chrY/chrY_MR_data4maxBlockDistance_1000_minBlockSize_5_data.txt.gz']
    Thu, 30 Mar 2023 12:26:39 INFO     Blocks with distance greater than 1000
    Thu, 30 Mar 2023 12:26:39 INFO      and minimum data points in block 5
    Thu, 30 Mar 2023 12:26:39 INFO     block size 574
    Thu, 30 Mar 2023 12:26:39 INFO     Export data in  ../../final_demo_data/fl_12samples/out_data/DMR_CpG_context/chrY_MR_data4maxBlockDistance_1000_minBlockSize_5_data.txt
    Thu, 30 Mar 2023 12:26:41 INFO     minimum MR length 17
    Thu, 30 Mar 2023 12:26:41 INFO     maximum MR length 67329
    Thu, 30 Mar 2023 12:26:42 INFO     Maximum length of adjancey CpG sites in a block 1000
    Thu, 30 Mar 2023 12:26:42 INFO     Hist plot n [ 39 118  60 224  71  60   2]
    Thu, 30 Mar 2023 12:26:42 INFO              bins [   17   100   500  1000  5000 10000 50000 67429]
    Thu, 30 Mar 2023 12:26:42 INFO     mininum MR data size 5
    Thu, 30 Mar 2023 12:26:42 INFO     maximum MR data size 1184
    Thu, 30 Mar 2023 12:26:50 INFO     Wild type /control sample file name is gcb
    Thu, 30 Mar 2023 12:26:50 INFO     Wild/control sample 4 ,
    Thu, 30 Mar 2023 12:26:50 INFO     Tumor/KO sample 8 ,
    Thu, 30 Mar 2023 12:26:50 INFO     DMR export path ../../final_demo_data/fl_12samples/out_data/DMR_CpG_context/chrY/plots
    Thu, 30 Mar 2023 12:26:50 INFO     DMR export MR data path ../../final_demo_data/fl_12samples/out_data/DMR_CpG_context/chrY/data
    Thu, 30 Mar 2023 12:26:50 INFO     Do parallel calculation by using 15 processes
    Thu, 30 Mar 2023 12:32:36 INFO     Export all position results at : ../../final_demo_data/fl_12samples/out_data/DMR_CpG_context/chrY/plots/chrY_all_mr_data.tsv
    Thu, 30 Mar 2023 12:32:36 INFO     Export range position results at : ../../final_demo_data/fl_12samples/out_data/DMR_CpG_context/chrY/plots/chrY_all_mr_data_range.tsv

The output file contain information about DMR and are ranked. Each row shows one region with the pvalue of smoothed and interpolated data, percentages and many other values conculated in the pipeline.
Here is how an output file look like :
`final_demo_data/fl_12samples/out_data/DMR_CpG_context/chrY/plots/chrY_all_mr_data_range.tsv`

.. code-block:: bash

    mr_id   T-test_pval_smoothed_data       T-test_pval_interpolated_data   percent_data_passed_ttest       gcb_vs_grpsDist_pval    tumor_vs_grpsDist_pval  gcb_vs_grpsDist_tval    tumor_vs_grpsDist_tval  cluster_accuracy        low_negative_tumor_vs_gcb_percent median_negative_tumor_vs_gcb_percent    high_negative_tumor_vs_gcb_percent      low_positive_tumor_vs_gcb_percent       median_positive_tumor_vs_gcb_percent  high_positive_tumor_vs_gcb_percent      is_DMR  position  DMR_type        chroms  log10_gcb_vs_grpsDist_pval      log10_tumor_vs_grpsDist_pval    log10_gcb_vs_grpsDist_pval_minMaxNorm   log10_tumor_vs_grpsDist_pval_minMaxNorm dmr_weight_score        percent_data_passed_ttest_gt_pvallogReg_score     logReg_predicted_dmr
    mr1130  0.000405656     0.00432085      0.0     0.761592        0.297122        0.310908        -1.05249        0.5     0.166667        0.0     0.0   0.0     0.0     0.0     U       chr18,63982541-63982589,5       mix     chr18   0.11827755858580184       0.5270650160086492      0.01702962203404642     0.07612316109961371     0.07490444530138562     0.0     -6.823775494058065      0.0010864253038653845
    mr500   5.20997e-10     1.68717e-06     0.0     0.817423        0.390883        -0.237085       -0.864533       0.5     0.209677        0.0     0.0   0.0     0.0     0.0     U       chr18,59912234-59912855,17      mix     chr18   0.08755308328330652       0.4079530847290674      0.012591791521204805    0.05891959092626307     0.07144182119159485     0.0     -6.8234527264599        0.001086775642195305
    mr184   0.34332 0.920516        0.0     0.678555        0.690795        -0.430763       0.39985 0.5     0.357143        0.0     0.0     0.0     0.0   0.0     U       chr18,58245851-58245998,6       mix     chr18   0.1684148687173299
            0.16065073958744097     0.02427143438536842     0.023201227509822907    0.06759562590323061     0.0     -6.809317575408866  0.0011022294112695151
    mr284   0.000270497     5.56906e-05     0.0     0.450906        0.467845        -0.781612       -0.730842       0.5     0.0     0.0     0.0     0.0   0.0     0.0     U       chr18,58749933-58749974,5       mix     chr18   0.34591387087929026       0.32989789693747895     0.04990931688907101     0.047645926851295275    0.0756088389984586      0.0     -6.797317450326605      0.0011155211388911381
    mr842   0.980768        0.999694        0.0     0.247502        0.162594        -1.27073        1.41585 0.5     0.0689655       0.0     0.0     0.0   0.0     0.0     U       chr18,62268226-62269676,5       mix     chr18   0.6064210781164319        0.788895166252045       0.08753687022269127     0.11393980393985409     0.09223626786600726     0.0     -6.785332833066833      0.0011289554816031888
    mr467   0.0104659       0.0635359       0.0     0.433502        0.977244        -0.830386       0.0286541       0.5     0.0     0.0     0.0     0.0229885       0.00383142      0.0     U       chr18,59743199-59745815,33      mix     chr18     0.36300877509976437     0.009996934354542979    0.05237849778855943     0.0014420025324108899   0.06861128005135525     0.0     -6.783096637705215      0.0011314800117390564

Top two rows of all results file looks like following. It gives information about methylated region, its relative chromosome number, logistic regression probablity and gene information.

.. code-block:: bash

    mr_chrs mr_start_pos    mr_end_pos      mr_info mr_logReg_proba genome_info     chromSegment_info
    chr18   57022124        57027729        chr18:mr5:hypo:D        0.999871        chr18:57025497:57031497:NM_005570||TSS:5000:1000||LMAN1:-:56995055:57026497~chr18:56996055:57025497:NM_005570||gene:5000:1000||LMAN1:-:56995055:5702649~E~R~TSS~PF~T
    chr18   57028952        57030829        chr18:mr6:hypo:D        0.999902        chr18:57025497:57031497:NM_005570||TSS:5000:1000||LMAN1:-:56995055:57026497~chr18:56343696:57338696:NM_006785||5distD:5000:1000000||MALT1:+:56338696:56221709~chr18:56486111:57481111:NR_146904||5distD:5000:1000000||LINC01926:+:56481111:56501596~chr18:56535155:57530155:NM_018181||5distD:5000:1000000||ZNF332:+:56530155:56653712~chr18:56535714:57530714:NM_001353526||5distD:5000:1000000||ZNF532:+:56530714:56653712~chr18:56536322:57531322:NM_001318728||5distD:5000:1000000||ZNF532:+:56531322:56653712~chr18:56536590:57531590:NM_001353531||5distD:5000:1000000||ZNF532:+:56531590:56653712~chr18:56537108:57532108:NM_001353527||5distD:5000:1000000||ZNF532:+:56532108:56653712~chr18:56707910:57702910:NR_024021||5distD:5000:1000000||OACYLP:+:56702910:56720446~chr18:56812115:57807115:NM_001307941||5distD:5000:1000000||SEC11C:+:56807115:56826063~chr18:56892389:57887389:NM_001012513||5distD:5000:1000000||GRP:+:56887389:56898002~chr18:56364655:57359655:NM_133459||5distD:5000:1000000||CCBE1:-:57098170:57364655~chr18:56301323:57296323:NM_052947||5dist:5000:1000000||ALPK2:-:56148481:56296323~chr18:56945686:57940686:NM_013435||5dist:5000:1000000||RAX:-:56934269:56940686~chr18:56990881:57985881:NM_181654||5dist:5000:1000000||CPLX4:-:56962633:56985881~chr18:56567227:57562227:NM_021127||5dist:5000:1000000||PMAIP1:+:57567227:57571537     R~T
