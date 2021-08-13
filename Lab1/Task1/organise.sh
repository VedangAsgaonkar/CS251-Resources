#!/bin/bash

mkdir organised

rollnos=$( cat ./mock_grading/roll_list )
names=$(ls mock_grading/submissions | cut -d "/" -f 3 )

cd ./organised

for rollno in $rollnos
do
    mkdir $rollno
    cd $rollno
    for file in $(ls ../../mock_grading/submissions | cut -d "/" -f 3 | egrep "^$rollno" )
    do
        ln -s ../../mock_grading/submissions/$file $file
    done   
    cd ..
done



