# Working with the zip files

f = open("file.exe", "w+")
f.write("here is the only file that i openned\n")
f.close()

f = open("file.ex1", "w+")
f.write("here is the only file that i openned\n")
f.close()
f = open("file.ex2", "w+")
f.write("here is the only file that i openned\n")
f.close()

# add files one by one to zip file... 
import zipfile

comp= zipfile.ZipFile("Comprassed.zip", "w")

comp.write("file.exe", compress_type = zipfile.ZIP_DEFLATED)
comp.write("file.ex1", compress_type = zipfile.ZIP_DEFLATED)
comp.write("file.ex2", compress_type = zipfile.ZIP_DEFLATED)

comp.close()

zipObj = zipfile.ZipFile("Comprassed.zip", "r")
zipObj.extractall("Here")

#Entire directory to zip file

#PATHS MUST BE EXACT PATH
import shutil
dirZip = "Here"
outputFile = "./example"
shutil.make_archive(outputFile, "zip", "dam")

#eXTRACT ENTIRE FILE 
shutil.unpack_archive("Source.zip","SourceLocation", "zip")

