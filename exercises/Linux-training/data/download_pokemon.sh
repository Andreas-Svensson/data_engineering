for pokemon in $(cat ./pokemon/pokemon_list.txt)
do
	echo -e "\n-----\ncreating file: $pokemon.json\n-----\n"
	wget -O ./pokemon/$pokemon.json https://pokeapi.co/api/v2/pokemon-species/$pokemon
done

echo -e "\n-----\nDone!\n-----\n"
