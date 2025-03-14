# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.write("Kaan Emre")
#     print(file.read())



#*** sayfa sonunu güncelleme***
# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nMerhabalar")
    

# *** sayfa başında güncelleme***
# with open("newfile.txt","r+",encoding="utf-8") as file:
#        content = file.read()
#        content = "Merhabalar\n" + content
#        file.seek(0)
#        file.write(content)

# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())


#*** sayfa ortasında güncelleme ***

with open("newfile.txt","r+",encoding="utf-8") as file:
    list=file.readlines()
    list.insert(1,"Polat Alemdar\n")
    file.seek(0)
    file.writelines(list)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())
