from django.shortcuts import render, redirect
from .models import Transaction
from django.db.models import Sum
from .forms import TransactionForm

def index(request):
    transactions = Transaction.objects.order_by('date')[:10]
    debet_all = Transaction.objects.filter(type='debet').aggregate(Sum('amount'))['amount__sum']
    credit_all = Transaction.objects.filter(type='credit').aggregate(Sum('amount'))['amount__sum']
    if debet_all is None:
        debet_all = 0
    if credit_all is None:
        credit_all = 0
    total_balance = round(float(debet_all) - float(credit_all), 2)
    content = {
        'transactions': transactions,
        'total_balance': total_balance
    }
    return render(request, 'balance/index.html', content)


def add(request):
    error = ''
    form = TransactionForm()
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Wrong form'
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'balance/add.html', context)


def balance(request):
    transactions = Transaction.objects.all()
    return render(request, 'balance/balance.html', {'transactions': transactions})


def balance_custom(request):
    if request.method == 'POST':
        operation = request.POST.get('form_select')
        start = request.POST.get('date_from')
        end = request.POST.get('date_to')
        category = request.POST.get('category')
        delete = request.POST.get('delete')
        if delete is not None:
            Transaction.objects.filter(id=delete).delete()
            return redirect('home')
        if category != "":
            if operation == 'all':
                query_set = Transaction.objects.filter(category__contains=category, date__range=(start, end))
            else:
                query_set = Transaction.objects.filter(type=operation, category__contains=category, date__range=(start, end))
        else:
            if operation == 'all':
                query_set = Transaction.objects.filter(date__range=(start, end))
            else:
                query_set = Transaction.objects.filter(type=operation, date__range=(start, end))
        content = {
            'set': query_set,
            'total_sum': query_set.aggregate(Sum('amount'))['amount__sum']
        }
        return render(request, 'balance/results.html', content)
    return render(request, 'balance/custom.html')


def results(request):

    return render(request, 'balance/results.html')
