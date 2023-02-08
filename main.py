import tkinter
from pyparsing import col
import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import filedialog
import csv

"""url = "https://www.ebay.com/itm/353832848728?_trkparms=amclksrc%3DITM%26aid%3D777008%26algo%3DPERSONAL.TOPIC%26ao%3D1%26asc%3D20200721145842%26meid%3D9c5f4ba013ef41b5961cb53f52770427%26pid%3D101259%26rk%3D1%26rkt%3D1%26itm%3D353832848728%26pmt%3D1%26noa%3D1%26pg%3D2380057%26algv%3DPersonalizedTopicsV2WithMetaOrganicPRecall%26brand%3DUnbranded&_trksid=p2380057.c101259.m47269&_trkparms=pageci%3Aab82615d-c0fd-11ec-bd70-3a62354c3424%7Cparentrq%3A4934a1e91800ad33af9dd008fffedd5a%7Ciid%3A2"
r = requests.get(url=url)
soup = BeautifulSoup(r.text, features="html.parser")"""

def getPrice():
    price = soup.find(id = "prcIsum")
    ptext = price.getText
    string = str(ptext)
    contentStart = string.find("content=")
    contentString = string[contentStart + 9:]
    contentEnd = contentString.find(" ")
    accPrice = contentString[0:contentEnd-1]
    accPrice = float(accPrice)
    return accPrice

def getTitle():
    title = soup.find(id = "vi-lkhdr-itmTitl")
    title = title.getText
    title = str(title)
    start = title.find(">")
    title = title[start + 1:]
    end = title.find("<")
    title = title[0:end]
    return title

def setLable():
    #get title
    url = linkEntry.get()
    r = requests.get(url=url)
    soup = BeautifulSoup(r.text, features="html.parser")
    title = soup.find(id = "vi-lkhdr-itmTitl")
    title = title.getText
    title = str(title)
    start = title.find(">")
    title = title[start + 1:]
    end = title.find("<")
    title = title[0:end]
    nameLable.config(text=f"Name: {title}")

    #get price
    price = soup.find(id = "prcIsum")
    ptext = price.getText
    string = str(ptext)
    contentStart = string.find("content=")
    contentString = string[contentStart + 9:]
    contentEnd = contentString.find(" ")
    accPrice = contentString[0:contentEnd-1]
    accPrice = float(accPrice)
    priceLable.config(text=f"Price: {accPrice}$")

    #profit
    userProfit = sellEntry.get()
    try:
        userProfit = int(userProfit)
        profit = userProfit - accPrice
        profitLable.config(text=f"Profit: {profit}$")
    except:
        profitLable.config(text="Profit: Something went wrong")


def openFile():
    #get title
    url = linkEntry.get()
    r = requests.get(url=url)
    soup = BeautifulSoup(r.text, features="html.parser")
    title = soup.find(id = "vi-lkhdr-itmTitl")
    title = title.getText
    title = str(title)
    start = title.find(">")
    title = title[start + 1:]
    end = title.find("<")
    title = title[0:end]

    price = soup.find(id = "prcIsum")
    ptext = price.getText
    string = str(ptext)
    contentStart = string.find("content=")
    contentString = string[contentStart + 9:]
    contentEnd = contentString.find(" ")
    accPrice = contentString[0:contentEnd-1]
    accPrice = float(accPrice)

    filePath = filedialog.askopenfilename()
    with open(filePath, 'a', newline='') as csvfile:
        content = csv.writer(csvfile)
        values = ['', '', '', '', '']
        values[0] = title
        values[1] = url
        values[2] = accPrice
        values[3] = sellEntry.get()
        userProfit = sellEntry.get()
        userProfit = int(userProfit)
        profit = userProfit - accPrice
        values[4] = profit
        content.writerow(values)

       # pass

#set window
window = Tk()
window.title("Profit Calculator")
window.geometry('700x700')
window.resizable(False, False)

#entry
linkFrame = Frame(window)
linkLable = Label(linkFrame, text="Enter Link:", font="none 12")
linkEntry = Entry(linkFrame, width=90)
linkLable.pack(side='left', padx = 10)
linkEntry.pack(pady=6)
linkFrame.pack(anchor='w')

#search and save
search = Button(window, text="Search Item", height=2, width=10, command=setLable)
save = Button(window, text="Save", height=2, width=10, command=openFile)
save.pack(side="bottom", pady=5)
search.pack(side="bottom", pady=5)

#enter sell price
sellFrame = Frame(window)
sellLable = Label(sellFrame, text="Sell Price: ", font="none 12")
sellEntry = Entry(sellFrame, width=10)
sellLable.pack(side='left', padx = 10, pady=10)
sellEntry.pack(pady=10)
sellFrame.pack(anchor='w')

#Name lable
nameLable = Label(window, text="Name:", font="none 12", wraplength=700)
nameLable.pack(anchor='w', pady=10, padx=10)

#price lable 
priceLable = Label(window, text="Price: ", font="none 12")
priceLable.pack(anchor='w', pady=10, padx=10)

#profit
profitLable = Label(window, text="Profit: ", font="none 12")
profitLable.pack(anchor='w', pady=10, padx=10)


window.mainloop()
#print(getTitle())

#print(ptext)
