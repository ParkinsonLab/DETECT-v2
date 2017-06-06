import sys

def get_pairs(file_name):
	pairs = set()

	with open(file_name) as f:
		for line in f:
			if line[0] != "#":
				blast_record = line.split("\t")
				if blast_record[0] != blast_record[1] and float(blast_record[7]) >= 50.0:
					pair = blast_record[0] + "," + blast_record[1]
					pairs.add(pair)

	return pairs

def write_list_to_file(input_file_name, pairs):
    output_file_name = input_file_name[0:-3] + "_unique_pairs.txt"
    
    with open(output_file_name, 'w') as f:
		f.writelines("%s\n" % pair for pair in pairs)

def main():
	ec = sys.argv[1]
	file_name = ec + ".bl"
	pairs = get_pairs(file_name)
	print("Writing to file...")
	write_list_to_file(file_name, pairs)

if __name__ == "__main__":
	main()
