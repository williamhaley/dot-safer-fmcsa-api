#!/usr/bin/env bash

printf "success:  "

find ./saved/ -name *.html -type f -size +30000c | wc -l
