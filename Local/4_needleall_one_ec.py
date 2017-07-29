from Bio import SeqIO
from Bio.Emboss.Applications import NeedleallCommandline
import sys

# To run: python 4_needleall_one_ec.py -target_ec -serial_num -prepared_filename
# Replace -ec with ec of pairs results file to extract pairs from, serial_num
# with the serial number of the partition that this belongs to,
# and -prepared_filename with the fasta filename of the prepared data.

def create_dict_qids_to_hids(filename):
	all_qids_to_hids = {}

	with open(filename, "r") as pairings_file:
		for line in pairings_file:
			line = line.rstrip("\n").split(",")

			if line[0] in all_qids_to_hids:
				all_qids_to_hids[line[0]].append(line[1])
			else:
				all_qids_to_hids[line[0]] = [line[1]]

	return all_qids_to_hids

def write_to_fasta(record_iter, file_name):
	with open(file_name, "a") as output_handle:
		SeqIO.write(record_iter, output_handle, "fasta")

def needleall(set1, set2, qid, serial_num):
	needleall_cline = NeedleallCommandline(asequence=set1, bsequence=set2, gapopen=10, gapextend=0.5, outfile=qid + "." + serial_num  + ".needleall")
	needleall_cline()

def main():
	target_ec = sys.argv[1]
	pairings_filename = target_ec + "_unique_pairs.txt"
	qids_to_hids = create_dict_qids_to_hids(pairings_filename)

	seq_filename = sys.argv[3]
	ids_to_recs = SeqIO.index(seq_filename, "fasta")

	serial_num = sys.argv[2]

	for qid in qids_to_hids:
		if qid != "Q8WZ42" and qid != "A2ASS6":
			query_filename = qid + "." + serial_num + ".query.fasta"
			hits_filename = qid + "." + serial_num  + ".hits.fasta"

			write_to_fasta(ids_to_recs[qid], query_filename)
			write_to_fasta((ids_to_recs[hid] for hid in qids_to_hids[qid] if hid != "Q8WZ42" and hid != "A2ASS6"), hits_filename)

			needleall(query_filename, hits_filename, qid, serial_num)

	print(target_ec + " has been needled...")

if __name__ == "__main__":
	main()