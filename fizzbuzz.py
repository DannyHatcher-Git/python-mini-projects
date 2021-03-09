#Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

#list(1-100)
#x5 and 3 fizz buzz
#    fizz buzz
#x3
#    fizz
#x5
#    buzz
#print
for i in range(0,101): # Use a comma (,) not a -
    if i%3==0 and i%5==0: # Checks for multiple of 3 (if =0 it is true) and multiple of 5 (if =0 it is true)
        print("Fizzbuzz")
    elif i%3==0: # Checking for just multiple of 3
        print("Fizz")
    elif i%5==0: # checking for just multiple of 5
        print("Buzz")
    else: # If it is none of the above print the number
        print(i)
