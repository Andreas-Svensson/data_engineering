# exercise 0 part 3

#a) create a folder
mkdir data/pokemon

#b) create a file
touch data/pokemon/pokemon_list.txt

#c) add pokemon to the list

echo -e "bulbasaur/nsquirtle/ncharmander/npikachu" > data/pokemon/po
kemon_list.txt

#d) print pokemon

#for i in $(seq 1 $(wc -l data/pokemon/pokemon_list.txt))
#do
#  echo "pokemon: $(sed -n $(i) data/pokemon/pokemon_list.txt)"
#done

while read -r line
do
  echo -e "pokemon: $line"
done < data/pokemon/pokemon_list.txt


