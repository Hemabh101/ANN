import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import cv2
import time
import os
import GPUtil
import time
import pygame
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import threading


def display_text(text):
    print(text)

def take_command():
    command = input("Enter your command: ")
    return command.lower()

def run_hexagon():
    data = {}

    while True:
        command = take_command()
        print(command)

        if 'play' in command:
            song = command.replace('play', '')
            display_text('Playing ' + song + ' on YouTube...')
            pywhatkit.playonyt(song)
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            display_text('Current time is ' + current_time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
        elif 'joke' in command:
            display_text(pyjokes.get_joke())
        elif 'search' in command:
            target = command.replace('search', '')
            display_text('Searching for ' + target + '...')
            pywhatkit.search(target)
        elif 'data' in command:

            def store_data():
                key = input("enter a variable name: ")
                value = input("Enter the data to store: ")
                data[key] = value
                print(f"Data stored under key '{key}'.")

            def share_data():
                key = input("Enter a variable name to share data: ")
                if key in data:
                    print(f"Data for '{key}': {data[key]}")
                else:
                    print(f"Variable '{key}' not found.")

            while True:
                action = input("Enter 'store data', 'share data', or 'quit': ")
                if action.lower() == 'quit':
                    break
                elif action.lower() == 'store data':
                    store_data()
                elif action.lower() == 'share data':
                    share_data()
                else:
                    print("Invalid action. Please enter 'store data', 'share data', or 'quit'.")
        elif 'close' in command:
            display_text('Closing Hexagon.')
            break
        elif 'face' in command:
            camera = cv2.VideoCapture(0)

            if not camera.isOpened():
                print("Error opening camera")
                exit()

            while True:
                ret, frame = camera.read()

                cv2.imshow('Camera', frame)

                key = cv2.waitKey(1) & 0xFF
                if key == ord('p'):
                    filename = f"photo_{time.strftime('%Y%m%d_%H%M%S')}.jpg"
                    cv2.imwrite(filename, frame)
                    photo_path = os.path.abspath(filename)
                    print("Photo saved at:", photo_path)
                    break

            camera.release()

            ref_images = [
                ("Your photo", cv2.imread(photo_path))
            ]

            cap = cv2.VideoCapture(0)

            should_detect = False

            while True:
                ret, frame = cap.read()

                if should_detect:
                    for ref_image_name, ref_image in ref_images:
                        result = cv2.matchTemplate(frame, ref_image, cv2.TM_CCOEFF_NORMED)
                        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

                        if max_val >= 0.8:
                            print("I see:", ref_image_name)
                            x, y = max_loc
                            w, h = ref_image.shape[1], ref_image.shape[0]
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                cv2.imshow("Camera", frame)

                key = cv2.waitKey(1)

                if key == ord("q"):
                    break
                elif key == ord("y"):
                    should_detect = True

        else:
            
            matching_variables = [var for var in data.keys() if var in command]
            if matching_variables:
                for variable in matching_variables:
                    print(f"Data for '{variable}': {data[variable]}")
            else:
                display_text('Please try again or rephrase your command.')

    cv2.destroyAllWindows()
    


run_hexagon()
