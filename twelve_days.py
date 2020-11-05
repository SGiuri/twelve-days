def recite(start_verse, end_verse):

    presents = ['a Partridge in a Pear Tree.',
                'two Turtle Doves, ',
                'three French Hens, ',
                'four Calling Birds, ',
                'five Gold Rings, ',
                'six Geese-a-Laying, ',
                'seven Swans-a-Swimming, ',
                'eight Maids-a-Milking, ',
                'nine Ladies Dancing, ',
                'ten Lords-a-Leaping, ',
                'eleven Pipers Piping, ',
                'twelve Drummers Drumming, ']

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

    for verse_number in range(start_verse-1, end_verse):

        verse = f"On the {days[verse_number]} day of Christmas my true love gave to me: "
        for numbers_of_presents in range(verse_number, -1, -1):

            verse += presents[numbers_of_presents]
            if numbers_of_presents == 1:
                verse += "and "
        the_song.append(verse)

    return the_song
