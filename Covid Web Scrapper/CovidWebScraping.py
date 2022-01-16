#add all of the imports needed
from bs4 import BeautifulSoup
from datetime import date
import requests as requests
import pandas as pd
import time
import csv
from tkinter import *

#create the variables used within the program
today = date.today()
filename = str(today)+".txt"
csvname = str(today)+".csv"
field=['Location','Reported Cases','Deaths','Recovered']

#function to find the Covid Data within the World
def WORLD(filename,csvname,field):
    #use request command to get the information from the link and store it into the variable
    html_text=requests.get('https://www.worldometers.info/coronavirus/#countries').text

    #use the bs4 import on the variable we got the link from
    soup = BeautifulSoup(html_text,'lxml')

    #find the specific data containing all of the cases under a specific class
    covidCases = soup.find_all('div',class_='maincounter-number')

    #create a variable to hold the cases
    cases=[]
    cases.append("World")

    #run a loop to get all of the cases from the html class
    for i in covidCases:
        data = i.find('span')
        cases.append(data.string)


    #open a file using the filename parameter we used to when calling the function
    f = open(filename,"w")

    #write the information we obtainted onto the txt file
    f.write("Cases In The World\n")
    f.write("Coronavirus Cases:"+cases[1]+"\n")
    f.write("Deaths:"+cases[2]+"\n")
    f.write("Recovered:"+cases[3]+"\n")
    f.close()

    #open a csv file using one of the parameters and write the information onto it as well
    with open(csvname,'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(field)
        csvwriter.writerow(cases)

        csvfile.close()
        return cases

#function to find the Covid Data within the United States
def USA(filename,csvname):
#this function follows all of the comments of the fucntion before but with a different link which leads to the United States' Covid Data

    html_text=requests.get('https://www.worldometers.info/coronavirus/country/us/').text


    soup = BeautifulSoup(html_text,'lxml')


    covidCases = soup.find_all('div',class_='maincounter-number')


    cases=[]
    cases.append("United States")
    for i in covidCases:
        data = i.find('span')
        cases.append(data.string)


    f = open(filename,"a")
    f.write("\n")
    f.write("Cases In The United States\n")
    f.write("Coronavirus Cases:"+cases[1]+"\n")
    f.write("Deaths:"+cases[2]+"\n")
    f.write("Recovered:"+cases[3]+"\n")
    f.close()

    with open(csvname,'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(cases)

        csvfile.close()
        return cases

#function to find the Covid Data within India
def INDIA(filename,csvname):
#this function follows all of the comments of the fucntion before but with a different link which leads to India's Covid Data
    html_text=requests.get('https://www.worldometers.info/coronavirus/country/india/').text

    soup = BeautifulSoup(html_text,'lxml')

    covidCases = soup.find_all('div',class_='maincounter-number')

    cases=[]
    cases.append("India")

    for i in covidCases:
        data = i.find('span')
        cases.append(data.string)


    f = open(filename,"a")
    f.write("\n")
    f.write("Cases In India\n")
    f.write("Coronavirus Cases:"+cases[1]+"\n")
    f.write("Deaths:"+cases[2]+"\n")
    f.write("Recovered:"+cases[3]+"\n")
    f.close()

    with open(csvname,'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(cases)

        csvfile.close()
        return cases

#function to find the Covid Data within Brazil
def BRAZIL(filename,csvname):
#this function follows all of the comments of the fucntion before but with a different link which leads to Brazil's Covid Data
    html_text=requests.get('https://www.worldometers.info/coronavirus/country/brazil/').text

    soup = BeautifulSoup(html_text,'lxml')

    covidCases = soup.find_all('div',class_='maincounter-number')

    cases=[]
    cases.append("Brazil")

    for i in covidCases:
        data = i.find('span')
        cases.append(data.string)


    f = open(filename,"a")
    f.write("\n")
    f.write("Cases In Brazil\n")
    f.write("Coronavirus Cases:"+cases[1]+"\n")
    f.write("Deaths:"+cases[2]+"\n")
    f.write("Recovered:"+cases[3]+"\n")
    f.close()

    with open(csvname,'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(cases)

        csvfile.close()
        return cases

#function to find the Covid Data within the United Kingdom
def UK(filename,csvname):
#this function follows all of the comments of the fucntion before but with a different link which leads to the United Kingdom's Covid Data

    html_text=requests.get('https://www.worldometers.info/coronavirus/country/uk/').text

    soup = BeautifulSoup(html_text,'lxml')

    covidCases = soup.find_all('div',class_='maincounter-number')

    cases=[]
    cases.append("United Kingdom")

    for i in covidCases:
        data = i.find('span')
        cases.append(data.string)


    f = open(filename,"a")
    f.write("\n")
    f.write("Cases In The United Kingdom\n")
    f.write("Coronavirus Cases:"+cases[1]+"\n")
    f.write("Deaths:"+cases[2]+"\n")
    f.write("Recovered:"+cases[3]+"\n")
    f.close()

    with open(csvname,'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(cases)

        csvfile.close()
        return cases

#function to find the Covid Data within Russia
def RUSSIA(filename,csvname):
#this function follows all of the comments of the fucntion before but with a different link which leads to Russia's Covid Data

    html_text=requests.get('https://www.worldometers.info/coronavirus/country/russia/').text

    soup = BeautifulSoup(html_text,'lxml')

    covidCases = soup.find_all('div',class_='maincounter-number')

    cases=[]
    cases.append("Russia")

    for i in covidCases:
        data = i.find('span')
        cases.append(data.string)


    f = open(filename,"a")
    f.write("\n")
    f.write("Cases In Russia\n")
    f.write("Coronavirus Cases:"+cases[1]+"\n")
    f.write("Deaths:"+cases[2]+"\n")
    f.write("Recovered:"+cases[3]+"\n")
    f.close()

    with open(csvname,'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(cases)

        csvfile.close()
        return cases

#this is the code that repeats the function call for the specified amount of time
if __name__ == '__main__':
    while True:
        world = []
        usa = []
        india = []
        brazil = []
        uk = []
        russia = []

        #calling all of the functions within the time loop
        world = WORLD(filename,csvname,field)
        usa = USA(filename,csvname)
        india = INDIA(filename,csvname)
        brazil = BRAZIL(filename,csvname)
        uk = UK(filename,csvname)
        russia = RUSSIA(filename,csvname)

        #create tkinter basics
        root = Tk()
        root.title("Coronavirus Cases Within The World")
        root.geometry("1050x500")
        root.configure(background='beige')

        #create the title for the first set of data
        world_title = Label(root,text="Total Number of Cases Of Covid Within The World",font=("Ariel,20,bold"),bg="beige",fg="black").grid(row=0,column=2,pady=20)

        #create the labels for where the data will go
        No = Label(root,text="No./Info",font=("Ariel,20,bold"),bg="beige",fg="black").grid(row=1,column=0)
        Location = Label(root,text="Location:",font=("Ariel,20,bold"),bg="beige",fg="black").grid(row=1,column=1,padx=50)
        Cases = Label(root,text="Cases:",font=("Ariel,20,bold"),bg="beige",fg="black").grid(row=1,column=2,padx=50)
        Death = Label(root,text="Deaths:",font=("Ariel,20,bold"),bg="beige",fg="black").grid(row=1,column=3,padx=50)
        Recovered = Label(root,text="Recovered:",font=("Ariel,20,bold"),bg="beige",fg="black").grid(row=1,column=4,padx=50)

        #input the data for World in the correct columns and rows
        worldnumber = Label(root,text="Total",font=("Ariel,20"),bg="beige",fg="black").grid(row=2,column=0,padx=50,pady=10)
        worldlocation = Label(root,text=world[0],font=("Ariel,20"),bg="beige",fg="black").grid(row=2,column=1,padx=50,pady=10)
        worldcases = Label(root,text=world[1],font=("Ariel,20"),bg="beige",fg="green").grid(row=2,column=2,padx=50,pady=10)
        worlddeath = Label(root,text=world[2],font=("Ariel,20"),bg="beige",fg="red").grid(row=2,column=3,padx=50,pady=10)
        worldrec = Label(root,text=world[3],font=("Ariel,20"),bg="beige",fg="blue").grid(row=2,column=4,padx=50,pady=10)

        #create a title for the top 5 countries with the highest cases
        title = Label(root,text="Top 5 Highest Countries With Covid 19",font=("Ariel,20,bold"),bg="beige",fg="black").grid(row=3,column=2,pady=20)

        #input the data for the United States under the correct columns and rows
        usanumber = Label(root,text="1",font=("Ariel,20"),bg="beige",fg="black").grid(row=4,column=0,padx=50,pady=10)
        usalocation = Label(root,text=usa[0],font=("Ariel,20"),bg="beige",fg="black").grid(row=4,column=1,padx=50,pady=10)
        usacases = Label(root,text=usa[1],font=("Ariel,20"),bg="beige",fg="green").grid(row=4,column=2,padx=50,pady=10)
        usadeath = Label(root,text=usa[2],font=("Ariel,20"),bg="beige",fg="red").grid(row=4,column=3,padx=50,pady=10)
        usarec = Label(root,text=usa[3],font=("Ariel,20"),bg="beige",fg="blue").grid(row=4,column=4,padx=50,pady=10)

        #input the data for India under the correct columns and rows
        indianumber = Label(root,text="2",font=("Ariel,20"),bg="beige",fg="black").grid(row=5,column=0,padx=50,pady=10)
        indialocation = Label(root,text=india[0],font=("Ariel,20"),bg="beige",fg="black").grid(row=5,column=1,padx=50,pady=5)
        indiacases = Label(root,text=india[1],font=("Ariel,20"),bg="beige",fg="green").grid(row=5,column=2,padx=50,pady=5)
        indiadeath = Label(root,text=india[2],font=("Ariel,20"),bg="beige",fg="red").grid(row=5,column=3,padx=50,pady=5)
        indiarec = Label(root,text=india[3],font=("Ariel,20"),bg="beige",fg="blue").grid(row=5,column=4,padx=50,pady=5)

        #input the data for Brazil under the correct columns and rows
        brazilnumber = Label(root,text="3",font=("Ariel,20"),bg="beige",fg="black").grid(row=6,column=0,padx=50,pady=10)
        brazillocation = Label(root,text=brazil[0],font=("Ariel,20"),bg="beige",fg="black").grid(row=6,column=1,padx=50,pady=10)
        brazilcases = Label(root,text=brazil[1],font=("Ariel,20"),bg="beige",fg="green").grid(row=6,column=2,padx=50,pady=10)
        brazildeath = Label(root,text=brazil[2],font=("Ariel,20"),bg="beige",fg="red").grid(row=6,column=3,padx=50,pady=10)
        brazilrec = Label(root,text=brazil[3],font=("Ariel,20"),bg="beige",fg="blue").grid(row=6,column=4,padx=50,pady=10)

        #input the data for the United Kingdom under the correct columns and rows
        uknumber = Label(root,text="4",font=("Ariel,20"),bg="beige",fg="black").grid(row=7,column=0,padx=50,pady=10)
        uklocation = Label(root,text=uk[0],font=("Ariel,20"),bg="beige",fg="black").grid(row=7,column=1,padx=50,pady=10)
        ukcases = Label(root,text=uk[1],font=("Ariel,20"),bg="beige",fg="green").grid(row=7,column=2,padx=50,pady=10)
        ukdeath = Label(root,text=uk[2],font=("Ariel,20"),bg="beige",fg="red").grid(row=7,column=3,padx=50,pady=10)
        ukrec = Label(root,text=uk[3],font=("Ariel,20"),bg="beige",fg="blue").grid(row=7,column=4,padx=50,pady=10)

        #input the data for Russia under the correct columns and rows
        russianumber = Label(root,text="5",font=("Ariel,20"),bg="beige",fg="black").grid(row=8,column=0,padx=50,pady=10)
        russialocation = Label(root,text=russia[0],font=("Ariel,20"),bg="beige",fg="black").grid(row=8,column=1,padx=50,pady=10)
        russiacases = Label(root,text=russia[1],font=("Ariel,20"),bg="beige",fg="green").grid(row=8,column=2,padx=50,pady=10)
        russiadeath = Label(root,text=russia[2],font=("Ariel,20"),bg="beige",fg="red").grid(row=8,column=3,padx=50,pady=10)
        russiarec = Label(root,text=russia[3],font=("Ariel,20"),bg="beige",fg="blue").grid(row=8,column=4,padx=50,pady=10)

        #setting the time needed to wait
        time_wait = 1440
        print("\n")
        #printing out how much time is needed for the code to refresh to the user
        wait_time = Label(root,text=f'Refreshing in about {time_wait//60} hours...',font=("Ariel,20,bold"),bg="beige",fg="black").grid(row=9,column=2,padx=10,pady=20)
        root.mainloop()
        #setting the program to sleep to the specified amound to time
        time.sleep(time_wait*60)
