#!/bin/bash
# To run: bash 0_make_blast_db.sh -fasta_filename
makeblastdb -in $1 -title uniprot_sprot_all_blastdb -dbtype prot -out uniprot_sprot_all_blastdb