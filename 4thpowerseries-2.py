n = int(raw_input())
b_rep = ""
power = 0
while(n!=0):
    b_rep += str(n%4)
    n = n / 4
try:
    print("YES",int(b_rep[::-1],2))
except:
    print("NO")
    
