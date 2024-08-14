from library_item import LibraryItem 


library = {} 

library["01"] = LibraryItem("Die For You", "The Weeknd", 4)
library["02"] = LibraryItem("My Love", "Westlife", 5)
library["03"] = LibraryItem("The Ghost of You", "My Chemical Romance", 3) 
library["04"] = LibraryItem("What Do You Do", "Papa Roach", 4) 
library["05"] = LibraryItem("Attack", "Thirty Seconds To Mars", 5)


def list_all(): 
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"  
    return output


def get_name(key): 
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_director(key): 
    try:
        item = library[key]
        return item.director
    except KeyError: 
        return None


def get_rating(key): 
    try:
        item = library[key]
        return item.rating
    except KeyError: 
        return -1

def set_rating(key, rating): 
    try:
        item = library[key]
        item.rating = rating 
    except KeyError: 
        return  


def get_play_count(key): 
    try:
        item = library[key]
        return item.play_count
    except KeyError: 
        return -1 


def increment_play_count(key): 
    try:
        item = library[key]
        item.play_count += 1 
    except KeyError:  
        return 


