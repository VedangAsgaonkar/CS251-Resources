#!/bin/bash
n=$1
awk '
BEGIN{
}
FILENAME == "word_token_mapping.txt" {
		token[$2]=$1
	}
FILENAME != "word_token_mapping.txt" && $1 == 0{
	num_tokens = split($2 , token_id ,"|")
	for(i =1 ; i<=num_tokens ; i++){
		freq[token_id[i]]++
	} 
}
END{
	for( i in  freq){
		print token[i] " " freq[i] 
	}

}' FS="-" word_token_mapping.txt FS=":" sample.txt | sort -k2r,2 -k1,1  | awk -v n="$n" ' 
BEGIN{}
NR>= 1 && NR <= n{print $1}
' > ham.txt
awk '
BEGIN{
}
FILENAME == "word_token_mapping.txt" {
		token[$2]=$1
	}
FILENAME != "word_token_mapping.txt" && $1 == 1{
	num_tokens = split($2 , token_id ,"|")
	for(i =1 ; i<=num_tokens ; i++){
		freq[token_id[i]]++
	} 
}
END{
	for( i in  freq){
		print token[i] " " freq[i] 
	}

}' FS="-" word_token_mapping.txt FS=":" sample.txt | sort -k2r,2 -k1,1  | awk -v n="$n" ' 
BEGIN{}
NR>= 1 && NR <= n{print $1}
' > spam.txt