from datetime import datetime
from random import choices
import string
from time import sleep

random_string = "".join(choices(string.printable, k=25))

while True:
    print(f"{datetime.now()}: {random_string}")
    sleep(5)
