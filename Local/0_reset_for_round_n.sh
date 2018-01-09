#!/bin/bash

# To run: bash 0_reset_for_round_n -partitions -fasta_filename
# Replace -partitions with the number of partitions (should match number of eligible_ec files from 0_get_eligible_ecs)
# and -fasta_filename with the name of the fasta file with the prepared sequences (output of 0_prepare_sequence_data)

rm *.hits.fasta || true &&
rm *.query.fasta || true &&
rm *.needleall || true &&
rm *.error || true &&
rm *[1,2,3,4,5,6,7,8,9,0].bl || true &&
rm *[1,2,3,4,5,6,7,8,9,0].needleall.final || true &&
rm *[1,2,3,4,5,6,7,8,9,0]_unique_pairs.txt || true &&
rm *[1,2,3,4,5,6,7,8,9,0]_aligned_unique_pairs.txt || true &&
rm *[1,2,3,4,5,6,7,8,9,0].*[1,2,3,4,5,6,7,8,9,0].*[1,2,3,4,5,6,7,8,9,0].*[1,2,3,4,5,6,7,8,9,0].fasta || true &&
cp processed.txt processed2.txt || true &&
rm processed.txt || true &&
cat processed.*.txt processed2.txt > processed.txt || true &&
rm processed2.txt || true &&
rm processed.*.txt || true &&
rm eligible_ecs.*.txt || true &&
rm master_pipeline.*.sh || true &&
rm run_master_pipelines.*.sh || true &&
python 0_get_eligible_ecs.py $1 $2 processed.txt &&
python 0_create_run_pipeline_forall_ec.py $1 $2 &&
bash 0_create_and_queue_all_master_pipelines.sh $1 &&
wait
