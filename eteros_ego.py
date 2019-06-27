check_range=int(input("Δώσε range: "))

list1 = [x for x in range(check_range)]
list2= []
list3=[]
def sum_div(x):
    y=0
    if x==1:
        y=1
    else:
        for  i in range(1,x):
         if x % i == 0:
            y+=i
    return y


for r in range(check_range):
    list2.append(sum_div(r))



for x in range(check_range):
    if x == sum_div(list2[x]) and list2[x] != list1[x]:
      list3.append(x)


print(list3)

