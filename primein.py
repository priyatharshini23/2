lower=int(input("Enter lower range:")
upper=int(input("Enter upper range:")
for number in range(lower,upper+1):
   if number>1:
       for i in range(2,number):
           if (number%i)==0:
               break
       else:
           print(number)
