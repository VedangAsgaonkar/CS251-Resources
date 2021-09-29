#!/bin/bash

filename=$1
start=$2
end=$3
awk -v start=$start -v end=$end '
    function get_time(time_string){
        num_parts = split(time_string,parts,":")
        hh = parts[1]+0;
        mm = parts[2]+0;
        ss = parts[3]+0;
        t = hh*3600 + mm*60 + ss;
        return t;
    }
    function to_time(time){
        hh = int(time/3600);
        mm = int((time-hh*3600)/60);
        ss = int(time-hh*3600-mm*60);
        if(hh<10){
            h = sprintf("0%d",hh);
        }
        else{
            h = sprintf("%d",hh);
        }
        if(mm<10){
            m = sprintf("0%d",mm);
        }
        else{
            m = sprintf("%d",mm);
        }
        if(ss<10){
            s = sprintf("0%d",ss);
        }
        else{
            s = sprintf("%d",ss);
        }
        return h ":" m ":" s;
    }
    BEGIN{
        FS = "\t";
        OFS = "\t";
        start_time = get_time(start);
        end_time = get_time(end);
    }
    {
        if(NR>1){
            split($3,parts,", ");
            time=get_time(parts[2]);
            if(! $1 in person){
                if(time<start_time){
                    time=start_time;
                }
                person[$1] = end_time-time;
            }
            else{
                if(time<start_time){
                    time=start_time;
                }
                if($2=="Joined"){
                    person[$1] += end_time-time;
                }
                else if($2=="Left"){
                    person[$1] -= end_time-time;
                }
            }
        }       
    }
    END{
        for(p in person){
            print p, to_time(person[p]) | "sort";
        }
    }
' $filename > output.txt
