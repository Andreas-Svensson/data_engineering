#!/bin/bash

echo -e "---\nexercise 0\n---"

# create note files
for i in {1..4}; do
  if [ $i -le 3 ]; then
    filename=note$i.txt
  else
    filename=note$i
  fi
  touch $filename
done

echo -e "\nexercise 0 done\n"
