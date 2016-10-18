#Create folder
mkdir blast blast_db input output

#Download BLAST+
cd blast
wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.3.0+-x64-linux.tar.gz
tar -zxvf ncbi-blast-2.3.0+-x64-linux.tar.gz
cd ..

#Download NT
blast_db
wget http://www.ncbi.nlm.nih.gov/BLAST/docs/update_blastdb.pl
perl update_blastdb.pl nt
#extract files
for file in *.tar.gz; do tar -zxf $file; done
cd ..

#split fasta file in 150 parts
cd input
sudo pip install pyfasta
pyfasta split -n 150 original.fasta
cd ..


##### START - This part should be executed for each aws instance (for 1...150)

#transfer files to new instance
scp -r blast blast_db input output new_instance:~/
ssh new_instance

#runblast in new_instance 01
./blast/ncbi-blast-2.3.0+/bin/blastn -db blast_db/nt -evalue 1e-05 -query input/original.00.fasta -out output/original.00.blast_output -num_threads 24
#runblast in new_instance 02
./blast/ncbi-blast-2.3.0+/bin/blastn -db blast_db/nt -evalue 1e-05 -query input/original.01.fasta -out output/original.01.blast_output -num_threads 24
# and so on ... 03, 04, 05 ... 150 (input/original.149.fasta)

# after it ends, transfer blast results to the original instance
scp -r output original_instance:~/
exit
##### END 

# at the original instance merge all 150 blast results into one
cd output
cat *.blast_output > all_blast_output.out 