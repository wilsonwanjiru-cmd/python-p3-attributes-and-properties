import pytest
from dog import Dog

def test_dog_name_not_empty():
    '''raises ValueError if empty string.'''
    with pytest.raises(ValueError, match="Name must be a string between 1 and 25 characters."):
        Dog(name="")

def test_dog_name_string():
    '''raises ValueError if not string.'''
    with pytest.raises(ValueError, match="Name must be a string between 1 and 25 characters."):
        Dog(name=123)

def test_dog_name_under_25():
    '''raises ValueError if string over 25 characters.'''
    with pytest.raises(ValueError, match="Name must be a string between 1 and 25 characters."):
        Dog(name="What do dogs do on their day off? Can't lie around - that's their job.")

def test_dog_breed_not_in_list():
    '''raises ValueError if not in breed list.'''
    with pytest.raises(ValueError, match="Breed must be in the list of approved breeds."):
        Dog(breed="Human")



