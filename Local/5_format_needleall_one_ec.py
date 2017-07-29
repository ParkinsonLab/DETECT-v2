import sys
from Bio import SeqIO

# To run: python 5_format_needleall_one_ec.py -target_ec -prepared_filename
# Replace -ec with ec of needle results file to format
# and -prepared_filename with the fasta filename of the prepared data.

def create_dict_ids_to_ecs(sequence_iterator):
	all_ids_to_ecs = {}

	for record in sequence_iterator:
		description = record.description.split(";")
		qid = description[0].split()[0]
		ec = ""

		for e in description:
			if "EC=" in e:
				ec = e.split()[0][3:]
				break
			else:
				ec = "no_ec"

		all_ids_to_ecs[qid] = ec

	return all_ids_to_ecs

def main():
	fasta_filename = sys.argv[2]
	fasta_handle = open(fasta_filename, "rU")
	fasta_iterator = SeqIO.parse(fasta_handle, "fasta")
	all_ids_to_ecs = create_dict_ids_to_ecs(fasta_iterator)

	target_ec = sys.argv[1]
	needleall_filename = target_ec + ".needleall.final"

	formatted_lines = []
	batchsize = 1000000
	
	with open(needleall_filename, "r") as needled:
		with open(target_ec + "_aligned_unique_pairs.txt", "w") as aligned:
			for line in needled:
				if "#" not in line and line != "\n":
					line = line.split(" ")

					if all_ids_to_ecs[line[0]] == all_ids_to_ecs[line[1]]:
						formatted_lines.append(",".join(["p", line[-1][1:-2]]))
					else:
						formatted_lines.append(",".join(["n", line[-1][1:-2]]))

					if len(formatted_lines) == batchsize:
						aligned.writelines("%s\n" % l for l in formatted_lines)
						del formatted_lines[:]

			aligned.writelines("%s\n" % l for l in formatted_lines)

	print(target_ec + " needleall file has been formatted...")

if __name__ == "__main__":
	main()
