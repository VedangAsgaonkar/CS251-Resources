#!/bin/bash

awk '
    BEGIN{
        c = 0;
        ORS="";
        OFS="";
    }
    {
        for(i=1 ; i<= NF; i++)
        {
           e=" ";
           if(i==NF){
               e="\n";
           }
           if($i in words){
               print words[$i],e;
           }
           else{
               words[$i] = c;
               c++;
               print words[$i],e;
           }
        }
    }
' sample.txt >output.txt
