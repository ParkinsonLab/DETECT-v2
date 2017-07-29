from Bio import SeqIO
import sys

# To run: python 0_get_eligible_ecs.py -partitions -fasta_filename -processed_filename
# Replace -partitions with number of eligible ec files you want, fasta_filename with name
# of your prepared sequence data fasta, and processed_filename with a text file where each
# row is an ec that has already been processed (suggest processed.txt, as that is the default
# output by other steps of this pipeline).

def create_list_ec_count_over_twenty_nine(sequence_iterator, processed):
	ec_count = {}

	for record in sequence_iterator:
		description = record.description.split(";")
		qid = description[0].split()[0]
		ec = "no_ec"
		
		for e in description:
			if "EC=" in e:
				ec = e.split()[0][3:]
				break

		if ec in ec_count and ec != "no_ec":
			ec_count[ec]+= 1
		elif ec != "no_ec" and ec not in processed:
			ec_count[ec] = 1

	return [ec for ec in ec_count if ec_count[ec] >= 30]

def get_processed(processed_filename):
	processed = []

	with open(processed_filename, "r") as ineligible:
		for line in ineligible:
			processed.append(line.rstrip("\n"))

	return processed

def main():
	fasta_file_name = sys.argv[2]

	input_handle = open(fasta_file_name, "rU")

	input_seq_iterator = SeqIO.parse(input_handle, "fasta")

	processed = get_processed(sys.argv[3])

	eligible_ecs_with_over_twenty_nine_members = create_list_ec_count_over_twenty_nine(input_seq_iterator, processed)

	input_handle.close()

	partitions = int(sys.argv[1])

	partition_size = len(eligible_ecs_with_over_twenty_nine_members) / partitions

	for i in range(1, partitions + 1):
		output_filename = "eligible_ecs." + str(i) + ".txt"

		with open(output_filename, "w") as out:
			out.writelines("%s\n" % ec for ec in eligible_ecs_with_over_twenty_nine_members[(i - 1) * partition_size:i * partition_size])

			if i == partitions:
				out.writelines("%s\n" % ec for ec in eligible_ecs_with_over_twenty_nine_members[i * partition_size:])

if __name__ == "__main__":
	main()
