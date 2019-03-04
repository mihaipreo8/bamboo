from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView
)
from .models import Transaction


# transactions = [
# 	{
# 		'Sender': 'Mihai Preo',
# 		'IdAccount': 1,
# 		'AccountNoSender': '12345678',
# 		'SortCodeSender': '001122',
# 		'Balance': 100,
# 		'Receiver': 'Bamboo Loans',
# 		'AccountNoReceiver': '87654321',
# 		'SortCodeReceiver': '221100',
# 		'Value':10,
# 		'TransactionDetails': 'Invoice 0197',
# 		'date_transaction': 'March 3, 2018'
# 	},
# ]

def home(request):
	# user1 = User.objects.filter(username='mihai').first()
	# user1_id = user1.id
	context = {
		'transactions' : Transaction.objects.all()
		# 'transactions' : Transaction.objects.filter(sender_id=user_id) # query all the transactions from the DB
	}
	return render(request, 'bank/home.html', context)

class TransactionListView(ListView):
	model = Transaction
	template_name = 'bank/home.html'
	context_object_name = 'transactions'
	ordering = ['-date_transaction']
	paginate_by = 3


class UserTransactionListView(ListView):
	model = Transaction
	template_name = 'bank/user_transaction.html'
	context_object_name = 'transactions'
	paginate_by = 3

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Transaction.objects.filter(sender=user).order_by('-date_transaction')


class TransactionDetailView(DetailView):
	model = Transaction
	
class TransactionCreateView(LoginRequiredMixin, CreateView):
	model = Transaction
	fields = ['receiver','accountNoReceiver', 'sortCodeReceiver', 'value', 'transactionDetails']

	def form_valid(self, form):
		form.instance.sender = self.request.user
		return super().form_valid(form)

def about(request):
	return render(request, 'bank/about.html', {'title':'About'})