import os
import requests
from flask import redirect, render_template
from functools import wraps

''' Display an apology to the user '''
def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def makePhrase(first,second,third):
    """Generate a silly phrase based on RNG"""

    # Start with a new line
    phrase = ""

    # Read the files into arrays without newlines
    with open("static/1.txt") as part1:
        openers = [line.rstrip() for line in part1]
    with open("static/2.txt") as part2:
        middles = [line.rstrip() for line in part2]
    with open("static/3.txt") as part3:
        closers = [line.rstrip() for line in part3]

    # Append the three parts to the phrase
    phrase += openers[first] + " " + middles[second] + " " + closers[third] + "!"

    part1.close()
    part2.close()
    part3.close()

    return phrase


