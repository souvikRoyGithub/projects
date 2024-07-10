def main():
    #style formats:
    # Fore.GREEN+Back.BLACK+Style.BRIGHT+
    # Fore.RED+Back.BLACK+Style.BRIGHT+
    # Fore.GREEN+Back.BLACK+Style.NORMAL+

    print(Fore.GREEN+Back.BLACK+Style.BRIGHT+Display.help())
    print(Fore.RED+Back.BLACK+Style.BRIGHT+Display.warning())
    user_path=Response.UserInput(Fore.GREEN+Back.BLACK+Style.NORMAL+'ENTER YOUR PATH:',{},True)
    if not os.path.exists(user_path): 
        print(Fore.RED+Back.BLACK+Style.BRIGHT+'\nPATH DOES NOT EXIST')
        return
    else: 
        if user_path.startswith('c:'):
            print(Fore.RED+Back.BLACK+Style.BRIGHT+'FILES ARE IN C DRIVE!!!\nWE WOULD RECOMMEND YOU TO CHECK ONCE IF THE PATH IS ABSOLUTELY CORRECT\n')
        print(Fore.GREEN+Back.BLACK+Style.NORMAL+f'THE FILES AND FOLDERS INSIDE THAT DIRECTORY\n{os.listdir(user_path)}')
        user_confirmation=Response.UserInput(Fore.GREEN+Back.BLACK+Style.NORMAL+'ARE YOU SURE?\nY/N',{'y','n'},False)
        if user_confirmation=='n':
            return
        else:
            if os.path.isdir(f'{user_path}\\Unable_to_shred'):
                pass
            else:
                os.mkdir(f'{user_path}\\Unable_to_shred')
            print(Fore.GREEN+Back.BLACK+Style.NORMAL+Shredder.FileShredder(user_path))
            print(Fore.RED+Back.BLACK+Style.BRIGHT+'BEFORE AUTOMATICALLY DELETE THE FILES AND FOLDERS WE WOULD RECOMMEND YOU TO CHECK ONCE IF THE FILES ARE OVERWRITTEN OR NOT FOR YOUR OWN PRIVACY AND SATISFACTION')
            if_delete=Response.UserInput(Fore.GREEN+Back.BLACK+Style.BRIGHT+'DELETE THE FILES AND FOLDERS?\nY/N',{'y','n'},False)
            if if_delete=='y':
                print(Fore.GREEN+Back.BLACK+Style.BRIGHT+Delete.AutoDelete(user_path))
            else:
                print(Fore.GREEN+Back.BLACK+Style.BRIGHT+"SELECT AND SHIFT+DELETE THE FILES AND FOLDERS INSIDE THAT DIRECTORY TO RECOVER SPACE")
            return
if __name__=='__main__':
    from colorama import Fore,Back,Style
    import Display
    import Response
    import Shredder
    import Delete
    import os
    main()
    print(Fore.RED+Back.BLACK+Style.BRIGHT+"FILES AND FOLDERS INSIDE THE Unable_to_shred DIRECTORY ARE NOT OVERWRITTEN NOR DELETED")
    print(Fore.GREEN+Back.BLACK+Style.BRIGHT+"THANKS FOR USING")