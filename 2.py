'''
Name:Rutuja Kumbhar
Assignment no: 27-2
Topic: Print Fibonacci series till nth term (Take input from user)
'''
#Source code:
def r(num):
  first = 0
  second = 1
  print(first, ",", second, end=", ")
 
  for i in range(2, num):
    next = first + second
    print(next, end=", ")
 
    first = second
    second = next
      
           
nterms = int(input("Enter nterms: "))
print("Fibonacci sequence:")
r(nterms)

"""
Output:
Enter nterms: 6
fibonacci series is:
0 , 1, 1, 2, 3, 5 
>>> 
"""
