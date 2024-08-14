from library_item import LibraryItem

def text_init():
    item = LibraryItem("Die For You", "The Weeknd")
    assert item.name == "Die For You"
    assert item.director == "The Weeknd"
    assert item.rating == 4
    assert item.play_count == 0
    