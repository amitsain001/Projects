import random
import string

def your_passward(length=10, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_char=True): 
    
    #Constructs the character_set based on the parameters. If none of the flags are set to True, it returns Error.
    
    set_of_character=""
    
    if include_uppercase:
        set_of_character +=string.ascii_uppercase
    if include_lowercase:
        set_of_character +=string.ascii_lowercase
    if include_digits:
        set_of_character +=string.digits
    if include_special_char:
        set_of_character +=string.punctuation
        
    if not set_of_character:
        return ValueError("invalid input from the user")
        
    passward=''.join(random.choice(set_of_character) for _ in range(length))
    return passward

# Providing the parameters as per requirement

passward_length = 15 
passward=your_passward(length = passward_length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_char=True)
print(f"\nyour passward is : {passward}")
    
    
    
    