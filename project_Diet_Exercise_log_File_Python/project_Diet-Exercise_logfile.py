def getdate():
    import datetime
    return datetime.datetime.now()
while True:
    try:
        n = int(input("\nEnter 1 or 2 or 3 to add something to the following profiles of Harry,Rohan or Hammad\nEnter 4 to see their profile:\nEnter 5 for close the program.\n"))
        if n == (1):
            i = input('Press "d" for Diet\nPress "e" for Exercise: ')
            if i == "d":
                with open("Diet_Harry.txt", "a") as f:
                    HD = input("Enter the Diet for Harry: ")
                    f.write(f"[{getdate()}]: {HD}\n")
                    print("Thank you for the data.")
            elif i == "e":
                with open("Ex_Harry.txt", "a") as f:
                    HE = input("Enter the Exercise for Harry: ")
                    f.write(f"[{getdate()}]: {HE}\n")
                    print("Thank you for the data.")
            else:
                print("You have not chosen any of the given option.")

        elif n == (2):
            i = input('Press "d" for Diet\nPress  "e" for Exercise: ')
            if i == "d":
                with open("Diet_Rohan.txt", "a") as f:
                    RD = input("Enter the Diet for Rohan: ")
                    f.write(f"[{getdate()}]: {RD}\n")
                    print("Thank you for the data.")
            elif i == "e":
                with open("Ex_Rohan.txt", "a") as f:
                    RE = input("Enter the Exercise for Rohan: ")
                    f.write(f"[{getdate()}]: {RE}\n")
                    print("Thank you for the data.")
            else:
                print("You have not chosen any of the given option.")
        elif n == (3):
            i = input('Press "d" for Diet\nPress  "e" for Exercise: ')
            if i == "d":
                with open("Diet_Hammad.txt", "a") as f:
                    HaD = input("Enter the Diet for Hammad: ")
                    f.write(f"[{getdate()}]: {HaD}\n")
                    print("Thank you for the data.")
            elif i == "e":
                with open("Ex_Hammad.txt", "a") as f:
                    HaE = input("Enter the Exercise for Hammad: ")
                    f.write(f"[{getdate()}]: {HaE}\n")
                    print("Thank you for the data.")
            else:
                print("You have not chosen any of the given option.")

        elif n == (4):
            i = input("Enter H,R or Ha to see the following profiles of Harry,Rohan or Hammad: ")
            if i == "H":
                j = input('Press "d" to see Diet file\nPress  "e" to see Exercise file: ')
                try:
                    if j == "d":
                        with open("Diet_Harry.txt") as f:
                            print(f.read())
                    elif j == "e":
                        with open("Ex_Harry.txt") as f:
                            print(f.read())
                    else:
                        print("You have not chosen any of the given option.")
                except (FileNotFoundError):
                    print("File does not exist yet.")
                except ValueError:
                    print("You have not chosen any of the given option.")

            elif i == "R":
                j = input('Press "d" to see Diet file\nPress  "e" to see Exercise file: ')
                try:
                    if j == "d":
                        with open("Diet_Rohan.txt") as f:
                            print(f.read())
                    elif j == "e":
                        with open("Ex_Rohan.txt") as f:
                            print(f.read())
                    else:
                        print("You have not chosen any of the given option.")
                except FileNotFoundError:
                    print("File does not exist yet.")
                except ValueError:
                    print("You have not chosen any of the given option.")

            elif i == "Ha":
                j = input('Press "d" to see Diet file\nPress  "e" to see Exercise file: ')
                try:
                    if j == "d":
                        with open("Diet_Hammad.txt") as f:
                            print(f.read())
                    elif j == "e":
                        with open("Ex_Hammad.txt") as f:
                            print(f.read())
                    else:
                        print("You have not chosen any of the given option.")
                except FileNotFoundError:
                    print("File does not exist yet.")
                except ValueError:
                    print("You have not chosen any of the given option.")
            else:
                print("You have not chosen any of the given option.")
                try:
                    user_input=input("Choose 'y' to try again \nChoose 'n' to close the program.\n")
                    if user_input=="y":
                        continue
                    elif user_input=="n":
                        break
                    else:
                        print("You are not choosing the given options so you are closing the program.")
                        break   
                except Exception:
                    print("You are not choosing the given options so you are closing the program.")
                    break
        elif n== 5:
            break
        else:
            print("You have not chosen any of the given option.")
            try:
                user_input=input("Choose 'y' to try again \nChoose 'n' to close the program.\n")
                if user_input=="y":
                    continue
                elif user_input=="n":
                    break
                else:
                    print("You are not choosing the given options so you are closing the program.")
                    break   
            except Exception:
                print("You are not choosing the given options so you are closing the program.")
                break
    except ValueError:
        print("You have not chosen any of the given option.")
        try:
            user_input=input("Choose 'y' to try again \nChoose 'n' to close the program.\n")
            if user_input=="y":
                continue
            elif user_input=="n":
                break
            else:
                print("You are not choosing the given options so you are closing the program.")
                break   
        except Exception:
            print("You are not choosing the given options so you are closing the program.")
            break
print("Thank you for using.")