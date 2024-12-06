def setColor(fg,bg):
        with open('C:/Users/TheSOmthing/elementconfig/config.txt','wt') as f:
                n = f.write("Color Code Data Stored Here\nFG\n"+fg+"\nBG\n" + bg)
        f.close()
