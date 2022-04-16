# femMCategoriser
A tool to assign taxonomy to bacterial genomes isolated from the female genital tract based on the FemMCat taxonomy

Requirements:
>fastANI (tested with version 1.33)

>SGB representative genome database (498Mb compressed)

>femMcategoriser requires 20GB RAM

* You will need to run this script to download the representative genome database from Zenodo
~~~
./download_refDB.py
~~~

* Help message
~~~
./femMCategoriser.py -h
   Options:
      -h, --help   show this help message and exit
      -q QUERIES   path to directory with query genomes in FASTA format
      -n NUMCORES  number of cores (default 6)
~~~

* This repo has a small test case (takes about 3 mins with 6 nodes) which you can run with this:

~~~
./femMCategoriser.py -q query_genomes_EXAMPLE -n 6
~~~

* The genome assignments can be found in "genome_species_SGB_assignment.tab"

Enjoy, Matt :-)
