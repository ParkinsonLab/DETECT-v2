Dependencies

EMBOSS, Biopython, NCBI Blast+

Basic Usage

Simply place this folder into your workspace, place raw dat file (named uniprot_sprot.dat) containing all proteins to process and a fasta file of all proteins that meet your 
criteria, generate a blast db based on your list of proteins, and run the bash script "0_reset_for_round_n.sh -n -x", where -n is the number of 
individual jobs to split into (currently set to optimally use some multiple of 8), and -x is the fasta filename of your prepared sequences
(see preprocessing). This will start the pipeline, and should result in two files, one for positive and one for negative densities, per viable EC. 

Configuration

To change the path to your EMBOSS instance, in the script "0_create_run_master_pipelines.py", find the "export=" section in the header variable, and change it to the full directory address of the bin folder of your EMBOSS installation.

To change the batch size from 8 to some other number, in the script "0_create_and_queue_all_master_pipelines.sh", change all instances of the number 8 to some other number. In the script "0_create_run_master_pipelines.py", change the addend in the declaration of the "end" variable to match that other number.

Preprocessing

0_prepare_sequence_data.py: Used to filter out proteins which do not belong to a viable class for analysis in DETECT from dat file into fasta 
file.

0_make_blast_db.sh: Used to generate the blast db based on list of proteins from fasta generated from above. Takes name of result of 0_prepare_sequence_data.py as an argument.

Postprocessing

0_create_mappings_and_prior_probabilities_file.py: Create two files containing the mappings of sequence IDs to EC, and prior probabilities 
used for the Bayesian estimation of DETECT, which will be required for DETECT to function.

0_concatenate_outputs.sh: Concatenate all your various density-pos and density-neg files into a single density-pos.out and density-neg.out file.

0_text_to_db.py: Create sqlite3 database which DETECT relies upon from your mapping and density files.

Notes

When running DETECT, change the name of your fasta file ("uniprot_sprot_prepared.fasta" by default) to "uniprot_sprot.fsa".

For more information, bug reports, or otherwise, please contact: leon.xu@mail.utoronto.ca
