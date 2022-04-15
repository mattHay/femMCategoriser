#Make jens ANI tab
import re

taxa = {}
for ent in open("assignment_to_all_genomes_12August2020.tab", "r"):
    ent = ent.rstrip().split("\t")
    
    taxa[ent[0].replace("-", "_")] = [ent[1], ent[2]]

output = open("genome_species_SGB_assignment.tab", "w")
seen = []
assigned = []
for ent in open("ANI_query_reps.tsv", "r"):
    ent = ent.rstrip().split("\t")

    genome1 = ent[0].split("/")[-1].split("-FIN")[0].split(".f")[0].split("-SP")[0].replace("-", "_")
    genome2 = ent[1].split("/")[-1].split("-FIN")[0].split(".f")[0].split("-SP")[0].replace("-", "_")

    ANI = 100 - float(ent[2])
    seen.append(genome1)

    if ANI < 5 and re.search("new", taxa[genome2][1]): 
        assigned.append(genome1)
        output.write(genome1 + "\t" + taxa[genome2][0] + "\tnew_species\t" + str(ANI) + "\n")

    elif ANI < 5:
        assigned.append(genome1)
        output.write(genome1 + "\t" + taxa[genome2][0] + "\t" + taxa[genome2][1] + "\t" + str(ANI)+ "\n")

output.close()

print("\n".join(list(set([x for x in seen if x not in assigned]))))
