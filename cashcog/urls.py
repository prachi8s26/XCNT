from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create-expense', views.create_expense_entry, name='create_expense'),
    url(r'get-expenses', views.get_all_the_records, name='get_expenses'),
    url(r'update-expense', views.update_status, name='update_expense')
]
