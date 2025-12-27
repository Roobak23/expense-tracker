from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from django.db.models import Q

def index(request):
    query = request.GET.get('q', '')

    # Search by title OR category
    if query:
        expenses = Expense.objects.filter(
            Q(title__icontains=query) |
            Q(category__icontains=query)
        )
    else:
        expenses = Expense.objects.all()

    # Total calculation
    total = sum(exp.amount for exp in expenses)

    return render(request, 'index.html', {
        'expenses': expenses,
        'total': total,
        'query': query
    })


def add_expense(request):
    if request.method == 'POST':
        Expense.objects.create(
            title=request.POST['title'],
            amount=request.POST['amount'],
            category=request.POST.get('category'),
            date=request.POST['date']
        )
        return redirect('index')

    return render(request, 'expense_form.html')


def edit_expense(request, id):
    expense = get_object_or_404(Expense, id=id)

    if request.method == 'POST':
        expense.title = request.POST['title']
        expense.amount = request.POST['amount']
        expense.category = request.POST.get('category')
        expense.date = request.POST['date']
        expense.save()
        return redirect('index')

    return render(request, 'expense_form.html', {'expense': expense})


def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    expense.delete()
    return redirect('index')
