# Neptune Computational Biology - Final Project

## Guidelines - you can delete this section before submission

This repository is a stub for your final project. Fork it, develop your project, and submit it as a pull request. Edit/ delete the text in this readme as needed.

Some guidelines and tips:

- Use the stubs below to write up your final project.

- For information on formatting text files with markdown, see https://guides.github.com/features/mastering-markdown/ . You can use markdown to include images in this document by linking to files in the repository, eg `![Figure 1](./Figure1.png?raw=true)`.

- The project must be entirely reproducible. In addition to the results, the repository must include all the data (or links to data) and code needed to reproduce the results.

- If you are working with unpublished data that you would prefer not to publicly share at this time, please contact me to discuss options. In most cases, the data can be anonymized in a way that putting them in a public repo does not compromise your other goals.

- Paste references (including urls) into the reference section, and cite them with the general format (Smith at al. 2003).

- Commit and push often as you work.

OK, here we go.

# Gonzalo's project - Clytia hemisphaerica GPCR complement and classification. Phylogeny of a cnidarian Neuropeptide Receptor.

## Introduction and Goals

The goal of my project is to answer the question:

Find all GPCRs of each class in Clytia (from an existing excell table and Transcriptome FASTA file) and get a good dataset of GPCRs to do a phylogeny of a specific Clytia Neuropeptide GPCR. 

"I should not make this data available in public repositories yet"



The methods I will use to do this are...

-TextWrangling, concatenate, python scripts to authomatise what I would do with regular expressions...


1) Use commands like "grep" and ">" to create new files with the specific PFAM information of GPCR family for each of the contigs (Class A, B, C and other). "Max recommended me to also do this in Python"

2) Use a Python script to create FASTA files with the contig name and protein sequence for each of the main classes of GPCRs. I will use the PFAM information files and the Clytia transcriptome for this. 

3) Run cd-hit to get rid of redundancy over 90% similarity for each of the FASTA files of each GPCR class. 

4) Count the number of GPCRs of each class in Clytia. 

Optional:

- Concatenate all the files to a single big file with all Clytia GPCRs.
- With a Python script retrieve all the rows from an excell table with mapping information in different Clytia tissues and life stages, using the contig names as bait.
- Do a heat map to check visually if a specific class is more expressed than another in a specific tissue/life stage.

5) Use my receptor of interest (JOMP Receptor) as a query to retrieve different similar neuropeptide GPCRs in Cnidaria, using different datasets.

6) Do a cluster map of al Clytia class A GPCRs, retrieved cnidarian good hits of JOMP receptor, and other known Bilaterian neuropeptide GPCRs.

7) With the best, closest-related sequences, build a phylogenetic tree (ML). 


The data I will use are 
- My own data
- Data publicly available at Compagen
- Recently assembled unpublished transcriptomes from hydrozoans (Dunn and Léclere)



## Methods

The tools I used were... See analysis files at (links to analysis files).

## Results

![Figure 1](./Figure1.png?raw=true)

In Figure 1...

## Discussion

These results indicate...

The biggest difficulty in implementing these analyses was...

If I did these analyses again, I would...

## References


