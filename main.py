import os  # accessing the os functions
import Capture_Image
import Train_Image
import Recognize


# creating the title bar function

def title_bar():
    os.system('cls')  # for windows

    # title of the program

    print("Face Recognition Attendance System")



# creating the user main menu function

def mainMenu():
    title_bar()
    print()
    print("1. Capture a new face")
    print("2. Train the images")
    print("3. Face Recognition and recording attendance")
    print("4. Send a mail of the attendance recorded")
    print("5. Exit")

    while True:
        try:
            choice = int(input("Please enter your choice (1-5): "))

            if choice == 1:
                CaptureFaces()
                break
            elif choice == 2:
                Trainimages()
                break
            elif choice == 3:
                RecognizeFaces()
                break
            elif choice == 4:
                os.system("python automail.py")
                break
            elif choice == 5:
                print("Thank You")
                break
            else:
                print("Invalid Choice. Enter 1-5")
                mainMenu()
        except ValueError:
            print("Invalid Choice. Enter 1-5\n Try Again")
    exit



# --------------------------------------------------------------
# calling the take image function form capture image.py file

def CaptureFaces():
    Capture_Image.takeImages()
    key = input("Enter any key to return to the main menu")
    mainMenu()


# -----------------------------------------------------------------
# calling the train images from train_images.py file

def Trainimages():
    Train_Image.TrainImages()
    key = input("Enter any key to return to the main menu")
    mainMenu()


# --------------------------------------------------------------------
# calling the recognize_attendance from recognize.py file

def RecognizeFaces():
    Recognize.recognize_attendence()
    key = input("Enter any key to return to the main menu")
    mainMenu()


# ---------------main driver ------------------
mainMenu()
