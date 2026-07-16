from typing import List, Tuple, Union, Dict

number : list[int] = [1,2,3,4,5] #for list
person : tuple[int,str] = (34, "Haseeb") # for tuple
scores : dict[str,int] = {"haseeb": 90, "hassan": 80} # for dict
identifier : Union[int, str] = "ID123" # for union
identifier = 12345

n : int = 5


name : str = "Haseeb"

def sum( a : int, b : int) -> int:
    return a + b

sum(3,2)