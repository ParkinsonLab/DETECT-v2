DETECT_TOOL=/absolute/file/path/to/detect_folder/detect.py

export PATH=/absolute/file/path/to/detect_folder/:$PATH # add the path to the folder containing DETECT
export PATH=/usr/local/bin/:$PATH # add the path to emboss to PATH

python $DETECT_TOOL sample.fasta --output_file sample.out --top_predictions_file sample.top --num_threads 8 --fbeta_file sample.f1.out --beta 1
