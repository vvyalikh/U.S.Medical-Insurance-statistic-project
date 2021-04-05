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

count1 = 0
for items in bmi:
    count1 = count1 + 1

#print(age)

#print(count1)

#1.age groups
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
    
#print('People quantity in each age group: group_N1: ' + str(group_N1) + ', group_N2: '+ str(group_N2) + ', group_N3: ' + str(group_N3)+ ', group_N4: '+ str(group_N4) + ', group_N5: '+ str(group_N5) + ', group_N6: ' + str(group_N6))
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


count_charges_per_group = {k: len(v) for k,v in charges_vs_age_dict.items()}
#print(count_charges_per_group)
sum_charges_per_group = {k: round(sum(v),2) for k,v in charges_vs_age_dict.items()}
#print(sum_charges_per_group)
average_charges_per_group = {k: round(sum_charges_per_group[k] / count_charges_per_group[k],2) for k in count_charges_per_group if k in sum_charges_per_group}
#print(average_charges_per_group)


print('Average insurance charges for age group 35-44 is: ' + str(average_charges_per_group.get('charges_group_N3')))





#2.bmi groups
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




#print(count)



#print(charges_vs_region)

underweight = []
healthy_weight = []
overweight = []
obese = []


def bmi_index_range(lst):
  for items in bmi:
    if items < 18.5:
      underweight.append(items)
    elif items > 18.5 and items < 24.9:
      healthy_weight.append(items)
    elif items > 25.0 and items < 29.9:
      overweight.append(items)
    elif items > 30.0:
      obese.append(items)   
  return lst

#print(bmi_index_range(underweight))  

def bmi_vs_region_list():
  bmi_vs_region_dict = {'underweight':[],'healthy_weight':[],'overweight':[],'obese':[]}
  for keys,values in bmi:
    if keys < 18.5:
      bmi_vs_region_dict['underweight'].append(values)
    elif keys > 18.5 and keys < 24.9:
      bmi_vs_region_dict['healthy_weight'].append(values)
    elif keys > 25.0 and keys < 29.9:
      bmi_vs_region_dict['overweight'].append(values)
    elif keys > 30.0:
      bmi_vs_region_dict['obese'].append(values) 
  return bmi_vs_region_dict

#print(bmi_vs_region_list())
