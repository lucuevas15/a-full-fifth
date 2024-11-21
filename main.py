# This code will run a loop until the "while" parameters are no longer met
# It will also print the final values of the loop

# Initial variables for loop
a = 1
b = 2
c = 5

print("The first output is:")

#The loop will run until parameters are met
while a < c:
        a = a + 1
        b = b + c

#Output value results
print("a: ", a)
print("b: ", b)
print("c: ", c)

# Initial variables for second loop        
d = 4
e = 6
f = 7

print("The second output is:")

#The loop will run until parameters are met
while d > f:
    d = d+1
    e = e-1

#Output value results
print("d: ", d)
print("e: ", e)
print("f: ", f)

# Initial variables for third loop        
g = 4
h = 6

print("The third output is:")

#The loop will run until parameters are met
while g < h:
    g = g +1

#Output value results
print("g: ", g)
print("h: ", h)

# Initial variables for loop    
j = 2
k = 5
n = 9

print("The fourth output is:")

#The outer loop will run until parameters are met
while j < k:
    m = 6 #Initial value for inner loop
    
    #Inner loop will run until these parameters
    while m < n:
        #Output value results
        print("Goodbye")
        m = m + 1 #Increments for value of "m" in inner loop
        print("m: ", m)
    j = j + 1 #Increment for value of "j" in outer loop
print("j: ", j)
print("k: ", k)
print("n: ", n)

# Initial variables for loop 
j = 2
k = 5
m = 6
n = 9

print("The fifth output is:")

#The outer loop will run until parameters are met
while j < k: #Inner loop will run until these parameters
    while m < n:
        #Output value results
        print("Hello")
        m = m + 1 #Increments for value of "m" in inner loop
        print("m: ", m)
    j = j + 1 #Increment for value of "j" in outer loop
print("j: ", j)
print("k: ", k)
print("n: ", n)

# Initial variables for loop 
p = 2
q = 4

print("The last output is:")

#The outer loop will run until parameters are met
while p < q: #Inner loop will run until these parameters
    print("Adios")
    r = 1 #Increments for value of "r" in inner loop
    while r < q:
        print("Adios")
        r = r + 1
        print("r: ", r)
    p = p + 1 #Increment for value of "p" in outer loop
print("p: ", p)
print("q: ", q)

#Please advise how I can list the results as just the loop ending value
#rather than each single run