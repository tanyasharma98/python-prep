# Oh soldier Prettify my Folder
#path , dictionary , format
import os
# def soldier("C.//", "tanya.txt", "jpg"):
def soldier(paths , file , format):
    os.chdir(paths)
    files =os.listdir(paths)
    if os.path.exists(paths) == True:
        print(f"Your Path Exists as:{paths}")
        with open(file) as f:
            filelist =f.read().split("\n")
    if os.path.exists(paths) == False:
        print(f"Your Path  Doesn't Exists as:{paths}")

    for file in files:
        if os.path.exists(file) == True and file not in filelist:
            remnamee = os.rename(file , file.capitalize())
        # print(file.capitalize())
        if os.path.splitext(file)[1] == format:
            renamee=os.rename(file, f"{i}.{format}")
            i += 1
            print(renamee)
    if os.path.exists(file) == False:
        print(f"Your File Doesn't exist as:{file}")


    if format== "jpg":
        i=1
        print("Files are found as:")
        for files in files:
             if files.endswith(".jpg"):
                 print(files)
                 os.rename(files,f"{i}.jpg")
                 i=i+1
        for files in files:
           print("Files Name are prettified as:")
           if files.endswith(".jpg"):
               continue
           print(files)


if __name__ == '__main__':
    print(r"C:\Users\tarun\PycharmProjects\PythonTuts\Exxx8folder")
    # dg = os.getcwd()
    pathhii = input("Copy from above")
    print(r"C:\Users\tarun\PycharmProjects\PythonTuts\Exxx8folder\Exe.txt")
    filll = input("Enter file name you want to prettify")
    formmm = input("Enter Format you want to prettify")
    soldier(pathhii,filll,formmm)

    # if os.path.exists(filll) == True:
    #     remnamee = os.rename(filll , filll.capitalize())
    #     print(filll.capitalize())


    # for files in os.listdir(dg) :
    #     if files.endswith(".jpg"):
    #         print("These files are found")
    #         print(files)
    #         # print(os.rename(files,f"{i}.jpg"))
    #         # i=i+1
    #         print("successfuly renamed")
    #         print(files)




                #--------------DAnger____________________
                # i=i+1
                # # namee=files.split("."[0][1])
                # namee= os.path.split(files)
                # os.rename(files,f"{i}.{namee[1]}")
                # print(files)




    # Format_img = input("Enter Format To rename")
    # print(os.getcwd())
    # soldier(path,file,Format_img)


