#!/usr/bin/python

import sqlite3
import subprocess
import sys

"""Script to upload old DETECT text files into databases using sqlite3"""

class ProgressMeter:
	def __init__(self,job_size):
		self.job_size = float(job_size)
		self.steps_done = float(0)

	def step (self):
		self.steps_done+= 1
		self.__show__(self.steps_done)

	def update (self, step):
		self.steps_done = step
		self.__show__(self.steps_done)

	def __show__ (self,complete):
		sys.stdout.write("Working: {:.2%} done\r".format(complete/self.job_size))
		sys.stdout.flush()

	def done(self):
		clear = chr(27) + '[2K' + chr(27) + '[G'
		sys.stdout.write(clear + "Job complete!\n")
		sys.stdout.flush()

def wc_count(filename):
	process = subprocess.Popen(('wc', '-l', filename),stdout=subprocess.PIPE)
	stdout,stderr =  process.communicate()
	return float(stdout.split()[0])

if __name__=="__main__":
	detect_files = ["density-pos.out","density-neg.out","swissProt2EC_ids-30+.mappings","prior_probabilities.out"]

	job_size = sum([wc_count(name) for name in detect_files])
	meter = ProgressMeter(job_size)
	lines_done = 0
	#process meter will be updated after every <update_time> lines written to DB
	update_time = 2048
	
	connection = sqlite3.connect('detect.db')
	with connection:
	
		cursor = connection.cursor()
		
		#get positives
		cursor.execute("create table positive_densities(ec text, score numeric, density numeric, primary key (ec,score))")
		cursor.execute("create index positive_index on positive_densities(ec,score)")
	
		for line in open('density-pos.out'):
			if not "EC" in line and not "NA" in line:
				ec, score, density = line.rstrip("\n").split(",")
				density = density.lstrip()
				cursor.execute("insert into positive_densities values('{}',{},{})".format(ec,score,density))
	
			lines_done += 1
			if lines_done % update_time == 0:
				meter.update(lines_done)
	
		#get negatives
		cursor.execute("create table negative_densities(ec text, score numeric, density numeric, primary key (ec,score))")
		cursor.execute("create index negative_index on negative_densities(ec,score)")
	
		for line in open('density-neg.out'):
			if not "EC" in line and not "NA" in line:
				ec, score, density = line.rstrip("\n").split(",")
				density = density.lstrip()
				cursor.execute("insert into negative_densities values('{}',{},{})".format(ec,score,density))
			
			lines_done += 1
			if lines_done % update_time == 0:
				meter.update(lines_done)
	
		#get uniprot-ec mappings
		cursor.execute("create table swissprot_ec_map(swissprot_id text, ec text, primary key (swissprot_id))")
		cursor.execute("create index map_index on swissprot_ec_map(swissprot_id)")

		for line in open("swissProt2EC_ids-30+.mappings"):
			
			if not "EC" in line:
				swissprot_id, ec = line.rstrip("\n").split(",")
				cursor.execute("insert into swissprot_ec_map values('{}','{}')".format(swissprot_id,ec))
		
			lines_done += 1
			if lines_done % update_time == 0:
				meter.update(lines_done)

		#get prior probabilities
		cursor.execute("create table prior_probabilities(ec text, probability numeric, primary key (ec))")
		cursor.execute("create index prior_index on prior_probabilities(ec)")

		for line in open("prior_probabilities.out"):
				
			if not "EC" in line:
				ec, num_proteins, probability = line.rstrip("\n").split(",")
				cursor.execute("insert into prior_probabilities values('{}',{})".format(ec,probability))

			lines_done += 1
			if lines_done % update_time == 0:
				meter.update(lines_done)


	meter.done()
