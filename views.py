from django.shortcuts import render,redirect
from bakery.forms import userForm
from bakery.forms import cForm
from bakery.models import itemdetails
from bakery.models import accountdb
from bakery.models import customerorderdetails
from bakery.forms import userForm2
# Create your views here.
def uploaddata(request):
	return render(request,'uploaddata.html')
def uld(request):
	if request.method=="POST":
		t=userForm(request.POST)
		if t.is_valid():
			try:
				t.save()
				return render(request,"uploaddata.html")
			except:
				pass
		return render(request,"uploaddata.html")
def showalldata(request):
	t=itemdetails.objects.all()
	return render(request,'showalldata.html',{'x':t})
def delete(request,id):
	t=itemdetails.objects.get(id=id)
	t.delete()
	return redirect("../showalldata")
def edit(request,id):
	t=itemdetails.objects.get(id=id)
	return render(request,'editalldata.html',{'x':t})
def edc(request,id):
	t=itemdetails.objects.get(id=id)
	f=userForm(request.POST,instance=t)
	if f.is_valid():
		f.save()
		return redirect("../showalldata")
	return render(request,"editalldata.html",{'x':t})


def vieworder(request,id):
	t=itemdetails.objects.get(id=id)
	return render(request,'vieworder.html',{'x':t})
def vld(request,id):
	t=itemdetails.objects.get(id=id)
	f=userForm(request.POST,instance=t)
	if f.is_valid():
		f.save()
		return redirect("../vieworder")
	return render(request,"vieworder.html",{'x':t})


def usercreateacc(request):
	return render(request,'createaccountuser.html')

def administrator(request):
	return render(request,'administrator login.html')
def adminlog(request):
	if request.method=='POST':
		User_name=request.POST['User_name']
		Pwd=request.POST['Pwd']
		try:
			if User_name=='sumon06' and Pwd=='sumon1234':
				return render(request,'uploaddata.html')
			else:
				return render(request,'administrator login.html')
		except:
			return render(request,'administrator login.html')

def createaccount(request):
	return render(request,'Login Page.html')
def cre(request):
	if request.method=="POST":
		t=cForm(request.POST)
		if t.is_valid():
			try:
				t.save()
				return render(request,'Login Page.html')
			except:
				pass
		return render(request,'Login Page.html')

def loginpage(request):
	return render(request,'Login2.html')
def log2(request):
	if request.method=='POST':
		User_name=request.POST['User_name']
		Pwd=request.POST['Pwd']
		try:
			p=accountdb.objects.get(User_name=User_name)
			t=accountdb.objects.get(Pwd=Pwd)
			if p and t is not None:
				t=itemdetails.objects.all()
				return render(request,'showmaindata.html',{'x':t})
			else:
				return render(request,'login2.html')
		except:
			return render(request,'login2.html')

def customerorder(request,id):
	t=itemdetails.objects.get(id=id)
	return render(request,'customerorder.html',{'x':t})
def cto(request,id):
	t=itemdetails.objects.get(id=id)
	f=userForm(request.POST,instance=t)
	if f.is_valid():
		f.save()
		return redirect("../customerorder")
	return render(request,"customerorder.html",{'x':t})	
def ceo(request):
	if request.method=="POST":
		t=userForm2(request.POST)
		if t.is_valid():
			try:
				t.save()
				return render(request,"customerorder.html")
			except:
				pass
		return render(request,"customerorder.html")
def showcustomerorder(request):
	t=customerorderdetails.objects.all()
	return render(request,'showcustomerorder.html',{'x':t})
def finalorder(request):
	return render(request,'finalorder.html')