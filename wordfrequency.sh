#!/bin/bash

awk '{
    for(i = 1; i <= NF; i++) {
        word[$i] ++
    }
} END {
    for(i in word) {
        print i, word[i]
    }
}' target.txt | sort -k2 -nr
