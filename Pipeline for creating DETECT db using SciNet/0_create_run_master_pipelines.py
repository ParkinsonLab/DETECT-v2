import sys

def main():
	serial_num = sys.argv[1]
	start = sys.argv[2]
	end = int(start) + 8

	with open("run_master_pipelines_on_scinet." + serial_num + ".sh", "w") as master:
		header = ["#!/bin/bash", "#PBS -l nodes=1:ppn=8,walltime=48:00:00", "#PBS -N GenerateIQROScores-%s\n" % serial_num, 
			"cd $PBS_O_WORKDIR", "export PATH=$PATH:/home/j/jparkins/ctorma/emboss/bin/\n", 
			"module load gcc", "module load intel/15.0.2", "module load python/2.7.8", "module load blast", "module load extras\n"]

		master.writelines("%s\n" % line for line in header)

		for i in range(int(start), end):
			master.write("chmod +x master_pipeline.%s.sh\n" % str(i))

		master.write("\n")

		for i in range(int(start), end):
			master.write("(./master_pipeline.%s.sh) &\n" % str(i))

		master.write("wait")

if __name__ == "__main__":
	main()
