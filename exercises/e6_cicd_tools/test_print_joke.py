from print_joke import get_random_reaction, reactions


def test_get_random_reaction_type():
    reaction = get_random_reaction()
    assert type(reaction) == str # Replace False with a check that makes sure the reaction is a string type


def test_get_random_reaction_repeats():
    # Write a test that checks that multiple calls to get_random_reaction()
    # doesn't give you the same reaction every time
    for _ in range(1000):
        reaction1, reaction2 = get_random_reaction(), get_random_reaction()
        if reaction1 != reaction2:
            break
    assert not reaction1 == reaction2


# Come up with a test of your own and implement it here.
def test_reactions_dtype():
    for reaction in reactions:
        if type(reaction) != str:
            break
    assert type(reaction) == str