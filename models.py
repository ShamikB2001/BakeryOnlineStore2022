from django.db import models

# Create your models here.

class itemdetails(models.Model):
	bakeryname=models.CharField(max_length=50)
	bakeryprice=models.CharField(max_length=10)
	bakeryimage=models.CharField(max_length=500)
	bakerytype=models.CharField(max_length=50)
	bakeryflavour=models.CharField(max_length=50)
	class Meta:
		db_table="itemdetails"
class accountdb(models.Model):
	First_name=models.CharField(max_length=50)
	Last_name=models.CharField(max_length=20)
	Email=models.EmailField()
	Phone_no=models.IntegerField(max_length=15)
	User_name=models.CharField(max_length=50)
	Pwd=models.CharField(max_length=20)
	Cpwd=models.CharField(max_length=20)
	class Meta:
		db_table="accountdb"
class customerorderdetails(models.Model):
	firstname=models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	address=models.CharField(max_length=300)
	pincode=models.CharField(max_length=10)
	phone=models.CharField(max_length=15)
	email=models.EmailField()
	altphone=models.CharField(max_length=15)
	quentity=models.CharField(max_length=20)
	itemname=models.CharField(max_length=50)
	itemprice=models.CharField(max_length=10)
	ordertime=models.CharField(max_length=100)
	class Meta:
		db_table="customerorderdetails"