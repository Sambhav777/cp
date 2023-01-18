def sgcd(a,b):
	if a==b:return a
	if a==0:return b
	if b==0:return a
	if a%2==0:
		if b%2==0:return 2*sgcd(a/2,b/2)
		else:return sgcd(a/2,b)
	if b%2==0:return sgcd(a,b/2)
	else:return sgcd(abs(a-b)/2,min(a,b))
def egcd(a,b):
	if b==0:return a
	else:A=egcd(b,a%b)
	return A
def lcm(a,b):
	try:return int(a*b/sgcd(a,b))
	except:return a*b/egcd(a,b)
def I(a):return map(int,a.split(' '))
def main():
    for i in range(int(input())):
        a,b = I(input())
main()