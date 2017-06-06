#!/bin/bash

module load gcc &&
module load intel/15.0.2 &&
module load python/2.7.8 &&

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
cp scores.txt scores2.txt || true &&
rm scores.txt || true &&
cat scores.*.txt scores2.txt > scores.txt || true &&
rm scores2.txt || true &&
rm scores.*.txt || true &&
rm eligible_ecs.*.txt || true &&
rm master_pipeline.*.sh || true &&
rm GenerateAIQROScores* || true &&
rm run_master_pipelines_on_scinet.*.sh || true &&
python 0_get_eligible_ecs.py $1 &&
python 0_create_run_pipeline_forall_ec.py $1 &&
bash 0_create_and_queue_all_master_pipelines.sh $1 &&
wait
