import csv
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

#function to load insurance.csv data
def load_data(lst, csv_file, column_name):
    with open(csv_file) as csv_starter:
        csv_dict = csv.DictReader(csv_starter)
        for row in csv_dict:
            lst.append(row[column_name])
        return lst

#call function load_data
load_data(age, 'insurance.csv', 'age')
load_data(sex, 'insurance.csv', 'sex')
load_data(bmi, 'insurance.csv', 'bmi')
load_data(children, 'insurance.csv', 'children')
load_data(smoker, 'insurance.csv', 'smoker')
load_data(region, 'insurance.csv', 'region')
load_data(charges, 'insurance.csv', 'charges')

#1.bmi vs age
#function to convert string to integer
def age_integer(age):
    age_list = []
    for items in age:
        items = int(items)
        age_list.append(items)
    return age_list

age_int_list = (age_integer(age))
#print(age_int_list)

#most commonly used for survey categories
#group 18-24
group_N1 = 0
#group 25-34
group_N2 = 0
#group 35-44
group_N3 = 0
#group 45-54
group_N4 = 0
#group 55-64
group_N5 = 0
#group over 65
group_N6 = 0

for item in age_int_list:
    if item >= 18 and item <= 24:
      group_N1 = group_N1 + 1
    elif item >= 25 and item <= 34:
      group_N2 = group_N2 + 1
    elif item >= 35 and item <= 44:
      group_N3 = group_N3 + 1
    elif item >= 45 and item <= 54:
      group_N4 = group_N4 + 1 
    elif item >= 55 and item <= 64 :
      group_N5 = group_N5 + 1 
    elif item >= 65 :
      group_N6 = group_N6 + 1
    
print('Age groups: group_N1: ' + str(group_N1) + ', group_N2: '+ str(group_N2) + ', group_N3: ' + str(group_N3)+ ', group_N4: '+ str(group_N4) + ', group_N5: '+ str(group_N5) + ', group_N6: ' + str(group_N6))
#2.bmi vs sex
#3.bmi vs children
#4.bmi vs region
#5.bmi vs smoker status