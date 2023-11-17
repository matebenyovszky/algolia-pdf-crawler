import threading
import time

# Function to display a simple spinner
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

cursor = spinning_cursor()

def spinner_task():
    while True:
        print(next(cursor), end='\r')
        time.sleep(0.1)
