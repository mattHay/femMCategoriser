#!/usr/bin/env python

############################
#Assign SGB and species_name annotations to a genome based on the femMCat taxonomy
import re
import glob
import subprocess
import os
from optparse import OptionParser

############################
#Command line arguments for the location of the query genomes and number of cores available
parser = OptionParser()
parser.add_option("-q", dest = "queries", type = "string", help = "directory path with query genomes in FASTA format")
parser.add_option("-n", dest = "numCores", type = "string", help = "number of cores (default 6)", default="6")
(ops, args) = parser.parse_args()

queries = ops.queries
numCores = ops.numCores

############################
#Make a file which contains the path of all the query sequences
output = open("queryGenomes.tab", "w")

for ent in glob.glob(queries + "/*"):

    output.write(ent + "\n")
    
output.close()

#Run FastANI between query sequences and SGB representative genomes
subprocess.call("fastANI --ql queryGenomes.tab --rl repGenomes.tab -o ANI_query_reps.tsv -t %s" % (numCores), shell = True)

############################
#Assign SGB taxonomy based on distance to rep genome
output = open("genome_species_SGB_assignment.tab", "w")
output.write("query_genome\tSGB_assignment\tspecies_name\tANI_to_rep_genome\n")
assigned = []
seen = []

for ent in open("ANI_query_reps.tsv", "r"):
    ent = ent.rstrip().split("\t")

    genome1 = ent[0].split("/")[-1]
    seen.append(genome1)

    #The taxonomic assignment is coded in the representative genome names
    taxonomy = ent[1].split("/")[-1].split("_link_")

    #These are uSGBs, they are defined by a set of genomes but don't have a binomial name
    if re.search("new", taxonomy[1]):

        taxonomy[1] = "uSGB"

    ANI = 100 - float(ent[2])

    #To assign an SGB the query must be withint 5% average nucleotide ID (ANI) of a rep genome
    if ANI < 5: 

        assigned.append(genome1)
        output.write(genome1 + "\t" + taxonomy[0] + "\t" + taxonomy[1] + "\t" + str(ANI)[:3] + "\n")

#Write query genomes which did not get assigned an SGB
seen = list(set(seen))
for ent in seen:

    if ent not in assigned:

        output.write(ent + "\tno_assignment\tno_assignment\tNA\n")

output.close()

os.remove("queryGenomes.tab")
os.remove("ANI_query_reps.tsv")
