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
to make my analyze more readable I've separated all patients
on groups. Most commonly used for survey categories
* 18-24   group_N1
* 25-34   group_N2
* 35-44   group_N3
* 45-54   group_N4
* 55-64   group_N5
* over 65 group_N6

After data separation I've realized that in data provided no patiens over 65 years old,
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



