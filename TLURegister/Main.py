from Fetch_Page import * 
from Display_Subject import *
from register import *
semester()

semesterId = input("enter your choice: ")
Show_All_Subjects(subject(semesterId)[1])

subject_index = int(input("Enter the index of the subject you want to select: "))
show(subject(semesterId)[0],subject_index)

send(semesterId)
