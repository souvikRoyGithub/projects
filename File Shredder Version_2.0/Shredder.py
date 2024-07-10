def FileShredder(user_path):
    import os,shutil
    def text_shred(file,pth,i): # overwrite normal txt files
        try:
            old_file,new_file=f'{pth}\\{file}',f'{pth}\\{i}.txt'
            with open(old_file,'w') as f: 
                f.write('1')
            os.rename(old_file,new_file)
        except:
            shutil.move(old_file,f'{user_path}\\Unable_to_shred')
    def binary_shred(file,pth,i): # overwrite binary files
        try:
            old_file,new_file=f'{pth}\\{file}',f'{pth}\\{i}.txt'
            with open(old_file,'wb') as f:
                f.write(b'1')
            os.rename(old_file,new_file)
        except:
            shutil.move(old_file,f'{user_path}\\Unable_to_shred')
    def file_shred(pth,i):
        for file in os.listdir(pth):
            if not os.path.isfile(f'{pth}\\{file}'): #handling folders 
                if file=='Unable_to_shred':
                    pass
                else:
                    file_shred(f'{pth}\\{file}',i)
            else:
                if '.txt' in file:
                    text_shred(file,pth,i)
                else:
                    binary_shred(file,pth,i)   
            i+=1
    file_shred(user_path,1)
    return f"OVERWRITTEN"