#!/usr/bin/env python
import re

InFileName = 'ClassC2.txt'
InFileName2 = '761_Clytia_GPCR_seqs.fas'

InFile = open( InFileName, 'r' )
InFile2 = open (InFileName2, 'r' )

OutFileName_ClassA = "ClassC_fasta.fas"
OutFileA = open (OutFileName_ClassA, 'a')



def Header_set (file):
	H_set = set()

	StringClassA = '(>\w+)(\t.*)'

	for Line in file:

		ResultA	= re.search( StringClassA, Line )

		contig_nameA = ResultA.group (1)

		H_set.add (contig_nameA)

	return H_set

H_set = Header_set(InFile)

#print (H_set)

String761 = '(>\w+)\n(.+)'
Result761 = re.findall( String761, InFile2.read() )

for result in Result761:

	contig_name761 = result [0]
	protein_seq = result [1]


	if contig_name761 in H_set:
		
		print (contig_name761 + '\n' + protein_seq)
		
		OutFileA.write (contig_name761 + '\n' + protein_seq + '\n')

	

InFile.close()


'''
def Contig (ContigString1 , ContigString2):	

	StringClassA = '(>\w+)(\t.*\n.+)'
	String761 = '(>\w+)\n(.+)'

	ResultA	= re.findall( StringClassA, ContigString1 )
	Result761 = re.findall( String761, ContigString2 )

	contig_nameA = ResultA.group (1)
	contig_name761 = Result761.group (1)
	protein_seq = Result761.group (2)

'''