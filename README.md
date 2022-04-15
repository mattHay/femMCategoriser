# femMCategoriser
A tool to assign taxonomy to bacterial genomes isolated from the female genital tract based on the FemMCat taxonomy

20G RAM memory with 6 cores it takes around 5 mins to query 6 genomes

./femMCategoriser.py -h

Options:
  -h, --help   show this help message and exit
  -q QUERIES   directory path with query genomes in FASTA format
  -n NUMCORES  number of cores (default 6)

Ref database is 489Mb

Requires fastANI (tested with version 1.33)
