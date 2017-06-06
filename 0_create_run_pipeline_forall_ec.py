import sys

def main():
	max_serial_num = sys.argv[1]

	for i in range(1, int(max_serial_num) + 1):
		with open("eligible_ecs." + str(i) + ".txt", "r") as eligible:
			with open("master_pipeline." + str(i) + ".sh", "w") as master:
				master.write("#!/bin/bash\n")
				master.write("chmod +x 0_run_pipeline_for_one_ec.sh &&\n")

				for line in eligible:
					line = line.rstrip("\n")

					master.write("./0_run_pipeline_for_one_ec.sh " + line + " " + str(i) + " &&\n")

				master.write("wait")

if __name__ == "__main__":
	main()
