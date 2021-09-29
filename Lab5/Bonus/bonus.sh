#!/bin/bash

sed '
s/ $//g
' bonus_sample_input.txt | awk '{ sub("\r$", ""); print }' > temp.txt

awk '
function char_to_int(x){
    if(x=="a"){
        return 10;
    }
    else if(x=="b"){
        return 11;
    }
    else if(x=="c"){
        return 12;
    }
    else if(x=="d"){
        return 13;
    }
    else if(x=="e"){
        return 14;
    }
    else if(x=="f"){
        return 15;
    }
    else{
        return x+0;
    }
}
function int_to_char(x){
    if(x==10){
        return "a";
    }
    else if(x==11){
        return "b";
    }
    else if(x==12){
        return "c";
    }
    else if(x==13){
        return "d";
    }
    else if(x==14){
        return "e";
    }
    else if(x==15){
        return "f";
    }
    else{
        return x;
    }
}
BEGIN{
    OFS="";
    ORS="";
}
        (NR%3==2){
            base1=$1+0;
            base2=$2+0;
        }
        (NR%3==0){
            num1 = 0;
            for(i=1 ; i<=NF ; i++){
                    num1 = num1*base1+char_to_int($i);
            }
        }
        (NR%3==1 && NR!=1){
            num2 = 0;
            for(i=1 ; i<=NF ; i++){
                num2 = num2*base1+char_to_int($i);
            }
            num = num1 + num2;
            cnt = 0;
            while(num>0){
                arr[cnt] = int_to_char(num%base2);
                num = int(num/base2);
                cnt ++ ;
            }
            cnt--;
            while(cnt>0){
                print arr[cnt] " ";
                cnt--;
            }            
            print arr[cnt] "\n";
        }
' temp.txt > output.txt

rm temp.txt