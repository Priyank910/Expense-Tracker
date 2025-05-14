from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Entertainment', 'Entertainment'),
        ('Bills', 'Bills'),
        ('Other', 'Other'),
    ]

    TRANSACTION_CHOICES = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount field
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  # Choice field
    transaction = models.CharField(max_length=20, choices=TRANSACTION_CHOICES, null=True)  # Income or Expense
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time when record is inserted

    def __str__(self):
        return f"{self.category}: {self.amount} ({self.transaction}) on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)