from Bio import SeqIO

fasta_sequences = SeqIO.parse(open(input_file),'fasta')

with open(output_file) as out_file:
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
        new_sequence = some_function(sequence)
        write_fasta(out_file)def divider(file_x):
    fasta_sequences = fasta_generator(input_file) # The function I miss

with open(output_file) as out_file:
    for fasta in fasta_sequences:
        name, sequence = fasta
        new_sequence = some_function(sequence)
        write_fasta(out_file) # Function defined elsewhere
