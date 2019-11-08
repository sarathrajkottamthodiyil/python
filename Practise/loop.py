primes = [2,3,5,7]
for prime in primes:
    print(prime)
print("********************")
for x in range(5):
    print(x)
print(20*"%")
for x in range(3,8,2):
    print(x)
print(20*"%")
for x in range(3, 6):
    print(x)
print("***************")

#####while loop#########

count = 0
while count < 5 :
    print(count)
    count += 1
else:
    print("count value reached %d" %(count))

for i in range(1, 10):
    if (i%5==0):
        break
    print(i)
#else:
    #print("this is not printed because for loop is terminated because of break but not due to fail in condition")
print("************************************")
