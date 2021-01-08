#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
import instaloader

# decoration
print(stylize("\n---- | Download Instagram profile picture | ----\n", fg("red")))

# class
class Downloader:
    def __init__(self, username):
        self.username = username

    # output magic method
    def __repr__(self):
        try:
            self.get_profile_picture(self.username)
            return stylize(f"\nProfile picture of \"{self.username}\" downloaded successfully.\n", fg("green"))
        except:
            return stylize(f"\nUser \"{self.username}\" does not exist.\n", fg("red"))

    # methods
    def get_profile_picture(self, user):
        session = instaloader.Instaloader()
        session.download_profile(user, profile_pic_only=True)
        return 0

# main execution
if __name__ == "__main__":
    # user interaction
    username = input("Enter username: ")

    print(Downloader(username))
