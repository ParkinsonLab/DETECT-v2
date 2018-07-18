==Instructions for running DETECTv2==


=Dependencies=

We first highlight the following dependencies required for running DETECT:

(1) BioPython

(2) EMBOSS (http://emboss.sourceforge.net/download/)

(3) NCBI Blast+ (https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download)


=Instructions=

To run DETECT, please follow the following instructions:

(1) Go to http://compsysbio.org/projects/DETECTv2/ to download the scripts and the complete databases
required for running DETECTv2.  This GitHub directory only holds the scripts required to run DETECT.

(2) Download DETECTv2.tar.gz and unzip it.

(3) (Optional) Test that you can run DETECT.

	(a) Navigate to the folder containing DETECTv2 scripts.  
	You will find a sample script (sample.sh) and fasta file (sample.fasta) for a quick test. 

	(b) Change the value of the variable DETECT_FOLDER (line 1) within sample.sh to represent the absolute path to the DETECTv2 folder (containing detect.py and sample.sh).

	(c) We require that the path to EMBOSS be added to the PATH variable on line 5 of sample.sh.
	We have given in sample.sh a typical directory where EMBOSS may be installed (/usr/local/bin/).  
	This directory may need to be changed.

	(d) Change into DETECT_FOLDER.  Run sample.sh.
	
	(e) As is, the following files should be created within DETECT_FOLDER:  sample.top, sample.out, and sample.f1.out.

(4) Run DETECT script.

	(a) Use sample.sh, and modify as explained in (3)(a), and (b).  
	Further modifications can be made; for more information, look into the following section ("Details of arguments for DETECTv2").
	
	(b) Change into the folder containing your script.  Run sample.sh.
	

	
=Details of arguments for DETECTv2=

Here, we provide details of the arguments for running DETECT:

    target_file           (string) : Required. Path to the file containing the target FASTA sequence(s)
	
	output_file           (string) : Optional. Path of the file to contain the output of the predictions
	
	verbose               (boolean): Optional. Print verbose output if specified.
	
	num_threads           (integer): Optional. Number of threads used by BLASTp
	
	bit_score             (float)  : Optional. The cutoff for BLASTp alignment bitscore
	
	e_value               (float)  : Optional. The cutoff for BLASTp alignment E-value
	
	top_predictions_file  (string) : Optional. Path to the file that enumerates predictions with probability over 0.2
	
	fbeta_file            (string) : Optional. Path to the file that enumerates predictions that pass EC-specific cutoffs
	
	beta                  (float)  : Optional. Value of beta in Fbeta: 1 (default), 0.5 or 2. Fbeta is maximized along EC-specific precision-recall curves to derive EC-specific score cutoffs

	
=Further information=

The paper for v2 is in press: Nursimulu N., Xu L.Y., Wasmuth J.D., Krukov I. and Parkinson J. (2018). Improved enzyme annotation with EC-specific cutoffs using DETECT v2. Bioinformatics. 

v1 has been published as well: Hung et al (2010), Bioinformatics vol. 26, no. 14.

For more information, bug reports, or otherwise, please contact: leon.xu@mail.utoronto.ca