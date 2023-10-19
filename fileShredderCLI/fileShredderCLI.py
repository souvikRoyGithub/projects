'''1.Make a directory and placed the files,folders in that directory that you want to delete.*(We would recommend you to not to create the folder in C drive)\n2.Take the path ofthe files and folders in that directory.\n3.input that path only.'''

import os

def warning():
    print('\n***warning!!! files can be parmanently deleted and also cant be recovered!!!***\n')

def userInput(msg,ansset,ifLook):
    while True:
        try:
            res=input(f'\n{msg}\n')
            if ifLook and res not in ansset:
                print("\nEnter a valid input!")
                continue     
            break   
        except: 
            print("\nEnter a valid input!")
            continue
        
    return res

def fileShred(myPath):
    def delTxt(file,pth,i): # overwrite normal txt files
        with open(pth+'\\'+file,'w') as f: 
            f.write('1')
        old,new=pth+'\\'+file,pth+'\\'+f'{i}'+'.txt'
        os.rename(old,new)

    def delBin(file,pth,i): # overwrite binary files
        with open(pth+'\\'+file,'wb') as f:
            f.write(b'1')
        old,new=pth+'\\'+file,pth+'\\'+f'{i}'+'.txt'
        os.rename(old,new)

    def fileShred(pth,i):
        for files in os.listdir(pth):
            if not os.path.isfile(pth+'\\'+files): #handling folders 
                fileShred(pth+'\\'+files,i)
            else:
                if '.txt' in files:
                    delTxt(files,pth,i)
                else:
                    delBin(files,pth,i)   
            i+=1

    fileShred(myPath,1)
    print("\nOverwritten!")

def autoDel(pth):
    import shutil

    for f in os.listdir(pth):
        if not os.path.isfile(pth+'\\'+f):
            shutil.rmtree(pth+'\\'+f,ignore_errors=True)
        else:
            os.remove(pth+'\\'+f)

    print("\nDeleted.")


def main():
    myPath=userInput('Enter your path:',{},False)
    if not os.path.exists(myPath): 
        print('\nPath does not exist.')
        return
    else: 
        if myPath.startswith('c:') or myPath.startswith('C:'):
            print('Files are in C drive!!!\nWe would recommend you to check once if the path is absolutely correct.\n')
        confirmation=userInput('Are you sure?\ny/n',{'y','n'},True)
        if confirmation=='n': return
        else: 
            fileShred(myPath)

            ifDel=userInput('Before automatically delete the files and folders we would recommend you to check once for your own privacy if the files are overwritten or not.\n\nDelete the files and folders?\ny/n',{'y','n'},True)
            if ifDel=='y': autoDel(myPath)
            else:
                print("\nnow do the shift+del the files and folders inside the 'shredderFolder' to recover space.")
            return

if __name__=='__main__':
    main()
    print("\nThanks for using!")