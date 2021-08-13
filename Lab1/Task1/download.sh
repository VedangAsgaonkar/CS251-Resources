#!/bin/bash
# Assignment code of pair: Prathamesh and Vedang

if [ $# -ne 2 ] 
then
	tput bold 
	echo Usage: bash download.sh \<link to directory\> \<cut-dirs arguement\>
	exit 1
fi
wget -R ".html,.html.tmp" -nH --cut-dirs="$2" -r -np $1 -q
dirname=$( basename $1 )
if [ $dirname != mock_grading ]
then
	mv $dirname mock_grading
fi
