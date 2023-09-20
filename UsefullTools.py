import random

feet_in_miles = 5280
meters_in_kilometers = 1000
beatles = ["John Lennon", "Paul McCartney"]


def get_file_txt(filename):
    return filename[filename.index('.') + 1:]


def roll_dice(num):
    return random.randint(1, num)
