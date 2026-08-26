from pathlib import Path
import os


def createfile():
    try:
        name = input("please enter your file name : ")
        path = Path(name) # file ka path check kr rhe hai 
        if not path.exists():  # checks file is already existed or not 
            # "with" keyword automatically closes the file after open
            with open(path,"w") as fs: # if path does not exists then create a path
                data = input("what do you want to write : ")
                fs.write(data)
            print("file created sussesfully. ")    
        else:
            print("ERROR! file name is already exists.")    
    except Exception as err:
        print(f"an error occured as {err}")        
                
def readfile():
    try:
        name = input("enter your file name : ")
        path = Path(name)
        if path.exists():  # if path of given file the open it and read 
            with open(path,"r") as fs:
                content = fs.read()
                print(f"your file content is : \n {content}")
        else:
            print("No such file exists!")  
    except Exception as err:
        print(f"an error occured as {err}")              
             
def updatefile():
    try:
        name = input("enter your file name : ")
        path = Path(name)
        if path.exists():
            print("Operations : ")
            print("1. renaming the file ")
            print("2. appending the content ")
            print("3. overwriting the file ")
            
            choice = int(input("enter your choice(1-3) : "))
            if choice==1:
                newname=input("enter your new file name : ")
                new_path= Path(newname)
                if not new_path.exists():
                    path.rename(new_path)
                    print("renamed successfully !")
                else:
                    print("file already exists !") 
            elif choice==2:
                with open(path,"a") as fs:
                    data=input("what do you want to append : ")
                    fs.write(" \n"+data)
                print("successfully appended !")  
            elif choice==3:
                with open(path,"w") as fs:
                    data=input("what do you want to write: ") 
                    fs.write(" \n"+data)      
                print("file overwrite successfully !")     
    except Exception as err:
        print(f"an error occurred as {err}")                   


def deletefile():
    try:
        name = input("enter your file name : ")
        path = Path(name)
        if path.exists():
            path.unlink()  # to delete a file path
            print("file deleted successfully !")
        else:
            print("ERROR! no such path exists.")
    except Exception as err:
        print(f"an error occured as {err}")      



print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

a=int(input("\ntell your response : "))

if a==1:
    createfile()
if a==2:
    readfile()
if a==3:
    updatefile()
if a==4:
    deletefile()