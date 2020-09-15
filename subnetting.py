from textwrap import wrap

ipaddr=input().split("/")

subnet=[0,0,0,0]

snt1=['1','9','17','25']
snt2=['2','10','18','26']
snt3=['3','11','19','27']
snt4=['4','12','20','28']
snt5=['5','13','21','29']
snt6=['6','14','22','30']
snt7=['7','15','23','31']
snt8=['8','16','24','32']

for i in range(4):
	if(ipaddr[1]==snt1[i]):
		for j in range(0,i):
			subnet[j]=255
		subnet[j+1]=128
		break
	if(ipaddr[1]==snt2[i]):
		for j in range(0,i):
			subnet[j]=255
		subnet[j+1]=192
		break
	if(ipaddr[1]==snt3[i]):
		for j in range(0,i):
			subnet[j]=255
		subnet[j+1]=224
		break
	if(ipaddr[1]==snt4[i]):
		for j in range(0,i):
			subnet[j]=255
		subnet[j+1]=240
		break
	if(ipaddr[1]==snt5[i]):
		for j in range(0,i):
			subnet[j]=255
		subnet[j+1]=248
		break
	if(ipaddr[1]==snt6[i]):
		for j in range(0,i):
			subnet[j]=255
		subnet[j+1]=252
		break
	if(ipaddr[1]==snt7[i]):
		for j in range(0,i):
			subnet[j]=255
		subnet[j+1]=254
		break
	if(ipaddr[1]==snt8[i]):
		for j in range(0,i):
			subnet[j]=255
		subnet[j+1]=255
		break

print("Subnet mask= ",end="")
print(subnet[0],".",subnet[1],".",subnet[2],".",subnet[3])

x=32-int(ipaddr[1])
addr=2**x
print("Number of addresses= ",addr)


ip=ipaddr[0].split('.')
binip=""


for i in range(len(ip)):
	temp=format(int(ip[i]),'08b')
	binip=binip+temp

firstip=binip[0:len(binip)-x]+binip[-x:len(binip)].replace('1','0')
firstip2=[]
k=0
while (k<len(firstip)):
	temp=firstip[k:k+8]
	firstip2.append(temp)
	k=k+8

lastip=binip[0:len(binip)-x]+binip[-x:len(binip)].replace('0','1')
lastip2=[]
k=0
while (k<len(lastip)):
	temp=lastip[k:k+8]
	lastip2.append(temp)
	k=k+8

for i in range(len(firstip2)):
	firstip2[i]=int(firstip2[i],2)
	lastip2[i]=int(lastip2[i],2)
	

print("First IP= ",end="")
print(firstip2[0],".",firstip2[1],".",firstip2[2],".",firstip2[3])

print("Last IP= ",end="")
print(lastip2[0],".",lastip2[1],".",lastip2[2],".",lastip2[3])












