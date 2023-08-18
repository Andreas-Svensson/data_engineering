#!/bin/bash

echo -e "---\nexercise 1\n---"

# a) make dir
mkdir cool_notes

# b) move note files
mv note* cool_notes/

# c) delete note4
rm cool_notes/note4

# d) change dir and list files
cd cool_notes
echo -e "\nFiles in cool_notes folder:"
ls

# e) move note3 to parent
mv note3.txt ..

# f) navigate to parent
cd ..

# g) list all files
echo -e "\nFiles in parent folder:"
ls -a

# h) rename note3
mv note3.txt note_home.txt

echo -e "\nexercise 1 done\n"
