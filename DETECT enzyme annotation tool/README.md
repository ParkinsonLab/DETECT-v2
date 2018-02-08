==Instructions for running DETECTv2==

Please note that the scripts and the databases required for running DETECTv2 can
be downloaded from http://compsysbio.org/projects/DETECTv2/

This folder has a sample script and fasta file that can be used to run DETECT.

Here, we provide details of the arguments that can be changed for running DETECT:

    target_file           (string) : Required. Path to the file containing the target FASTA sequence(s)
	
	output_file           (string) : Optional. Path of the file to contain the output of the predictions
	
	verbose               (boolean): Optional. Print verbose output if specified.
	
	num_threads           (integer): Optional. Number of threads used by BLASTp
	
	bit_score             (float)  : Optional. The cutoff for BLASTp alignment bitscore
	
	e_value               (float)  : Optional. The cutoff for BLASTp alignment E-value
	
	top_predictions_file  (string) : Optional. Path to the file that enumerates predictions with probability over 0.2
	
	fbeta_file            (string) : Optional. Path to the file that enumerates predictions that pass EC-specific cutoffs
	
	beta                  (float)  : Optional. Value of beta in Fbeta: 1 (default), 0.5 or 2. Fbeta is maximized along EC-specific precision-recall curves to derive EC-specific score cutoffs

==Further information==

The paper for v2 is currently under review; v1 has been published: Hung et al (2010), Bioinformatics vol. 26, no. 14.

For more information, bug reports, or otherwise, please contact: leon.xu@mail.utoronto.ca