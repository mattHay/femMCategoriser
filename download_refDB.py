#!/usr/bin/env python
#Download refernce database
import os

print("downloading representative genomes")
os.system("wget https://zenodo.org/record/6464921/files/genome_representatives.tar.gz")

print("decompressing and unpacking")
os.system("tar xfz genome_representatives.tar.gz")
os.remove("genome_representatives.tar.gz")
