# https://github.com/tamccullough - questions? twitter @tamccullough

# replace everything with your collections attributes.
# add more dictionaries within it

FIRST_NAMES = [
    'Name1','Name2','Name3',
]
LAST_NAMES = [
    'Lastname1','Lastname2','Lastname3',
]

convert = {
    'torso':{
        1:'one',
        2:'two',
        3:'three',
        4:'four',
    },
    'arms':{
        1:'a-1',
        2:'a-2',
        3:'a-3',
        4:'a-4',
    },
}

# query the above dictionary to convert the int values in the dataframe
# into something useful in the item attributes
def get_collection_item(item,num):
    return convert[item][num]
