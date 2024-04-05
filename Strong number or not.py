def fact1(x):
  fact=1
  for i in range(1,x+1,1):
    fact=fact*i
    return fact
sum=0
temp=0
n=145
while n>0:
  R=n%10
  sum=sum+fact1(R)
  n=n//10
if sum==temp:
  print(sum,"is strong number")
else:
  print(sum,"is not strong number")    
