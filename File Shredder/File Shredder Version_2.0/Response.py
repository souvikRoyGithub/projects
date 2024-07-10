def UserInput(msg,answers_set,skip_answer_set):
    while True:
        try:
            user_response=input(f'{msg}\n').lower()
            if skip_answer_set:
                break
            if user_response not in answers_set:
                from colorama import Fore,Back,Style
                print(Fore.RED+Back.BLACK+Style.BRIGHT+"ENTER A VALID INPUT")
                continue     
            break   
        except: 
            print(Fore.RED+Back.BLACK+Style.BRIGHT+"ENTER A VALID INPUT")
            continue
    return user_response