Basic Usage

Simply place this folder into your workspace, place raw dat file of all proteins to process and a fasta file of all proteins that meet your 
criteria, generate a blast db based on your list of proteins, and run the bash script "0_reset_for_round_n -n -x", where -n is the number of 
individual jobs to split into (currently set to optimally use some multiple of 8), and -x is the fasta filename of your prepared sequences
(see preprocessing). This will start the pipeline, and should result in two files, one for positive and one for negative densities, per viable EC. 

Preprocessing

0_prepare_sequence_data: Used to filter out proteins which do not belong to a viable class for analysis in DETECT from dat file into fasta 
file.

0_make_blast_db: Used to generate the blast db based on list of proteins from fasta generated from above. 

Postprocessing

0_create_mappings_and_prior_probabilities_file: Create two files containing the mappings of sequence IDs to EC, and prior probabilities 
used for the Bayesian estimation of DETECT, which will be required for DETECT to function.

For more information, bug reports, or otherwise, please contact: leon.xu@mail.utoronto.ca
