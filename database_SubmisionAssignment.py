


import sqlite3

#connect to database
conn = sqlite3.connect('data.db')
#create table named tbl_files with two columns "ID and col_files"
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_files TEXT\
                )")

    conn.commit()#commit data to database

conn.close()#close the connection



#connect to database
conn = sqlite3.connect('data.db')

#create list
fileList = ('information.docx', 'Hello.txt','myImage.png',\
            'myMovie.mpg','Wolrd.txt','data.pdf','myPhoto.jpg')

#a for loop to look into the list 
for item in fileList:
    #an if statement to look only for items ending in '.txt'
    if item.endswith('.txt'):
        #include items into the data base
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files(col_files)\
                        VALUES(?)", (item,))
            print(item)#print the items
#close the connection
conn.close()





































