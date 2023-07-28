from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello_world),
    path('first/',views.first,name="first_page"),
    path('register/',views.register,name="register"),
    path('add_team/',views.add_team,name='add_team'),
    path('',views.list_team,name="list_team"),
    path('update_team/<id>',views.update_team,name="update_team"),
    path('delete_team/<id>',views.delete_team,name="delete_team"),
    path('modelform/',views.team_modelform,name="model_form"),
    path('normalform/',views.team_info_form,name="normal_form")
    path('registeruser/',views.register_user,name="register_user")
]
