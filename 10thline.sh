#!/bin/bash

awk '{if(FNR==10) print $0}' target.txt
