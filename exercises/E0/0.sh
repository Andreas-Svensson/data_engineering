#!/bin/bash

echo "running exercise script..."
sleep 1

# create note files
for i in {1..4}; do
  if [ $i -le 3 ]; then
    filename=note$i.txt
  else
    filename=note$i
  fi
  touch $filename
done


