import os,sys,shutil

def choice():
    ch = int(input("enter your choice \n1.open file \n 2.append file \n 3.create file \n 4.delete file \n 5.copy file \n 6.move file 7.rename_file \n 8. exit \n "))
    if ch == 1:
        open_file()
    elif ch == 2:
        append_file()
    elif ch == 3:
        create_file()
    elif ch == 4:
        delete_file()
    elif ch == 5:
        copy_file()
    elif ch == 6:
        move_file()
    elif ch == 7:
        rename_file()
    elif ch == 8:
        print("bye bye..........exiting text editor")
        exit(0)
    else:
        print("wrong input ,try again")
        choice()


def open_file():
    try:
       file_path = input("enter full path to your file- ")
       if os.path.exists(file_path):
           with open(file_path) as fp:
            print(fp.read())
    except Exception as e:
        print("there was a problem: %s" %(e))
            
        choice()

    else:
        print("file does not exists \n do you want to create a new file y/n-")
        if input().lower() == 'y':
            create_file(file_path)
        else:
            choice()


def append_file():
    file_path = input("enter full path to your file-")
    if os.path.exists(file_path):
        with open(file_path , 'a+') as fp:
            print("start writing into file- press:wq for save and exit")
            while True:
                temp = input()
                if temp ==':wq':
                    print("save and exiting your file")
                    choice()
                else:
                    fp.write(temp)
                    fp.write('\n')
    else:
        print("file does not exists")
        choice()


def create_file(path = None):
    if path:
        file_path = path
    else:
        file_path = input("enter full path to your file-")
        with open(file_path,'w+') as fp:
            print("start writing into file - press :wq save and exit")
            while True:
                temp = input()
                if temp == ':wq':
                   print("saving and exiting the file")
                choice()
            else:
                fp.write(temp)
                fp.write('\n')


def delete_file():
    file_path = input("enter your file path which you want to delete-")
    if os.file.exists(file_path):
        os.unlink(file_path)
        print("file sucessfully deleted")
    else:
        print("no such file exist")
        choice()


def copy_file():
    source_path = input("enter full source file_path-")
    dest_path = input("enter full destination file path-")
    if os.path.exists(source_path):
        shutil.copy(source_path , dest_path)
        print("file sucessfully copied")
    else:
        print("file does not exists")
        choice()

def move():
    source_path = input("enter path which file do you want to move-")
    dest_path=input("enter new path where do you want to move your file")
    if os.path.exists(source_path):
        shutil.move(source_path , dest_path)
        print("file sucessfully moved")
    else:
        print("file does not exists")
        choice()

def rename_file():
    old_path = input("enter old path of file which you want to rename")
    new_path = input("enter new path")
    if os.path.exists(old_path):
        os.rename(old_path ,new_path)
        print("file sucessfully renamed")
    else:
        print("file does not exists")
        choice()

if __name__ == '__main__':
    print("welcome to command line text editor")
    choice()


