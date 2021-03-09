'''
(i*i)%3 is 0 or 1
(i*i*i)%5 is 0 or 1
'''

for i in range(1,101):
    start_index = i*i%3*4 # i % 3 = 0 or 1 * 4 gives starting point. 0*4 is 0 1*4 is 4.  i^2 1 if false 0 if true
    end_index = 8-i**4%5*4 # i^4 % 5 = 0 or 1 *4 gives end point. 8 - 4 = 4, 8 - 0 = 8
    print("FizzBuzz"[start_index:end_index]or i) # Print (condition:condition) the number from range as default

