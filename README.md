Local Workstation Version

Please see the README in the Local Folder.

The following is for the distributed version for use on Scinet.

Basic Usage

Simply place this folder into Scinet, place raw dat file of all proteins to process and a fasta file of all proteins that meet your 
criteria, generate a blast db based on your list of proteins, and run the bash script "0_reset_for_round_n.sh -n", where -n is the number of 
individual jobs to split into (currently set to optimally use some multiple of 8). This will start the pipeline, and should result in two 
files, one for positive and oen for negative densities, per viable EC. 

Configuration

To change the path to your EMBOSS instance, in the script "0_create_run_master_pipelines.py", find the "export=" section in the header variable, and change it to the full directory address of the bin folder of your EMBOSS installation.

To change the batch size from 8 to some other number, in the script "0_create_and_queue_all_master_pipelines.sh", change all instances of the number 8 to some other number. 

Notes

If using some batch management system (e.g. qsub, dsub), ensure that the job needs to be submitted in the same directory as the sequence file and the scripts.

Preprocessing

0_prepare_sequence_data: Used to filter out proteins which do not belong to a viable class for analysis in DETECT from dat file into fasta 
file.

0_make_blast_db: Used to generate the blast db based on list of proteins from fasta generated from above. 

Postprocessing

0_create_mappings_and_prior_probabilities_file.py: Create two files containing the mappings of sequence IDs to EC, and prior probabilities 
used for the Bayesian estimation of DETECT, which will be required for DETECT to function.

0_concatenate_outputs.sh: Concatenate all your various density-pos and density-neg files into a single density-pos.out and density-neg.out file.

0_text_to_db.py: Create sqlite3 database which DETECT relies upon from your mapping and density files.

Notes

When running DETECT, change the name of your fasta file ("uniprot_sprot_prepared.fasta" by default) to "uniprot_sprot.fsa".

Warning

Some filenames may have to be changed, such as whenever a reference to the dat or fasta files are made. These filenames will come from 
external sources and are not generated exactly the same way automatically. The path to the EMBOSS package will also have to be changed to 
one that is available to you. Furthermore, please ensure that you have installed all the necessary packages (those that are imported in 
the bash script headers). Finally, this pipeline is designed to run off of the Scinet cluster; usage on other clusters will require further
modifications.

For more information, bug reports, or otherwise, please contact: leon.xu@mail.utoronto.ca
