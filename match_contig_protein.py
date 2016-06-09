#!/usr/bin/env python
import re

InFileName = 'ClassA2.txt'
InFileName2 = '761_Clytia_GPCR_seqs.fas'

InFile = open( InFileName, 'r' )
InFile2 = open (InFileName2, 'r' )

OutFileName_ClassA = "ClassA_fasta.fas"
OutFileA = open (OutFileName_ClassA, 'a')

def Contig (ContigString1 , ContigString2):	

	StringClassA = '(>\w+)(\t.*\n.+)'
	String761 = '(>\w+)\n(.+)'

	ResultA	= re.findall( StringClassA, ContigString1 )
	Result761 = re.findall( String761, ContigString2 )

	contig_nameA = ResultA.group (1)
	contig_name761 = Result761.group (1)
	protein_seq = Result761.group (2)




for Line in InFile2:
	Line = Line.strip()

	if 
		
		Line = Line + "Class A \n"
		print (Line)
		
		OutFileA.write (Line)

	

InFile.close()