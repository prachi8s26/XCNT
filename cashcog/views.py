import json

import requests
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render

from .models import Expense


def create_expense_entry(request):
    cashcog_request = requests.get('https://cashcog.xcnt.io/stream', params=request.GET, stream=True)
    for chunk in cashcog_request.iter_content(chunk_size=1024):
        cashcog_expense = json.loads(chunk)

        Expense.objects.create(
            uuid=cashcog_expense["uuid"],
            description=cashcog_expense["description"],
            created_at=cashcog_expense["created_at"],
            amount=cashcog_expense["amount"],
            currency=cashcog_expense["currency"],
            employee_first_name=cashcog_expense["employee"]["first_name"],
            employee_last_name=cashcog_expense["employee"]["last_name"],
            employee_uuid=cashcog_expense["employee"]["uuid"]
        )


def get_all_the_records(request):
    expenses = Expense.objects.all()
    serialize_expense = serialize('json', expenses)
    expenses_json = json.loads(serialize_expense)

    context = {"users": expenses_json}
    return render(request, "cashcog/show_expenses.html", context)


def update_status(request):
    Expense.objects.filter(uuid=request.POST["uuid"]).update(status=request.POST["status"])
    return HttpResponse(status=200)
