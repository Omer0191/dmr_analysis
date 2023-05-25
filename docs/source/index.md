
 
<img align="center" src="https://user-images.githubusercontent.com/79196757/180248926-efd6e216-0683-4549-99f0-e6783224a2c7.png">
<img align="right" src="https://user-images.githubusercontent.com/79196757/180251608-da859f67-aa58-49e8-bea8-a0258be93635.png"><img align="left" src="https://user-images.githubusercontent.com/79196757/180251606-8e257ad0-86d5-4cb7-b549-ed5e5c0aa9eb.jpg">  





# Differential Methylated Region Analysis Tool 
## dmr_analysis Documentation

dmr_analysis is a software tool for differentially Methylated Regions analysis to rank significant DMRs.




## Modules:
[Home](index.md) | [DMR Block Analysis](dmr_analysis_block.md) | [Combine MultiChr4Rank](dmr_combine_multChrs4rank.md) | [Selected4plot](dmr_selected4plot.md) | [map2genome](dmr_map2genome.md) | [map2chromSegment](dmr_map2chromSegment.md) | [cal2genome_percent](dmr_cal2genome_percent.md) | [cal2chromSegment_percent](dmr_cal2chromSegment_percent.md) | [percent2plot](dmr_percent2plot.md) | [combine2geneAnnot](dmr_combine2geneAnnot.md) | [exportData](dmr_exportData.md)  | [gene annotation](dmr_gene_annotation.md) 


## Download:

dmr_analysis is written in python. It can be installed and accessed from command line and is avalible for both linux and mac operating systems. The package can be downloaded [here](https://github.com/dmr-analysis/dmr_analysis/archive/refs/heads/master.zip) . Or type command:

<pre>wget https://github.com/dmr-analysis/dmr_analysis/archive/refs/heads/master.zip </pre>
	
## Installation:
## Installation:
<p>It is highly recommended to create a separate virtual environment for the package to avoid any library conflicts problem. You you create virtual environment using the following commands. We recommend to use install and use miniconda/anaconda (https://docs.conda.io/en/latest/miniconda.html). Tutorial of creating and updating virtual commands can be found at (https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) </p> 

If the minicinda is already installed, then you can proceed with the following step by step installation. We have already provided a quick installation setup file named quick_install.sh for your ease. A simple bash command will do everything autmatically and prepare the package, ready to run. 
<pre> ./quick_install </pre>

However step by step details are given as under and can be following if quick_install.sh is unsuccessful:

<pre>conda create --name dmr_env python==3.9.16
conda activate dmr_env</pre>

<p>Install pip if not already installed: </p>
<pre> conda install pip</pre>

Please allow any other installations when prompted

<p>Prior to installing the package, dependencies must be fulfilled. It is advised to install dependencies using miniconda. List of dependencies is as follows: </p>
<ul>
  <li>matplotlib==3.5.3</li>
  <li>numpy==1.21.5</li>
  <li>pandas==1.4.4</li>
  <li>scikit_learn==1.2.2</li>
  <li>scipy==1.9.1</li>
  <li>setuptools==65.6.3</li>
  <li>statsmodels==0.13.5</li>
  <li>bedtools==2.27.0</li>
</ul>



These dependencies can be installed one by one using conda manager. For example:

<pre>conda install numpy==1.21.5</pre>
	
A requirements.txt file is given with the package. All requiremnts can be automatically installed using one command:
<pre>conda install --file requirements.txt</pre>

Or can be installed using pip.

<pre>pip install numpy==1.21.5</pre>
	
A requirements.txt file is given with the package. All requiremnts can be automatically installed using one command:
<pre>pip install -r requirements.txt</pre>

You can install the package using following command, go to the dmr_analysis directory (folder containing setup.py and pyproject.toml) and type the following command
<pre>pip install .</pre>

For more details, follow the readme file in the package.

		
## Contents of the package:
		
<p>The package folder will contain following:
	</p>
<ul>
	<li><code>final_demo</code> : Contains functions scripts.</li>
	<li><code>dmr_analysis</code> : Contains python soruce code of pipeline.</li>
	<li><code>readme.txt</code> : Instructions about usage of package.</li>
	<li><code>requirments.txt</code> :  List of requirements. Can be used for automatic installation from miniconda or pip.</li>
	<li><code>setup.py</code>: Setup file for package.</li>
	<li><code>final_demo_data</code>: Contains data in and out for the secondary functions.</li>


</ul>	
	

	
## Pipeline Tasks:
	
<p>The pipeline consists of follwoing tasks. To run a task, type dmr_analysis task args. To see what are the options for each task of the pipeline, please run: dmr_analysis -h </p>

<ul>
<li><code>dmr_analysis_block </code> : Predict Differentially Methylated Region (DMR) from genome-wide methylation regions such as by using WGBS or other similar techniques.</li>
	<li><code>dmr_combine_multChrs4rank </code> : Combine predicted DMRs/MRs from multiple chromosomes then rank the DMRs by using logistic regresssion model. </li>
	<li><code>dmr_selected4plot</code> : Plot figure and export raw/smoothed methylation data for selected DMR or MR.</li>
	<li><code>dmr_map2genome</code> : Map all DMR/MRs to reference genome.</li>
	<li><code>dmr_map2chromSegment</code> : Map all DMR/MRs to chromation segments generated from 6 human cell lines.</li>
	<li><code>dmr_cal2genome_percent</code> : Calculate percentage of DMRs intersected with predefined genomic regions such as TSS, TES, 5dist et al.</li>
	<li><code>dmr_cal2chromSegment_percent</code> :Calculate percentage of DMRs intersected with chromatin segments generated from 6 human celles.</li>
	<li><code>dmr_percent2plot</code> : Plot percentage of DMRs in predefined genomic or chromatin segment regions.</li>
	<li><code>dmr_combine2geneAnnot</code> : Combine annotations from both predefined genomic regions and chromatin segments (This function is slow and requests both genome and chromatin segment results available).</li>
	<li><code>dmr_exportData</code>:  Plot and export data for DMRs/MRs located in specific regions (e.g., DMRs/MRs intersected with mutation block or enhancer regions).</li>
	<li><code>dmr_gene_annotation</code>:  Cleans reference file and creates genomic region files (TSS, geneBody, TES, 5dist and intergenic) from the reference. This module is reimplemented here from hmst-seq-analyzer tool https://hmst-seq.github.io/hmst/ </li>
	
</ul>
	
## Demos

[Demo1: FL](demo1.md) | 
[Demo2: HAP](demo2.md) | 
[Demo3: RAT](demo3.md) 
	
         	
           			
         	
         		
         		
         	
Having trouble with package? Contact us @ junbai.wang@medisin.uio.no and we will be glad to help you.
You can go to look inside the code here: [https://github.com/dmr-analysis/dmr_analysis](https://github.com/dmr-analysis/dmr_analysis)
