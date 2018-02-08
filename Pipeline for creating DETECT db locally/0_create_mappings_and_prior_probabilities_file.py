from Bio import SeqIO
import sys

# To run: python 0_create_mappings_and_prior_probabilities_file.py -fasta_filename
# Replace -fasta_filename with name of your prepared sequence file.

def create_dict_ids_to_ecs_and_ec_count(sequence_iterator):
	all_ids_to_ecs = {}
	ec_count = {}

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

		if ec in ec_count and ec != "no_ec":
			ec_count[ec]+= 1
		elif ec != "no_ec":
			ec_count[ec] = 1

	return (all_ids_to_ecs, ec_count)

def main():
	mappings_filename, prior_probs_filename = "swissProt2EC_ids-30+.mappings", "prior_probabilities.out"

	with open(mappings_filename, "w") as mappings:
		with open(prior_probs_filename, "w") as prior_probs:
			fasta_filename = sys.argv[1]
			fasta_handle = open(fasta_filename, "rU")
			fasta_iterator = SeqIO.parse(fasta_handle, "fasta")

			all_ids_to_ecs, ec_count = create_dict_ids_to_ecs_and_ec_count(fasta_iterator)

			to_write_to_file = []

			for sid in all_ids_to_ecs:
				if all_ids_to_ecs[sid] != "no_ec" and ec_count[all_ids_to_ecs[sid]] >= 30:
					to_write_to_file.append(",".join([sid, all_ids_to_ecs[sid]]))

			mappings.writelines("%s\n" % item for item in to_write_to_file)

			to_write_to_file = []

			for ec in ec_count:
				if ec_count[ec] >= 30:
					to_write_to_file.append(",".join([ec, str(ec_count[ec]), str(float(ec_count[ec]) / len(all_ids_to_ecs))]))

			prior_probs.writelines("%s\n" % item for item in to_write_to_file)

if __name__ == "__main__":
	main()
