#!/bin/bash

touch marksheet.csv
touch distribution.txt

cd organised
roll_nos=$( ls )

for rollno in $roll_nos
do
    cd $rollno

    mkdir student_outputs
    filename=$( ls | egrep '.cpp' )
    g++ $filename -o executable 2>/dev/null 
    inputs=$( ls ../../mock_grading/inputs | cut -d '.' -f 1 )
    total=0
    for input in $inputs
    do
        ( timeout 5s ./executable < ../../mock_grading/inputs/$input.in > ./student_outputs/$input.out 2>/dev/null | 2>/dev/null )

        difference=$( diff ../../mock_grading/outputs/$input.out ./student_outputs/$input.out | wc -l )
       
        if [ $difference -eq 0 ]
        then
            (( total++ ))  
        fi
    done
    cd ..
    echo "$rollno,$total" >> ../marksheet.csv
done

cd ..

marks=$( cat marksheet.csv | cut -d ',' -f 2 | sort -r -n )
for mark in $marks
do
    echo $mark >> distribution.txt
done