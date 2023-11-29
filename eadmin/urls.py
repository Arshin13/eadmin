from django.urls import path
from .import views

urlpatterns=[
    path('index/',views.index,name='index'),
    path('add/',views.add_employee,name='add'),
    path('edit/<int:emp_id>',views.edit_employee,name='edit'),
    path('delete/<int:emp_id>',views.delete_employee,name='delete'),

    path('details/',views.employee_details,name='details'),
    path('',views.login,name='login')
]