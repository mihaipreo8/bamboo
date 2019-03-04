from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Transaction(models.Model):
	
	receiver = models.CharField(max_length=100)
	accountNoReceiver = models.CharField(max_length=8)
	sortCodeReceiver = models.CharField(max_length=6)
	value = models.IntegerField()
	transactionDetails = models.CharField(max_length=100)
	date_transaction = models.DateTimeField(default=timezone.now) #default=timezone.now  auto_new_add=True

	sender = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self): #we can return how want thi to be printed out
		return self.transactionDetails


	def get_absolute_url(self):
		return reverse('transaction-detail', kwargs={'pk': self.pk})




# class Accounts(models.Model):
	
# 	accountNo = models.CharField(max_length=8)
# 	sortCode = models.CharField(max_length=6)
# 	#balance = models.IntegerField()
# 	date_created = models.DateTimeField(default=timezone.now) #default=timezone.now  auto_new_add=True

# 	owner = models.ForeignKey(User, on_delete = models.CASCADE)