from Bio import SeqIO
import sys

def not_fragment(description):
	if "Fragment" not in description:
		return True
	return False

def has_less_than_one_ec(description):
	if description.count("EC=") <= 1:
		return True
	return False

def ec_complete(description):
	if ".-" not in description and ".n" not in description:
		return True
	return False

def check_target_ec(description, target_ec):
	if target_ec in description:
		return True
	return False

def write_to_fasta(record_iter, file_name):
	output_handle = open(file_name, "w")
	count = SeqIO.write(record_iter, output_handle, "fasta")
	output_handle.close()

	print "Found %i eligible records" % count

def main():
	target_ec = sys.argv[1]

	file_name = "uniprot_sprot.dat"
	input_handle = open(file_name, "rU")

	input_seq_iterator = SeqIO.parse(input_handle, "swiss")

	detect_worthy_seq_iterator = (record for record in input_seq_iterator \
		if not_fragment(record.description) \
		if has_less_than_one_ec(record.description) \
		if ec_complete(record.description) \
		if check_target_ec(record.description, target_ec))

	output_file_name = target_ec + ".fasta"
	write_to_fasta(detect_worthy_seq_iterator, output_file_name)

	input_handle.close()

if __name__ == "__main__":
	main()
