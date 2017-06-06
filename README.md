Basic Usage

Simply place this folder into Scinet, place raw dat file of all proteins to process and a fasta file of all proteins that meet your 
criteria, generate a blast db based on your list of proteins, and run the bash script "0_reset_for_round_n -n", where -n is the number of 
individual jobs to split into (currently set to optimally use some multiple of 8). This will start the pipeline, and should result in two 
files, one for positive and oen for negative densities, per viable EC. 

Preprocessing

0_prepare_sequence_data: Used to filter out proteins which do not belong to a viable class for analysis in DETECT from dat file into fasta 
file.

0_make_blast_db: Used to generate the blast db based on list of proteins from fasta generated from above. 

Postprocessing

0_create_mappings_and_prior_probabilities_file: Create two files containing the mappings of sequence IDs to EC, and prior probabilities 
used for the Bayesian estimation of DETECT, which will be required for DETECT to function.

Warning

Some filenames may have to be changed, such as whenever a reference to the dat or fasta files are made. These filenames will come from 
external sources and are not generated exactly the same way automatically.

For more information, bug reports, or otherwise, please contact: leon.xu@mail.utoronto.ca
