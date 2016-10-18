#!/bin/bash

name=$1
echo $name

# time blastn -db /blast/blastdb/nt -evalue 1e-05 -num_descriptions 100 -num_alignments 100 -query /blast/input/$name -out /blast/output/$name.blast_output -num_threads 8 &

( time blastn -db /blast/blastdb/nt -evalue 1e-05 -num_descriptions 100 -num_alignments 100 -query /blast/input/$name -out /blast/output/$name.blast_output -num_threads 8 ) 2> /blast/output/$name.time.txt