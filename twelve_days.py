def recite(start_verse, end_verse):
    presents = ['a Partridge in a Pear Tree.',
                'two Turtle Doves',
                'three French Hens',
                'four Calling Birds',
                'five Gold Rings',
                'six Geese-a-Laying',
                'seven Swans-a-Swimming',
                'eight Maids-a-Milking',
                'nine Ladies Dancing',
                'ten Lords-a-Leaping',
                'eleven Pipers Piping',
                'twelve Drummers Drumming']

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

    for verse_number in range(start_verse - 1, end_verse):

        first_part_verse = f"On the {days[verse_number]} day of Christmas my true love gave to me: "
        second_part_verse = ", ".join(presents[verse_number:0:-1])
        # print(second_part_verse)

        if verse_number > 0:
            verse = first_part_verse + second_part_verse + ", and " + presents[0]
        else:
            verse = first_part_verse + presents[0]

        the_song.append(verse)

    return the_song
