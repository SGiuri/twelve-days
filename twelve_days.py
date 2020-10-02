import re


def recite(start_verse, end_verse):
    verse_12 = """
    On the twelfth day of Christmas my true love gave to me: 
    twelve Drummers Drumming, 
    eleven Pipers Piping, 
    ten Lords-a-Leaping, 
    nine Ladies Dancing, 
    eight Maids-a-Milking, 
    seven Swans-a-Swimming, 
    six Geese-a-Laying, 
    five Gold Rings, 
    four Calling Birds, 
    three French Hens, 
    two Turtle Doves, 
    and a Partridge in a Pear Tree.
    """

    days = ["first",
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth",
            "seventh",
            "eighth",
            "ninth",
            "tenth",
            "eleventh",
            "twelfth"]

    the_song = []

    # splitting the twelfth verse
    verse_parts = [verse.lstrip() for verse in verse_12.strip().split("\n")]
    intro_verse = verse_parts.pop(0)

    # building each verse
    for day in range(start_verse, end_verse + 1):

        days_intro = re.sub(r"twelfth", days[day - 1], intro_verse)

        if day == 1:
            requested_verse = days_intro + list_to_str(verse_parts[11][4:])
        else:
            requested_verse = days_intro + list_to_str(verse_parts[12 - day:])
        the_song.append(requested_verse)

    return the_song


def list_to_str(list_of_string):
    final_stirng = ""
    for j in range(len(list_of_string)):
        final_stirng += list_of_string[j]
    return final_stirng
