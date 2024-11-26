sales= []

days= ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

for day in days:
    sal= float(input(f'please enter average sales for{day}:'))
    sales.append(sal) 

print("\n total sales for a shop over a week:")
total= sum(sales) 
print (total)

print("\n average sales for a week")
av= sum(sales)/7
print(av)

    