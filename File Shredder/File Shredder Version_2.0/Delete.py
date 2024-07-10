def AutoDelete(user_path):
    import os,shutil
    for file in os.listdir(user_path):
        if not os.path.isfile(f'{user_path}\\{file}'):
            if file=='Unable_to_shred':
                pass
            else:
                shutil.rmtree(f'{user_path}\\{file}',ignore_errors=True)
        else:
            os.remove(f'{user_path}\\{file}')
    return f"\nDELETED"