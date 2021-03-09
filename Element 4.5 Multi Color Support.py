import tkinter as tk
import tkinter.font as tkFont
from tkinter import colorchooser
from PIL import ImageTk, Image
import requests
from io import BytesIO
import time
from elementVariable import elementInfo, Periods, Groups
from elementNLP import autoCorrect
from colorData import setColor
#Debug Module
import pdb

switchCondition = 0

window = tk.Tk()
bgColor = "#2a2a2a"
fgColor = "#00fcff"


 
with open("C:/Users/TheSOmthing/elementconfig/config.txt") as fp:
    for i, line in enumerate(fp):
        if i == 2:
            fgColor = line.lower()
        elif i == 4:
            bgColor = line.lower()
    fp.close()
    
##background color
window.configure(bg=bgColor)
##application name
window.title("Periodic Table of Element Search")
##application icon

bgColor = bgColor[0:7]
fgColor = fgColor[0:7]

fontStyle = tkFont.Font(family="Courier", size=9)

img_url = 'https://raw.githubusercontent.com/Datlightning/PythonImage/main/elementLogo.png'
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
window.iconphoto(False, img)

exitFrame = tk.LabelFrame(window, padx=10, pady=10, fg=fgColor, bg=bgColor)
exitFrame.pack(side="right", pady=10, padx=10, anchor='n')

tabSwitch = tk.LabelFrame(window, padx=5, pady=5, fg=fgColor, bg=bgColor)
tabSwitch.pack(pady=10, padx=10, anchor='w', side = 'top')

deleteFrame = tk.LabelFrame(window, padx=0, pady=0, bg=bgColor)
deleteFrame.pack(pady=10, padx=10, side='left', anchor = 'n')


exFrame = tk.LabelFrame(window, padx=10, pady=10, fg=fgColor, bg=bgColor)
exFrame.pack(side="right", pady=20, padx=20, anchor='s')
exFrame.configure(width=150, height=80)
exFrame.pack_propagate(False)

pictureFrame = tk.LabelFrame(window, padx=10, pady=10, fg=fgColor, bg=bgColor)
pictureFrame.pack(pady=20, padx=20)


frame = tk.LabelFrame(window, font=fontStyle, text="Type in the Element Name, Number or Symbol.", padx=10, pady=10,
                      fg=fgColor, bg=bgColor)
frame.pack(pady=20, padx=20, side='bottom', anchor='center')
frame.configure(width=400, height=90)
frame.pack_propagate(False)

outputFrame = tk.LabelFrame(window, padx=10, pady=10, fg=fgColor, bg=bgColor)
outputFrame.pack(pady=20, padx=20)

e = tk.Entry(frame, bg=fgColor, fg="black")
e.pack()
e.pack_propagate(False)

position = 1000
switchModeVar = 0
switchNumVar = 1


def switchNum():
    global switchNumVar
    if switchNumVar == 0:
        weightOrNumber.configure(text='Searching Using\n Atomic Number')
        switchNumVar = 1
    elif switchNumVar == 1:
        weightOrNumber.configure(text='Searching Using\n Atomic Weight')
        switchNumVar = 0
def s():
    global switchModeVar
    global switchCondition
    global position
    global outputFrame
    global pictureFrame

    if switchCondition == 0:
        switchPicture.configure(text='Picture Mode Activated')
        switchPicture['state'] = 'disabled'
        switchButton['state'] = 'normal'
        switchButton.configure(text='Switch to Text')
        outputFrame.destroy()
        position = 1000
        outputFrame = tk.LabelFrame(window, padx=10, pady=10, fg=fgColor, bg=bgColor)
        outputFrame.pack(pady=20, padx=20)
        switchModeVar = 1

        switchCondition = 1
    elif switchCondition == 1:
        switchButton.configure(text='Text Mode Activated')
        switchButton['state'] = 'disabled'
        switchPicture['state'] = 'normal'
        switchPicture.configure(text='Switch to Pictures')
        pictureFrame.destroy()
        pictureFrame = tk.LabelFrame(window, padx=10, pady=10, fg=fgColor, bg=bgColor)
        pictureFrame.pack(pady=20, padx=20)
        switchModeVar = 0

        switchCondition = 0

    window.update_idletasks()


def Click():
    if e.get() == "":
        return

    global position
    global myLabel
    global switchCondition
    global pictureFrame
    global switchNumVar
    b['state'] = 'disabled'
    window.update_idletasks()
    ##Different atomic weights



    ##This function located the row of each element when necessary
    def periodCheck(periodNumber):
        if periodNumber in Periods.period1:
            return "1st"
        elif periodNumber in Periods.period2:
            return "2nd"
        elif periodNumber in Periods.period3:
            return "3rd"
        elif periodNumber in Periods.period4:
            return "4th"
        elif periodNumber in Periods.period5:
            return "5th"
        elif periodNumber in Periods.period6:
            return "6th"
        elif periodNumber in Periods.period7:
            return "7th"

    ##This function located the column of each element when necessary
    def groupCheck(periodNumber):
        if periodNumber in Groups.group1:
            return "1A"
        elif periodNumber in Groups.group2:
            return "2A (Alkaline earth Metals)"
        elif periodNumber in Groups.group3:
            return "3B"
        elif periodNumber in Groups.group4:
            return "4B"
        elif periodNumber in Groups.group5:
            return "5B"
        elif periodNumber in Groups.group6:
            return "6B"
        elif periodNumber in Groups.group7:
            return "7B"
        elif periodNumber in Groups.group8:
            return "8B"
        elif periodNumber in Groups.group9:
            return "8B"
        elif periodNumber in Groups.group10:
            return "8B"
        elif periodNumber in Groups.group11:
            return "1B (Coin-age metals)"
        elif periodNumber in Groups.group12:
            return "2B"
        elif periodNumber in Groups.group13:
            return "3B (Triels)"
        elif periodNumber in Groups.group14:
            return "4A (Tetrels)"
        elif periodNumber in Groups.group15:
            return "5A (Pnictogens)"
        elif periodNumber in Groups.group16:
            return "6A (Chalcogens)"
        elif periodNumber in Groups.group17:
            return "7A (Halogens)"
        elif periodNumber in Groups.group18:
            return "8A (Noble Gases)"

    def pictureInfo():
        global pictureFrame
        pictureFrame.destroy()
        nameFont = tkFont.Font(family="Courier", size=20)
        font = tkFont.Font(family="Courier", size=10)
        largeFont = tkFont.Font(family="Courier", size=60)
        ElementName = elementInfo.elementName[elementId]
        ElementNumber = str(elementInfo.possibleAnswers[elementId])
        ElementWeight = str(elementInfo.elementList[elementId])
        ElementSymbol = elementInfo.elementSymbol[elementId]
        ElementNuetrons = str(elementInfo.elementList[elementId] - (elementId + 1))
        pictureFrame = tk.LabelFrame(window, padx=15, pady=15, fg=fgColor, bg=bgColor)
        pictureFrame.pack(pady=20, padx=20)
        pictureFrame.configure(width='270', height='270')
        pictureFrame.pack_propagate(False)
        elementLabelBottomText = tk.Label(pictureFrame, font=font, fg=fgColor, bg=bgColor,
                                          text="Atomic Mass: " + ElementWeight + "\n Protons: " + ElementNumber + "\n Electrons: " + ElementNumber + "\n Neutrons: " + ElementNuetrons)
        elementLabelBottomText.pack(side='bottom')

        elementLabelName = tk.Label(pictureFrame, font=nameFont, fg=fgColor, bg=bgColor,
                                    text=ElementName)
        elementLabelName.pack(side='bottom')

        elementLabelNumber = tk.Label(pictureFrame, font=nameFont, fg=fgColor, bg=bgColor,
                                      text=ElementNumber)
        elementLabelNumber.pack(side='top', anchor='w')

        elementLabelSymbol = tk.Label(pictureFrame, font=largeFont, fg=fgColor, bg=bgColor,
                                      text=ElementSymbol)
        elementLabelSymbol.pack(side='top', pady=10)
    answer = e.get()
    e.delete(0, 'end')
    i = 0
    elementId = 0
    global pictureFrame
    def text(answer):
        text=(str(elementInfo.elementName[answer]) + " has the symbol " + str(
                                           elementInfo.elementSymbol[answer]) + ", the element number is " + str(
                                           answer + 1) + ", the atomic mass is " + str(
                                           elementInfo.elementList[answer]) + " (Rounded to the Nearest Integer), it has " + str(
                                           answer + 1) + " protons," + " it has " + str(
                                           answer + 1) + " electrons and " + str(elementInfo.elementList[answer] - (
                                                   answer + 1)) + " neutrons. \nThe element is in the " + str(
                                           periodCheck(answer + 1)) + " period and is in group " + str(
                                           groupCheck(answer + 1)) + ".")
        return str(text)
    def hydrogen(answer):
        text=(str(elementInfo.elementName[answer]) + " has the symbol " + str(
                                           elementInfo.elementSymbol[answer]) + ", the element number is " + str(
                                           answer + 1) + ", the atomic mass is " + str(
                                           elementInfo.elementList[answer]) + " (Rounded to the Nearest Integer), it has " + str(
                                           answer + 1) + " proton," + " it has " + str(
                                           answer + 1) + " electron and " + str(elementInfo.elementList[answer] - (
                                                   answer + 1)) + " neutrons. \nThe element is in the " + str(
                                           periodCheck(answer + 1)) + " period and is in group " + str(
                                           groupCheck(answer + 1)) + ".")
        return str(text)
    def latinNames(name,answer):
        text=(str(name)+" is the latin name for " + str(elementInfo.elementName[answer]) + ". It has the symbol " + str(
                                           elementInfo.elementSymbol[answer]) + ", the element number is " + str(
                                           answer + 1) + ", the atomic mass is " + str(
                                           elementInfo.elementList[answer]) + " (Rounded to the Nearest Integer), it has " + str(
                                           answer + 1) + " protons," + " it has " + str(
                                           answer + 1) + " electrons and " + str(elementInfo.elementList[answer] - (
                                                   answer + 1)) + " neutrons. \nThe element is in the " + str(
                                           periodCheck(answer + 1)) + " period and is in group " + str(
                                           groupCheck(answer + 1)) + ".")
        return str(text)
    x = 0
    testTry = 0
    fontSmall = tkFont.Font(family="Courier", size=9)
    try:
        int(answer)
        testTry = 1
    except ValueError:
        testTry = 0
    if testTry == 1:
        x = answer
        x = int(x)
        ##The input is the Atomic Number
        if switchNumVar == 1:
            if x == 1:
                if switchCondition == 1:
                    pictureInfo()
                else:
                    myLabel = tk.Label(outputFrame, font=fontSmall, fg=fgColor, bg=bgColor,
                                       text=hydrogen(elementId))
                    myLabel.grid(row=position, column=0)
            elif x <= 118 and x >= 1:
                elementId = x - 1
                if switchCondition == 1:
                    pictureInfo()
                else:
                    myLabel = tk.Label(outputFrame, font=fontSmall, fg=fgColor, bg=bgColor,
                                       text=text(elementId))
                    myLabel.grid(row=position, column=0)
            else:
                b.configure(text="Your Number does not exist. Please try again.")
                window.update_idletasks()
                b.pack_propagate(False)
                window.update_idletasks()
                time.sleep(1)
                b.configure(text="Search")
                window.update_idletasks()
        else:
            if x == 1:
                if switchCondition == 1:
                    pictureInfo()
                else:
                    myLabel = tk.Label(outputFrame, font=fontSmall, fg=fgColor, bg=bgColor,
                                       text=hydrogen(elementId))
                    myLabel.grid(row=position, column=0)
            elif x >= 1:
                if x in elementInfo.elementList:
                    for something in range(118):
                        if elementInfo.elementList[something] == x:
                            elementId = something
                        if switchCondition == 1:
                            pictureInfo()
                        else:
                            myLabel = tk.Label(outputFrame, font=fontSmall, fg=fgColor, bg=bgColor,
                                           text=text(elementId))
                            myLabel.grid(row=position, column=0)
                else:
                    greatestLess = 0
                    smallestMore = 0
                    for another in range(118):
                        if elementInfo.elementList[another] < x and elementInfo.elementList[another] > smallestMore:
                            smallestMore = elementInfo.elementList[another]
                    for another in range(118):
                        if elementInfo.elementList[another] > x:
                            greatestLess = elementInfo.elementList[another]
                            break
                    
                    if abs(greatestLess - x) < abs(smallestMore - x):
                        x = greatestLess
                    else:
                        x = smallestMore
                    for something in range(118):
                        if elementInfo.elementList[something] == x:
                            elementId = something
                        if switchCondition == 1:
                            pictureInfo()
                        else:
                            myLabel = tk.Label(outputFrame, font=fontSmall, fg=fgColor, bg=bgColor,
                                               text=text(elementId))
                            myLabel.grid(row=position, column=0)
            else:
                b.configure(text="Your Number does not exist. Please try again.")
                window.update_idletasks()
                b.pack_propagate(False)
                window.update_idletasks()
                time.sleep(1)
                b.configure(text="Search")
                window.update_idletasks()
    elif len(answer) <= 2 and len(answer) > 0:
        element = answer
        ##The input is the Atomic Symbol
        while i < 118:
            if element.lower() == "h":
                elementId = 0
                i = 118
                if switchCondition == 1:
                    pictureInfo()
                else:
                    myLabel = tk.Label(outputFrame, font=fontSmall, fg=fgColor, bg=bgColor,
                                       text=hydrogen(elementId))
                    myLabel.grid(row=position, column=0)
            elif element.lower() == elementInfo.elementSymbol[i].lower():
                elementId = i
                i = 118
                if switchCondition == 1:
                    pictureInfo()
                else:
                    myLabel = tk.Label(outputFrame, font=fontSmall, fg=fgColor, bg=bgColor,
                                       text=text(elementId))
                    myLabel.grid(row=position, column=0)
            elif i == 117:
                window.update_idletasks()
                b.configure(text="Your Symbol does not exist. Please try again.")
                b.pack_propagate(False)
                window.update_idletasks()
                time.sleep(1)
                b.configure(text="Search")
                window.update_idletasks()
                break
            else:
                i += 1

    else:
        ##The input is the Element Name
        element = autoCorrect(answer, elementInfo.allNames)
        i = 0
        while i < 118:
            if element.lower() == "hydrogen":
                elementId = 0
                i = 118
                if switchCondition == 1:
                    pictureInfo()
                else:
                    myLabel = tk.Label(outputFrame, font=fontSmall, fg=fgColor, bg=bgColor,
                                       text=hydrogen(elementId))
                    myLabel.grid(row=position, column=0, padx=0)
            elif element.lower() == elementInfo.elementName[i].lower():
                elementId = i
                i = 118
                if switchCondition == 1:
                    pictureInfo()


                else:
                    myLabel = tk.Label(outputFrame, font=fontSmall, fg=fgColor, bg=bgColor,
                                       text=text(elementId))
                    myLabel.grid(row=position, column=0, padx=0)
            elif element.lower() == "aluminium":
                elementId = 12
                i = 118
                if switchCondition == 1:
                    pictureInfo()
                else:
                    myLabel = tk.Label(outputFrame, font=fontSmall, fg=fgColor, bg=bgColor,
                                       text=text(elementId))
                    myLabel.grid(row=position, column=0, padx=0)
            else:
                i += 1
                ##The input is not the Element name, symbol or number.
                if i == 118:
                    j = 0
                    latinIndex = 0
##                    pdb.set_trace()
                    while True:
                        if j >= 118:
                            window.update_idletasks()
                            b.configure(text="Your answer was not recognized. Please try again")
                            window.update_idletasks()
                            time.sleep(1)
                            b.configure(text="Search")
                            break
                        elif element.lower() == elementInfo.latinNames[j].lower():
                            latinIndex = j
                            if switchCondition == 1:
                                elementId = latinIndex
                                pictureInfo()
                            else:
                                myLabel = tk.Label(outputFrame, font=fontSmall, fg=fgColor, bg=bgColor,
                                               text=latinNames(elementInfo.latinNames[j],latinIndex))
                                myLabel.grid(row=position, column=0, padx=0)
##                            pdb.set_trace()
                            break
                        
                        j += 1

    b['state'] = 'normal'
    position -= 1
    window.update_idletasks()


def fillerFunc(event):
    b.config(relief="sunken")
    b.config(fg=bgColor, bg=fgColor)
    window.update_idletasks()
    time.sleep(.075)
    b.invoke()
    b.config(relief="raised")
    b.config(fg=fgColor, bg=bgColor)
    window.update_idletasks()

window.bind('<Return>', fillerFunc)

def Clear():
    global outputFrame
    global pictureFrame
    if switchCondition == 0:
        outputFrame.destroy()
        position = 1000
        outputFrame = tk.LabelFrame(window, padx=10, pady=10, fg=fgColor, bg=bgColor)
        outputFrame.pack(pady=20, padx=20)
    elif switchCondition == 1:
        pictureFrame.destroy()
        pictureFrame = tk.LabelFrame(window, padx=10, pady=10, fg=fgColor, bg=bgColor)
        pictureFrame.pack(pady=20, padx=20)

def anotherFillerFunc(event):
    destroy.config(relief="sunken")
    window.update_idletasks()
    time.sleep(.075)
    destroy.invoke()
    destroy.config(relief="raised")
    window.update_idletasks()

window.bind('<Escape>', anotherFillerFunc)

def switchMode(event):
    global switchModeVar
    if switchModeVar == 0:
        switchPicture.config(relief="sunken")
        switchPicture.config(fg=bgColor, bg=fgColor)
        window.update_idletasks()
        time.sleep(.075)
        switchPicture.invoke()
        switchPicture.config(relief="raised")
        switchPicture.config(fg=fgColor, bg=bgColor)
        window.update_idletasks()
        switchModeVar = 1
    else:
        switchButton.config(relief="sunken")
        switchButton.config(fg=bgColor, bg=fgColor)
        window.update_idletasks()
        time.sleep(.075)
        switchButton.invoke()
        switchButton.config(relief="raised")
        switchButton.config(fg=fgColor, bg=bgColor)
        window.update_idletasks()
        switchModeVar = 0
window.bind('<Tab>', switchMode)

def Close():
    window.destroy()
    exit()

b = tk.Button(frame,font=fontStyle, text="Search", justify='center', pady=15, padx=5, command=Click, fg=fgColor, bg=bgColor,
              activeforeground=bgColor, activebackground=fgColor)
b.pack(side='bottom', anchor='center', pady=5)
window.update_idletasks()

switchPicture = tk.Button(tabSwitch,font=fontStyle, text="Switch to Pictures", justify='center', pady=0, padx=0, command=s,
                          fg=fgColor, bg=bgColor, activeforeground=bgColor, activebackground=fgColor)
switchPicture.pack(pady=0, padx=5, side='left', anchor='w')

switchButton = tk.Button(tabSwitch,font=fontStyle, text="Switch to Text", justify='center', pady=0, padx=0, command=s,fg=fgColor, bg=bgColor, activeforeground=bgColor, activebackground=fgColor)
switchButton.pack(pady=0, padx=5, side='left', anchor='w')
switchButton.configure(text='Text Mode Activated')
switchButton['state'] = 'disabled'
switchCondition = 0

img_url2 = 'https://raw.githubusercontent.com/Datlightning/PythonImage/main/trashcan.png'
response2 = requests.get(img_url2)
img_data2 = response2.content
img2 = ImageTk.PhotoImage(Image.open(BytesIO(img_data2)))

destroy = tk.Button(deleteFrame,font=fontStyle, command=Clear, pady=0, padx=0, bg=fgColor, fg=bgColor,
                    activeforeground=bgColor, activebackground=fgColor)
destroy.pack(padx=10, pady=10, side="top", anchor='e')
destroy.config(height='25', width='25')
destroy.pack_propagate(0)
destroy.config(image=img2)
exitFont = tkFont.Font(family="Candara", size=12)

exits = tk.Button(exitFrame, font=exitFont, text="Close", command=Close, pady=0, padx=0, fg=fgColor, bg=bgColor,
                  activeforeground=bgColor, activebackground=fgColor)
exits.pack(padx=0, pady=0)

weightOrNumber = tk.Button(exFrame, font=fontStyle,command = switchNum, text="Searching Using:\n Atomic Number", pady=20, padx=0, fg=fgColor, bg=bgColor,
                  activeforeground=bgColor, activebackground=fgColor)
weightOrNumber.pack(padx = 0, pady = 0)

#recreates the entire app. 
def reColor():
    global exitFrame
    global colorSwap
    global weightOrNumber
    global exits
    global exFrame
    global deleteFrame
    global b
    global e
    global destroy
    global switchButton
    global switchPicture
    global frame
    global pictureFrame
    global outputFrame
    global tabSwitch
    global img2
    exitFrame.destroy()
    colorSwap.destroy()
    weightOrNumber.destroy()
    exits.destroy()
    exFrame.destroy()
    deleteFrame.destroy()
    b.destroy()
    e.destroy()
    destroy.destroy()
    switchButton.destroy()
    switchPicture.destroy()
    frame.destroy()
    pictureFrame.destroy()
    outputFrame.destroy()
    tabSwitch.destroy()
    window.configure(bg=bgColor)

    exitFrame = tk.LabelFrame(window, padx=10, pady=10, fg=fgColor, bg=bgColor)
    exitFrame.pack(side="right", pady=10, padx=10, anchor='n')

    tabSwitch = tk.LabelFrame(window, padx=5, pady=5, fg=fgColor, bg=bgColor)
    tabSwitch.pack(pady=10, padx=10, anchor='w', side = 'top')

    deleteFrame = tk.LabelFrame(window, padx=0, pady=0, bg=bgColor)
    deleteFrame.pack(pady=10, padx=10, side='left', anchor = 'n')


    exFrame = tk.LabelFrame(window, padx=10, pady=10, fg=fgColor, bg=bgColor)
    exFrame.pack(side="right", pady=20, padx=20, anchor='s')
    exFrame.configure(width=150, height=80)
    exFrame.pack_propagate(False)

    pictureFrame = tk.LabelFrame(window, padx=10, pady=10, fg=fgColor, bg=bgColor)
    pictureFrame.pack(pady=20, padx=20)


    frame = tk.LabelFrame(window, font=fontStyle, text="Type in the Element Name, Number or Symbol.", padx=10, pady=10,
                          fg=fgColor, bg=bgColor)
    frame.pack(pady=20, padx=20, side='bottom', anchor='center')
    frame.configure(width=400, height=90)
    frame.pack_propagate(False)

    outputFrame = tk.LabelFrame(window, padx=10, pady=10, fg=fgColor, bg=bgColor)
    outputFrame.pack(pady=20, padx=20)

    e = tk.Entry(frame, bg=fgColor, fg="black")
    e.pack()
    e.pack_propagate(False)
    b = tk.Button(frame,font=fontStyle, text="Search", justify='center', pady=15, padx=5, command=Click, fg=fgColor, bg=bgColor,
              activeforeground=bgColor, activebackground=fgColor)
    b.pack(side='bottom', anchor='center', pady=5)
    window.update_idletasks()

    switchPicture = tk.Button(tabSwitch,font=fontStyle, text="Switch to Pictures", justify='center', pady=0, padx=0, command=s,
                              fg=fgColor, bg=bgColor, activeforeground=bgColor, activebackground=fgColor)
    switchPicture.pack(pady=0, padx=5, side='left', anchor='w')

    switchButton = tk.Button(tabSwitch,font=fontStyle, text="Switch to Text", justify='center', pady=0, padx=0, command=s,fg=fgColor, bg=bgColor, activeforeground=bgColor, activebackground=fgColor)
    switchButton.pack(pady=0, padx=5, side='left', anchor='w')
    switchButton.configure(text='Text Mode Activated')
    switchButton['state'] = 'disabled'
    switchCondition = 0

    img_url2 = 'https://raw.githubusercontent.com/Datlightning/PythonImage/main/trashcan.png'
    response2 = requests.get(img_url2)
    img_data2 = response2.content
    img2 = ImageTk.PhotoImage(Image.open(BytesIO(img_data2)))

    destroy = tk.Button(deleteFrame,font=fontStyle, command=Clear, pady=0, padx=0, bg=fgColor, fg=bgColor,
                        activeforeground=bgColor, activebackground=fgColor)
    destroy.pack(padx=10, pady=10, side="top", anchor='e')
    destroy.config(height='25', width='25')
    destroy.pack_propagate(0)
    destroy.config(image=img2)
    exitFont = tkFont.Font(family="Candara", size=12)

    exits = tk.Button(exitFrame, font=exitFont, text="Close", command=Close, pady=0, padx=0, fg=fgColor, bg=bgColor,
                      activeforeground=bgColor, activebackground=fgColor)
    exits.pack(padx=0, pady=0)

    weightOrNumber = tk.Button(exFrame, font=fontStyle,command = switchNum, text="Searching Using:\n Atomic Number", pady=20, padx=0, fg=fgColor, bg=bgColor,
                      activeforeground=bgColor, activebackground=fgColor)
    weightOrNumber.pack(padx = 0, pady = 0)

    colorSwap = tk.Button(tabSwitch, font=fontStyle, text="Edit Color Scheme", command=editColor, pady=0, padx=0, fg=fgColor, bg=bgColor,
                      activeforeground=bgColor, activebackground=fgColor)
    colorSwap.pack(padx = 5, pady = 0, side = 'left')

closeLock = 0
def editColor():
    global closeLock
    global switchCondition
    newColor = tk.Toplevel()
    newColor.iconphoto(False, img)
    ##background color
    newColor.configure(bg=bgColor)
    ##application name
    newColor.title("Change the Color Scheme")
    disable()
    
    def closeNew():
        global closeLock
        global switchCondition

        if closeLock == 1:
            newColor.destroy()
            closeLock = 0
            reColor()
            
        else:
            newColor.destroy()
            b['state'] = 'normal'
            e['state'] = 'normal'
            weightOrNumber['state'] = 'normal'
            colorSwap['state'] = 'normal'
            if switchCondition == 1:
                switchButton['state'] = 'disabled'
                switchPicture['state'] = 'normal'
            elif switchCondition == 0:
                switchButton['state'] = 'normal'
                switchPicture['state'] = 'disabled'
    close = tk.Button(newColor, font=fontStyle, text="Close", command=closeNew, pady=5, padx=5, fg=fgColor, bg=bgColor,
                  activeforeground=bgColor, activebackground=fgColor)
    close.pack(padx = 0, pady = 30)

    fgSwap = tk.Button(newColor, font=fontStyle, text="Change Foreground", command=colorWheelFG, pady=5, padx=5, fg=fgColor, bg=bgColor,
                  activeforeground=bgColor, activebackground=fgColor)
    fgSwap.pack(padx = 30, pady = 30, side='left')
    bgSwap = tk.Button(newColor, font=fontStyle, text="Change Background", command=colorWheelBG, pady=5, padx=5, fg=fgColor, bg=bgColor,
                  activeforeground=bgColor, activebackground=fgColor)
    bgSwap.pack(padx = 30, pady = 30, side='right')


def colorWheelFG():
    global fgColor
    global closeLock
    fgColor = colorchooser.askcolor()[1]
    setColor(fgColor,bgColor)
    closeLock = 1
def colorWheelBG():
    global bgColor
    global closeLock
    bgColor = colorchooser.askcolor()[1]
    setColor(fgColor,bgColor)
    closeLock = 1

def disable():
    b['state'] = 'disabled'
    e['state'] = 'disabled'
    weightOrNumber['state'] = 'disabled'
    colorSwap['state'] = 'disabled'
    switchButton['state'] = 'disabled'
    switchPicture['state'] = 'disabled'
    


colorSwap = tk.Button(tabSwitch, font=fontStyle, text="Edit Color Scheme", command=editColor, pady=0, padx=0, fg=fgColor, bg=bgColor,
                  activeforeground=bgColor, activebackground=fgColor)
colorSwap.pack(padx = 5, pady = 0, side = 'left')

window.update_idletasks()
window.mainloop()



