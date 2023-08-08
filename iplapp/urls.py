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
    path('normalform/',views.team_info_form,name="normal_form"),
    path('registeruser/',views.register_user,name="register_user"),
    path('login/',views.login_user,name="login_user"),
    path('rest_hello/',views.rest_hello,name="rest_hello"),
    # Class Based Views
    path('cls_helloview/',views.HelloView.as_view(),name="cls_helloview"),
    path('cls_registerview/',views.RegisterView.as_view(),name="cls_registerview"),
    path('cls_teamcreateview/',views.TeamCreateView.as_view(),name="cls_teamcreateview"),
    path('cls_listview/',views.TeamListView.as_view(),name='cls_listview'),
    path('cls_detailview/<pk>',views.TeamDetailView.as_view(),name='cls_detailview'),
    path('cls_teamupdateview/<pk>',views.TeamUpdateView.as_view(),name="cls_teamupdateview"),
    path('cls_teamdeleteview/<pk>',views.TeamDeleteView.as_view(),name="cls_teamdeleteview"),
    # Function Based Apis
    path('add_teamapi',views.add_team_api,name="add_teamapi")
]
