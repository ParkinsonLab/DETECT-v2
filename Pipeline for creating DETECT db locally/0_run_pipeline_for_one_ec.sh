#!/bin/bash

# $1 = target ec, $2 = serial number, $3 = fasta filename of prepared sequences

python 1_create_fasta_with_target_ec_from_dat.py $1 uniprot_sprot.dat &&
blastp -query $1.fasta -db uniprot_sprot_all_blastdb -outfmt "7 qseqid sseqid ssac qstart qend sstart send evalue bitscore qcovs qcovhsp slen pident" -out $1.bl -evalue 1 -max_target_seqs 100000 &&
python 3_get_blast_results_unique_pairs.py $1 &&
python 4_needleall_one_ec.py $1 $2 $3 &&
cat *.$2.needleall > $1.needleall.final &&
rm *.$2.query.fasta &&
rm *.$2.hits.fasta &&
rm *.error &&
rm *.$2.needleall &&
python 5_format_needleall_one_ec.py $1 $3 &&
python 6_generate_probability_profile_for_one_ec.py $1 $2 &&
rm $1.* &&
rm $1_* &&
wait
