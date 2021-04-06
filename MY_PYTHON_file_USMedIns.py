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

#sorting out data per age groups
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
    
#print('Age groups: group_N1: ' + str(group_N1) + ', group_N2: '+ str(group_N2) + ', group_N3: ' + str(group_N3)+ ', group_N4: '+ str(group_N4) + ', group_N5: '+ str(group_N5) + ', group_N6: ' + str(group_N6))

#to convert string to float
def charges_float(charges):
    charges_list = []
    for items in charges:
        items = float(items)
        charges_list.append(items)
    return charges_list

charges_float_list = (charges_float(charges))
#print(charges_float_list)

charges_vs_age = {key:value for key, value in zip(charges_float_list,age_int_list)}
#print(charges_vs_age)

#function to count age groups vs insurance charges corelation
def count_charges_vs_age():
  charges_vs_age_list = {'charges_group_N1':[],'charges_group_N2':[],'charges_group_N3':[],'charges_group_N4':[],'charges_group_N5':[] }
  for key, value in charges_vs_age.items():
    if value >= 18 and value <= 24:
      charges_vs_age_list['charges_group_N1'].append(key)
    elif value >= 25 and value <= 34:
      charges_vs_age_list['charges_group_N2'].append(key)
    elif value >= 35 and value <= 44:
      charges_vs_age_list['charges_group_N3'].append(key)
    elif value >= 45 and value <= 54:
      charges_vs_age_list['charges_group_N4'].append(key)
    elif value >= 55 and value <= 64:
      charges_vs_age_list['charges_group_N5'].append(key)
  return charges_vs_age_list
  
charges_vs_age_dict = count_charges_vs_age()
#print(charges_vs_age_dict)

#to count charges quantity per age group
count_charges_per_group = {k: len(v) for k,v in charges_vs_age_dict.items()}
#print(count_charges_per_group)

#to count sum of insurance charges per age group
sum_charges_per_group = {k: round(sum(v),2) for k,v in charges_vs_age_dict.items()}
#print(sum_charges_per_group)

#to count average insurance price per age group
average_charges_per_group = {k: round(sum_charges_per_group[k] / count_charges_per_group[k],2) for k in count_charges_per_group if k in sum_charges_per_group}
#print(average_charges_per_group)

print('Average insurance charges for age group 18-24 is: ' + str(average_charges_per_group.get('charges_group_N1')) + 
'; for age group 25-34 is: ' + str(average_charges_per_group.get('charges_group_N2')) + '; for age group 35-44 is: ' 
+ str(average_charges_per_group.get('charges_group_N3')) + '; for age group 45-54 is: '
 + str(average_charges_per_group.get('charges_group_N4')) + '; for age group 55-64 is: ' 
 + str(average_charges_per_group.get('charges_group_N5')))


#2.bmi groups

def bmi_float(bmi):
    bmi_float_list = []
    for items in bmi:
        items = float(items)
        bmi_float_list.append(items)
    return bmi_float_list

bmi_float_list1 = bmi_float(bmi)

def bmi_list():
  bmi_dict = {'underweight':[],'healthy_weight':[],'overweight':[],'obese':[]}
  for items in bmi_float_list1:
    if items <= 18.5:
      bmi_dict['underweight'].append(items)
    elif items >= 18.6 and items <= 24.9:
      bmi_dict['healthy_weight'].append(items)
    elif items >= 25.0 and items <= 29.9:
      bmi_dict['overweight'].append(items)
    elif items >= 30.0:
      bmi_dict['obese'].append(items) 
  return bmi_dict

bmi_groups_dict = bmi_list()

count_people_per_group = {k: len(v) for k,v in bmi_groups_dict.items()}
print(count_people_per_group)

count_part_of_obese_patients = round((705 / 1318)*100, 0)
#print(count_part_of_obese_patients)
count_part_of_healthy_weight_patients = round((221 / 1318)*100, 0)
#print(count_part_of_healthy_weight_patients)

#bmi vs insurance charge correlation
charges_vs_bmi = {key:value for key, value in zip(charges_float_list,bmi_float_list1)}
#print(charges_vs_bmi)

def count_charges_vs_bmi():
  charges_vs_bmi_list = {'charges_underweight_group':[],'charges_healthy_weight_group':[],'charges_overweight_group':[],'charges_obese_group':[]}
  for key, value in charges_vs_bmi.items():
    if value <= 18.5:
      charges_vs_bmi_list['charges_underweight_group'].append(key)
    elif value >= 18.6 and value <= 24.9:
      charges_vs_bmi_list['charges_healthy_weight_group'].append(key)
    elif value >= 25 and value <= 29.9:
      charges_vs_bmi_list['charges_overweight_group'].append(key)
    elif value >= 30:
      charges_vs_bmi_list['charges_obese_group'].append(key)
  return charges_vs_bmi_list


charges_vs_bmi_dict = count_charges_vs_bmi()
#print(charges_vs_bmi_dict)

count_charges_per_bmi_group = {k: len(v) for k,v in charges_vs_bmi_dict.items()}
#print(count_charges_per_bmi_group)
sum_charges_per_bmi_group = {k: round(sum(v),2) for k,v in charges_vs_bmi_dict.items()}
#print(sum_charges_per_bmi_group)
average_charges_per_bmi_group = {k: round(sum_charges_per_bmi_group[k] / count_charges_per_bmi_group[k],2) for k in count_charges_per_bmi_group if k in sum_charges_per_bmi_group}
#print(average_charges_per_bmi_group)

#3.have children vs child free












#4.region groups
def unique_regions(region):
    unique_region = []
    for item in region:
        if item not in unique_region:
            unique_region.append(item)
    return unique_region

#print(unique_regions(region))
# in insurance.csv presented 4 regions southwest,southeast,northwest,northeast