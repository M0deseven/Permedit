import os

print('Directory Ownership Tool')

MAIN_MENU = '''\
### Change Directory Permissions = chmod
### Change Directory Ownership = chown
### List Directory Contents = ls
### Quit = quit / exit
### Change Directory = cd'''

func_list = ['quit', 'ls', 'chown', 'chmod', 'chdir']

Error01 = 'A problem has occured. Double check paths and spelling'

print('Enter a direcory to modify//>')
mod_dir = input('//> ')


def space_remover(string):
    newstring = string.replace(' ', '_')
    return newstring


def change_directory(mod_dir):
    print('Enter a new directory')
    newdir = input('//> ')
    mod_dir = newdir
    print(mod_dir)
    os.chdir(mod_dir)
    return mod_dir

def permission_change():
    permission_list = ['r','w','x']
    print('[+] or [-] permissions? ')
    sub_mode = input('//> ')
    print(f'select a permission to {sub_mode}')
    print('[r]ead|[w]rite|e[x]ecute')
    print(permission_list)
    selected_permission = input('//> ')
    os.chdir(mod_dir)
    for file in os.listdir():
        os.rename(file, space_remover(file))
        for i in permission_list:
            if i == selected_permission:
                try:
                    os.system(f'sudo -S chmod -R {sub_mode}{i} {space_remover(file)} ')
                except:
                    print(Error01)
    os.system('ls -lsar')
    print('')


def ownersip_change():
    print('Enter a User Name')
    usrname = input('//> ')
    os.chdir(mod_dir)
    for file in os.listdir():
        os.rename(file, space_remover(file))
        try:
            os.system(f'sudo -S chown  -R {usrname}:{usrname} {file}')
        except:
            print(Error01)
    os.system('ls -lsar')
    print(' ')


while True:
    print(MAIN_MENU)
    mode = input('//> ')
    if mode.lower() == 'chmod':
        permission_change()
    if mode.lower() == 'chown':
        ownersip_change()
    if mode.lower() == 'ls':
        os.chdir(mod_dir)
        os.system('ls -lsar')
        print(' ')
    if mode.lower() == 'cd':
        change_directory(mod_dir)
    if mode.lower() == 'quit':
        break
    if mode.lower() not in func_list:
        print('invalid selection')