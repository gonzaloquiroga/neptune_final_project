#!/usr/bin/env python
import re

InFileName = 'ClassA2.txt'
InFileName2 = 'ClassB2.txt'
InFileName3 = 'ClassC2.txt'
InFileName4 = 'ClassOther2.txt'

InFileName5 = '761_Clytia_GPCR_seqs.fas'

InFile = open( InFileName, 'r' )
InFile2 = open (InFileName2, 'r' )
InFile3 = open (InFileName3, 'r' )
InFile4 = open (InFileName4, 'r' )

InFile5 = open (InFileName5, 'r' )

OutFileName_ClassA = "ClassA_fasta.fas"
OutFileA = open (OutFileName_ClassA, 'a')
OutFileName_ClassB = "ClassB_fasta.fas"
OutFileB = open (OutFileName_ClassB, 'a')
OutFileName_ClassC = "ClassC_fasta.fas"
OutFileC = open (OutFileName_ClassC, 'a')
OutFileName_ClassO = "ClassOther_fasta.fas"
OutFileO = open (OutFileName_ClassO, 'a')


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

def fasta (file2, searchset):

	String761 = '(>\w+)\n(.+)'
	Result761 = re.findall( String761, InFile2.read() )

	for result in Result761:

		contig_name761 = result [0]
		protein_seq = result [1]


		if contig_name761 in searchset:
		
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