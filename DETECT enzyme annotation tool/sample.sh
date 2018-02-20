DETECT_FOLDER=/absolute/file/path/to/detect_folder
DETECT_TOOL=${DETECT_FOLDER}/detect.py

export PATH=${DETECT_FOLDER}/:$PATH # add the path to the folder containing DETECT
export PATH=/usr/local/bin/:$PATH # add the path to emboss to PATH

python $DETECT_TOOL sample.fasta --output_file sample.out --top_predictions_file sample.top --num_threads 8 --fbeta_file sample.f1.out --beta 1
