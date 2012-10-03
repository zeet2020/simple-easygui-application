#simple applicatio to create gui application using the easygui python library 

#importing the library file 
import os
import sys



try:
	from easygui import *
except ImportError as ex:
	print format(ex)
	sys.exit(1)


#simple application to browse and view files

#declaring the class fileviewer
class fileviewer:

    def __init__(self):
        #file open prompt
        self.menu()
        
    def menu(self):
        ch=indexbox('Simple File Viewer','Menu',['View File','Exit'])
        if ch ==0:
            #open file select and opne the file
            self.open_file()
            self.menu()
        elif ch ==1:
            #exit the applicaiton
            sys.exit()
            

    def open_file(self):
        #open the file in codebox
        file_name=fileopenbox("please select file to be opened")
        filename = os.path.normpath(file_name)
        text = open(filename,'rb').read()
        codebox("Contents of file " + filename, text=text)
        
        
if __name__ == '__main__':
    fileviewer()
