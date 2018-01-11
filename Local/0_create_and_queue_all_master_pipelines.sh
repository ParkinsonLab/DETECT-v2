#!/bin/bash

max_serial_num=$1
let "max_batch_num=max_serial_num/8"

input_counter=1
for i in `seq 1 $max_batch_num`;
        do
		python 0_create_run_master_pipelines.py $i $input_counter &&
		let "input_counter+=8"
        done 

for i in `seq 1 $max_batch_num`;
        do
		bash run_master_pipelines.$i.sh &
		wait
        done  
