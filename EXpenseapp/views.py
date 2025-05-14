from django.shortcuts import render, get_object_or_404, redirect
from .models import *


# Create your views here.

def index(request):
    # Fetch all expenses from the database
    expenses = Expense.objects.all().order_by('-created_at')[:10]

    return render(request, "index.html", {'expenses': expenses, 'show_all': False})

def all_expenses(request):
    expenses = Expense.objects.all().order_by('-created_at')  # Fetch all transactions
    return render(request, "index.html", {'expenses': expenses, 'show_all': True})


def add_expense(request):
    amount = request.POST.get('amount')
    category = request.POST.get('category')
    transaction = request.POST.get('type')  # Retrieve the selected type

    if request.method == 'POST':
        if transaction == 'Income':
            # Logic for handling Income (e.g., save to a different model or table)
            Expense.objects.create(amount=amount, category=category, transaction=transaction)
            print("Adding Income")
        elif transaction == 'Expense':
            # Logic for handling Expense
            Expense.objects.create(amount=amount, category=category, transaction=transaction)
            print("Adding Expense")

        print("Donee")
    else:
        print("Somthing Wrong")


    # Fetch all expenses from the database
    expenses = Expense.objects.all().order_by('-created_at')[:10]

    return render(request, "index.html", {'expenses': expenses, 'show_all': False})


# Delete an expense
def delete_expense(request, expense_id):

    print(expense_id)
    expense = get_object_or_404(Expense, id=expense_id)  # Get the expense or return a 404 if not found
    expense.delete()  # Delete the expense

    print("Yoo")

    return redirect(index)  # Redirect back to the main page
