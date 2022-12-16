# Rich Whiffen - 12/15/2022
# testing out reading and writing the tree dictionaries.

import time
import json
import pickle

TREE_DICT_FILE="home-tree.json"

#tree_dict={
#"row1": [0, 55],
#"row2": [56, 102],
#"row3": [103, 143],
#"row4": [144, 180],
#"row5": [181, 210],
#"row6": [211, 234],
#"row7": [235, 249],
#}


#with open(TREE_DICT_FILE, "w") as handle:
# json.dump(tree_dict, handle)

with open(TREE_DICT_FILE, 'r') as handle:
    tree_dict = json.loads(handle.read())


for row in tree_dict:
    start_led=tree_dict[row][0]
    end_led=tree_dict[row][1]
    print(f"row: {row} start: {start_led}, end: {end_led}")
print(tree_dict)
