#!/bin/bash

awk '
BEGIN {}
{
    for(i = 1; i <= NF; i++) {
        if(word[i] == "") {
            word[i] = $i
        } else {
            word[i] = word[i]" "$i
        }
    }
} END {
    for(i in word) print word[i]
}' target.txt
