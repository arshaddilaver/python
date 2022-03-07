"Display future leap years from current year to a final year entered by user."

from datetime import date
year1=date.today().year
final_year=int(input("enter final year"))

print("Leap years range from {} to {}".format(year1,final_year))
for year in range(year1,final_year+1):
    if ((year%4==0) and (year%400==0 or year%100!=0)):
        print(year) 
