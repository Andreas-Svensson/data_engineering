# exercise 0 part 2

echo -e "---\nexercise 2\n---"

# a) print
echo "hello not from note_home"

# b) write text to note_home
echo "hello from note_home" > note_home.txt

# c) print out the current path
echo "current path is:" $(pwd)

# d) write text to note_home
echo "current path is:" $(pwd) >> note_home.txt

# e) print contents of note_home
cat note_home.txt

# f) count words in file
wc -w note_home.txt

# g count lines in file
wc -l note_home.txt

# h) count files in cool_notes
ls cool_notes | wc -l

# i) check disk usage
df -h

echo -e "\nexercise 2 done\n"
