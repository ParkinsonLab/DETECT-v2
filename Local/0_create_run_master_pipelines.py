import sys

def main():
	batch_num = sys.argv[1]
	start = sys.argv[2]
	end = int(start) + 8

	with open("run_master_pipelines." + batch_num + ".sh", "w") as master:
		header = ["#!/bin/bash"]

		master.writelines("%s\n" % line for line in header)

		for i in range(int(start), end):
			master.write("chmod +x master_pipeline.%s.sh\n" % str(i))

		master.write("\n")

		for i in range(int(start), end):
			master.write("(./master_pipeline.%s.sh) &\n" % str(i))

		master.write("wait")

if __name__ == "__main__":
	main()
