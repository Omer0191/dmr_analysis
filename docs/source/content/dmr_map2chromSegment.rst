dmr_map2chromSegment
====================

Map DMR/MRs to predicted chromatin segments from 6 human cell lines.

Required Parameters
-------------------
- ``-inFolder IN_CHROMATINSEGMENT_FILE_FOLDER`` or ``--in_chromatinSegment_file_folder IN_CHROMATINSEGMENT_FILE_FOLDER``: Path of the input file folder containing combined chromatin segment files from six cells in BED format. The combined six cells `*.bed.gz` files can be downloaded from [https://genome.ucsc.edu/cgi-bin/hgFileUi?db=hg19&g=wgEncodeAwgSegmentation](https://genome.ucsc.edu/cgi-bin/hgFileUi?db=hg19&g=wgEncodeAwgSegmentation).
- ``-outFolder IN_OUTFILE_FOLDER`` or ``--in_outFile_folder IN_OUTFILE_FOLDER``: Path of the output file folder for DMR/MRs mapped to chromatin segments.
- ``-inDFile IN_DMR_FILE`` or ``--in_DMR_file IN_DMR_FILE``: Input DMR file name, which is a sorted export file from DMR_analysis with BED format, such as the export file from "dmr_combine_multChrs4rank".

Optional Parameters
-------------------
- ``-inMinLen IN_MINIMUM_LENGTH4REGION`` or ``--in_minimum_length4region IN_MINIMUM_LENGTH4REGION``: The minimum length for each selected chromatin segment. The default is 10 bp.
- ``-inFileStr IN_FILENAME_STRING`` or ``--in_fileName_string IN_FILENAME_STRING``: String name for input chromatin segment files that are stored in the folder. The default is `*.bed.gz`.
- ``-OFileStr IN_OUTFILENAME_STRING`` or ``--in_outFileName_string IN_OUTFILENAME_STRING``: Output file type string that will be used for output combined chromatin segment files. The default is "combined_six_cells_chromatin_segment_min".
- ``-inMinOp IN_MINIMUM_OVERLAP4BEDTOOLS`` or ``--in_minimum_overlap4bedtools IN_MINIMUM_OVERLAP4BEDTOOLS``: The minimum overlap rate in bedtools intersection. The default is 1e-9 or 1 bp.
- ``-inExist IN_COMBINED_CHROMATINSEGMENT_EXIST`` or ``--in_combined_chromatinSegment_exist IN_COMBINED_CHROMATINSEGMENT_EXIST``: Indicates whether the combined six cell chromatin segment files exist or not. Use 0 for "not exist," which means the ``-in_chromatinSegment_file_folder`` is the path for raw files downloaded. Use 1 if the combined six cell chromatin segment files are ready and sorted by chromosome position, where the path of ``-inFolder`` is the location of these combined files of six cells with filenames starting with "combined_six_cells_*.gz". The default is 0.

