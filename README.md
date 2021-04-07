# U.S.Medical-Insurance-statistic-project

This is CODECADEMY off-platform project

I made statistic analyze based on data provided (insurance.csv):
1. age groups vs insurance charges correlation
2. bmi groups vs insurance charges correlation
3. have kids / no kids vs insurance charges correlation
4. regions vs insurance charges correlation

During my research I used csv module and functions to clean data and to find out
if exist any correlation mentioned above.

1. age
to make my analyze more readable I've separated all people
on groups. Most commonly used for survey categories
* 18-24   group_N1
* 25-34   group_N2
* 35-44   group_N3
* 45-54   group_N4
* 55-64   group_N5
* over 65 group_N6

After data separation I've realized that in data provided no people over 65 years old,
so I will not use group_N6 in my further research.

Age groups: group_N1: 278, group_N2: 271, group_N3: 260, group_N4: 287, group_N5: 242, group_N6: 0

Next what I've investigated, what is average price of insurance for each average group.

Average insurance charges 
* for age group 18-24 is: 9037.95; 
* for age group 25-34 is: 10352.39; 
* for age group 35-44 is: 13134.17; 
* for age group 45-54 is: 15853.93; 
* for age group 55-64 is: 18513.28

As we can see, there are direct correlation berween age and insurance charges, i.e.
less charges for younger persons and higher charges for older persons.

2.bmi
I sorted all people on four groups:
'underweight': 21,'healthy_weight': 221,'overweight': 377,'obese': 706.

Acording to calculation results, 53% of researh group are obese and
only 17% have healthy BMI rate.

Then I've calculated average price for each BMI rate group:
*  'charges_underweight_group': 8657.62 
*  'charges_healthy_weight_group': 10404.9
*  'charges_overweight_group': 10993.99
*  'charges_obese_group': 15572.04

As we can see most significant price difference in 'obese' group, but almost not between
'overweight' and 'healthy_weight' groups. From that we can conclude, that only
people with really hight BMI are 'concern group' for insurance companies.

3. have kids / no kids
I just filteres all people from the list to two groups:
*  'no_kids': 573, 'have_kids': 764

and calculated average insurance price for each group:
*  'no_kids': 12384.7, 'have_kids': 13949.94

Average price is slightly different but I dont think that existence of kids
has a huge impact on insurance price.

4. region





['southwest', 'southeast', 'northwest', 'northeast']





