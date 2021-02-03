#!/usr/bin/env python
# coding: utf-8

# In[293]:


import csv 
import math
import statistics

# Creating a list for all the variables where the index for each list corresponds to one individual:

age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

# Opening our file and extracting each key to its corresponding list such as age, sex, etc..

with open('insurance.csv') as insurance:
    insurance_reader = csv.DictReader(insurance, delimiter=',')
    for row in insurance_reader:
        age.append(row["age"])
        sex.append(row["sex"])
        bmi.append(row["bmi"])
        children.append(row["children"])
        smoker.append(row["smoker"])
        region.append(row["region"])
        charges.append(float(row["charges"]))

# Which region has the highest insurance cost average?

# First let's create a Dictionary {Patient #: {age: , sex: , bmi: ,...}}:

def patients_num_dict(age, sex, bmi, children, smoker, region, charges):
    
    patient_dict = {}
    count = 0
    for i in range(1338):
        patient_dict[i] = {}
    for i in patient_dict:
        patient_dict[i] = {"age": age[count], "sex": sex[count], "bmi":bmi[count], 
                             "children": children[count], "smoker": smoker[count], 
                             "region": region[count], "charges": charges[count]}
        count += 1
    return patient_dict

patients = patient_num_dict(age, sex, bmi, children, smoker, region, charges)

# Now let's create a dictionary of all patients categorized by each region:

def northeast_dict(patients):
    northeast_dict = {}
    for i in patients:
        patient_region = patients[i]["region"]
        if patient_region == "northeast":
            northeast_dict[i] = patients[i]
    return northeast_dict

northeast_dict = northeast_dict(patients)

def northwest_dict(patients):
    northwest_dict = {}
    for i in patients:
        patient_region = patients[i]["region"]
        if patient_region == "northwest":
            northwest_dict[i] = patients[i]
    return northwest_dict

northwest_dict = northwest_dict(patients)

def southeast_dict(patients):
    southeast_dict = {}
    for i in patients:
        patient_region = patients[i]["region"]
        if patient_region == "southeast":
            southeast_dict[i] = patients[i]
    return southeast_dict

southeast_dict = southeast_dict(patients)

def southwest_dict(patients):
    southwest_dict = {}
    for i in patients:
        patient_region = patients[i]["region"]
        if patient_region == "southwest":
            southwest_dict[i] = patients[i]
    return southwest_dict

southwest_dict = southwest_dict(patients)

# Now let's find out the average cost of insurance for each of the regions:

class Charges:
    def southwest_charges(self, southwest_dict):
        self.southwest = southwest_dict
        southwest_charges = []
        for i in self.southwest:
            southwest_charges.append(self.southwest[i]["charges"])
        southwest_average = sum(southwest_charges) / len(southwest_charges)
        return southwest_average
    def southeast_charges(self, southeast_dict):
        self.southeast = southeast_dict
        southeast_charges = []
        for i in self.southeast:
            southeast_charges.append(self.southeast[i]["charges"])
        southeast_average = sum(southeast_charges) / len(southeast_charges)
        return southeast_average
    def northwest_charges(self, northwest_dict):
        self.northwest = northwest_dict
        northwest_charges = []
        for i in self.northwest:
            northwest_charges.append(self.northwest[i]["charges"])
        northwest_average = sum(northwest_charges) / len(northwest_charges)
        return northwest_average
    def northeast_charges(self, northeast_dict):
        self.northeast = northeast_dict
        northeast_charges = []
        for i in self.northeast:
            northeast_charges.append(self.northeast[i]["charges"])
        northeast_average = sum(northeast_charges) / len(northeast_charges)
        return northeast_average

charges = Charges()          
    
southwest_average = charges.southwest_charges(southwest_dict)
southeast_average = charges.southeast_charges(southeast_dict)
northwest_average = charges.northwest_charges(northwest_dict)
northeast_average = charges.northeast_charges(northeast_dict)

print("The average charges for patients located in the southwest region is: " + str(southwest_average))
print("The average charges for patients located in the southeast region is: " + str(southeast_average))
print("The average charges for patients located in the northwest region is: " + str(northwest_average))
print("The average charges for patients located in the northeast region is: " + str(northeast_average))
print(" ")
print("After retrieving and organizing the data from our 'insurance' file, I wanted to see if there's any correlation")
print("between the patients' region and their medical charges. As the numbers above project, the region has no major affect on the")
print("patients' average medical charges.")


# In[ ]:




