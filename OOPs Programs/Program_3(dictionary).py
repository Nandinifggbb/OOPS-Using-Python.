d={}
class employee():
	def salary(self,name,add,basic,tds=0,deducts=0):
		self.name=name
		self.add=add
		self.basic=basic
		self.hra=1.2*basic
		self.da=0.25*basic
		self.tds=tds
		self.pf=2000
		self.pt=500
		self.deducts=deducts
		self.netsal=self.basic+self.hra+self.da-(self.pf+self.pt+self.deducts+self.tds)
		return self.netsal
	def accept(self):
		name=input("name:")
		add=input("Address:")
		basic=int(input("basic:"))
		tds=int(input("TDS:"))
		deducts=int(input("Deducts:"))
		self.netsal=self.salary(name,add,basic,tds,deducts)
	def display(self):
		print("Hra=",self.hra,"Da=",self.da)
		print("netsal=",self.netsal)
	def search1(self,name):
		for k,v in d.items():
			if k==name:
				print("name:",v.name)
				print("address:",v.add)
				print("basic:",v.basic)
				print("netsal:",v.netsal)


while True:
	print("1:Accept Employee Details")
	print("2:Display Employee Details")
	print("3:Update Employee Details")
	print("4:Search Employee Details")
	print("5:Alter Employee Details")

	choice=int(input("Enter a choice"))

	if choice==1:
		e=employee()
		e.accept()
	elif choice==2:
		e.display()
	elif choice==3:
		d[e.name]=e.__dict__
		print(d,"\n")
	elif choice==4:
		name=input("enter")
		e.search1(name)
	elif choice==5:
		k = input(": ")
		d[k] = e.accept()
		print("Employee details changed")
	else: 
		break
	