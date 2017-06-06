#!/bin/bash

total=$1
let "max_serial_num=total/8"

input_counter=1
for i in `seq 1 $max_serial_num`;
        do
		python 0_create_run_master_pipelines.py $i $input_counter &&
		qsub run_master_pipelines_on_scinet.$i.sh &&
		let "input_counter+=8"
        done   
