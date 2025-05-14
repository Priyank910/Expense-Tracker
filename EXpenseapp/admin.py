from django.contrib import admin
from .models import Expense, Contact


# Register your models here.


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'category', 'transaction', 'created_at', 'id')
    list_filter = ('category', 'created_at')
    search_fields = ('category',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')