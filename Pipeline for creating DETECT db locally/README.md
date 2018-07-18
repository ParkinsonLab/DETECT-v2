==Pipeline for making the DETECT database locally==

The following outlines the steps to create, from SwissProt, the database eventually used for running DETECT (The Density Estimation Tool for Enzyme ClassificaTion); the scripts in this folder are meant to be run on a desktop computer.

The paper for v2 is in press: Nursimulu N., Xu L.Y., Wasmuth J.D., Krukov I. and Parkinson J. (2018). Improved enzyme annotation with EC-specific cutoffs using DETECT v2. Bioinformatics. 

v1 has been published as well: Hung et al (2010), Bioinformatics vol. 26, no. 14.

For more information, bug reports, or otherwise, please contact: leon.xu@mail.utoronto.ca


=Dependencies=

(1) BioPython

(2) EMBOSS (http://emboss.sourceforge.net/download/)

(3) NCBI Blast+ (https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download)


=Usage=

*Preprocessing steps*

(a) Place this folder into your workspace.

(b) Place raw dat file (named uniprot_sprot.dat) (downloaded typically    
    from SwissProt). 
	
(c) Generate a blast database based on your list of proteins.

    (i)  Run 0_prepare_sequence_data.py
         This filters out proteins which do not belong to a viable 
         EC class for analysis by DETECT (viable classes have >= 30 
         protein sequences) and prepares a fasta file called 
         uniprot_sprot_prepared.fasta.
		 
    (ii) Run 0_make_blast_db.sh: Used to generate the blast db based 
         on list of proteins from fasta generated from above. Takes 
         name of output of 0_prepare_sequence_data.py as an argument 
         (uniprot_sprot_prepared.fasta).
		 
(d) First, make sure to set up the path to the EMBOSS instance.  
    To change the path to your EMBOSS instance, in the script 
    "0_create_run_master_pipelines.py", find the "export=" section in 
    the header variable, and change it to the full directory address 
    of the bin folder of your EMBOSS installation.

*Processing*

(e) Run the bash script "0_reset_for_round_n.sh -n -x", where -n is 
    the number of individual jobs to split into (currently set to 
    use a multiple of 8), and -x is the fasta filename of 
    your prepared sequences (following preprocessing steps). 
    This will start the pipeline, and should result in two files, one 
    for positive and one for negative densities, per EC (ECs with 
    >= 30 protein sequences as per uniprot_sprot.dat). 

    Please note that, if for some reason, the execution of this step    
    is interrupted, it is possible to resume the execution by 
    rerunning the above script.

*Postprocessing*

(f) Run 0_create_mappings_and_prior_probabilities_file.py: 
         Requires as argument the name of the fasta file output from 
         0_prepare_sequence_data.py (uniprot_sprot_prepared.fasta).  
         Creates two files containing the mappings of sequence IDs to 
         EC (swissProt2EC_ids-30+.mappings), and prior probabilities 
         used for the integrated likelihood score calculation of 
         DETECT (prior_probabilities.out), which will be required for 
         DETECT to function.

(g) Run 0_concatenate_outputs.sh: 
         Concatenates all various density-pos and density-neg files 
         into a single density-pos.out and density-neg.out file.

(h) Run 0_text_to_db.py: 
         Creates sqlite3 database (detect.db) upon which DETECT 
         relies.  Uses results from previous post-processing steps.

(i) In a last step, the files generated need to be re-organized to 
    have the following structure under the current folder (called
    DETECTv2 here):

          DETECTv2/data/detect.db
          DETECTv2/data/uniprot_sprot.fsa
          DETECTv2/data/uniprot_sprot.fsa.phr
          DETECTv2/data/uniprot_sprot.fsa.pin
          DETECTv2/data/uniprot_sprot.fsa.psq
          DETECTv2/density-neg.out
          DETECTv2/density-pos.out
          DETECTv2/detect.py
          DETECTv2/ec_to_cutoff.mappings
          DETECTv2/prior_probabilities.out
          DETECTv2/swissProt2EC_ids-30+.mappings

Please note the following:

         (1) Change the name of your fasta file 
             ("uniprot_sprot_prepared.fasta") to "uniprot_sprot.fsa".
         (2) As well, we require that the names of all 
             uniprot_sprot_all_blastdb.* files be changed to 
             uniprot_sprot.fsa.*
         (3) detect.py can be downloaded from the directory “DETECT 
             enzyme annotation tool” on the GitHub repository.
         (4) ec_to_cutoff.mappings can also be downloaded from the 
             above folder.  Please note that this mapping file is most 
             appropriately used alongside the version of SwissProt 
             used to make DETECTv2.  
         (5) ec_to_cutoff.mappings is only required if the user 
             intends to apply the F1-scheme cutoffs introduced in v2.  

