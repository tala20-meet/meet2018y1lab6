counts=input("add a number: ")
print (counts)
for count in range (int(counts)):
    print (count)
    if count%3==0 and count%5==0:
       print("fizzbuzz")
    elif count%3==0:
       print ("fizz")
    elif count % 5==0:
        print("buzz")
   
