#!/bin/bash

# Remove empty samples i.e., word length =0
# Make sure text has only letters . Remove any punctuations, numbers, symbols.
# Lower case all the alphabets
# Removing URLs ( starting with https: or http: or www.)
sed -r -n '
y/QWERTYUIOPASDFGHJKLZXCVBNM/qwertyuiopasdfghjklzxcvbnm/
s/[0-9[:punct:]]//g
s/(https|http|www)[a-z]*//g
/^$/ !{
    p
}
' sample.txt > output1.txt

# Remove Stop words (read list of stop words provided in stopwords.txt)
sed 's/.*/s:(^| )&\($| \):\\1:g/' stopwords.txt > words.sed
sed -r -f words.sed output1.txt > output2.txt

#Stemming - The task of removing certain prefixes and suffixes and retaining the word.
# The valid suffixes to be removed are in the files suffixes.txt . Remove only the suffix, not
# the entire word.
sed -r 's/.*/s:&\\b:0:g/' suffixes.txt > words.sed
sed -r -f words.sed output2.txt > output1.txt
sed -r 's/0//g' output1.txt > output2.txt

# Make sure spaces are used appropriately
# Remove words that have word length <=2
sed -r -n '
s/\b[a-z]{1,2}\b//g
s/[ ]+/ /g
s/ $//g
p
' output2.txt > output.txt

#append endline if not present
echo "" >> output.txt

#cleanup
rm output2.txt
rm output1.txt
rm words.sed
