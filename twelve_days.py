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
            "forth",
            "fifth",
            "sixth",
            "seventh",
            "eigth",
            "nineth",
            "tenth",
            "eleventh",
            "twelfth"]

    verse_parts = [verse.lstrip() for verse in verse_12.strip().split("\n")]

    intro = verse_parts.pop[0]
    requested_song = []
    # creating first verse

    for day in range(start_verse,end_verse+1):
        day_intro = re.sub(r"twelfth", days[day - 1], intro)
        the_verse = day_intro
        if day == 1:
            the_verse += verse_parts[11][4:]
        else:

            the_verse += verse_parts[13-day:]
        if start_verse == end_verse:
            return the_verse
        requested_song.append(the_verse)

    return requested_song


expected = [
    "On the twelfth day of Christmas my true love gave to me: "
    "twelve Drummers Drumming, "
    "eleven Pipers Piping, "
    "ten Lords-a-Leaping, "
    "nine Ladies Dancing, "
    "eight Maids-a-Milking, "
    "seven Swans-a-Swimming, "
    "six Geese-a-Laying, "
    "five Gold Rings, "
    "four Calling Birds, "
    "three French Hens, "
    "two Turtle Doves, "
    "and a Partridge in a Pear Tree."
]

print(recite(12,12))