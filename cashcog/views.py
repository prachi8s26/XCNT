import json

import requests
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render

from .models import Expense, Employee


def create_expense_entry(request):
    cashcog_request = requests.get('https://cashcog.xcnt.io/stream', params=request.GET, stream=True)
    for chunk in cashcog_request.iter_content(chunk_size=1024):
        chunk_decode = chunk.decode('utf8').replace("'", '"')
        cashcog_expense = json.loads(chunk_decode)

        Employee.objects.create(
            uuid=cashcog_expense["employee"]["uuid"],
            first_name=cashcog_expense["employee"]["first_name"],
            last_name=cashcog_expense["employee"]["last_name"]
        )

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
    all_data = Expense.objects.all()
    # waiting_for_approval_expenses = Expense.objects.filter(status=0)
    data = serialize('json', all_data)
    dataa = json.loads(data)

    act = {"users": dataa}
    return render(request, "cashcog/index.html", act)


def update_status(request):
    Expense.objects.filter(uuid=request.POST.get["uuid"]).update(status=request.GET["status"])
    return HttpResponse(html="xyz")
