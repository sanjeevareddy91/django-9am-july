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
    path('add_teamapi',views.add_team_api,name="add_teamapi"),
    path('team_get_update_delete_api/<id>',views.team_get_update_delete_api,name="team_get_update_delete_api"),
    path('serializers_addteam_api/',views.serializers_addteam_api,name="serializers_addteam_api"),
    path('serializer_team_get_update_delete_api/<id>',views.serializer_team_get_update_delete_api,name='serializer_team_get_update_delete_api'),
    path('cbsample_apiview',views.CBSampleAPIView.as_view(),name='cbsample_apiview'),
    path('cbaddteam_api',views.CBAddTeam_API.as_view(),name='cbaddteam_api'),
    path('cbaddteam_api/<pk>',views.CBAddTeam_API_withID.as_view()),
    path('team_info_listapiview',views.TeamInfoListView.as_view()),
    path('team_info_createapiview',views.TeamInfoCreateView.as_view()),
    path('team_info_retrieveapiview/<pk>',views.TeamInfoRetrieveView.as_view()),
    path('team_info_updateapiview/<pk>',views.TeamInfoUpdateView.as_view()),
    path('team_info_destroyapiview/<pk>',views.TeamInfoDestroyView.as_view()),
    path('team_info_listcreateapiview/',views.TeamInfoListCreateView.as_view()),
    path('team_info_retrieveupdatedestroyapiview/<pk>',views.TeamInfoRetrieveUpdateDestroyView.as_view()),
    path('team_info_viewset_list',views.TeamInfoViewset.as_view({'get':'list'})),
    path('team_info_viewset_retrieve/<pk>',views.TeamInfoViewset.as_view({'get':'retrieve'})),
    path('cbaddteam_apiauth',views.CBAddTeam_APIAuth.as_view(),name='cbaddteam_apiauth'),
    path('register_userapi/',views.register_userapi)
]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'teams',views.TeamInfoViewset,basename='teams')

router.register(r'teamsmodelviewset',views.TeamInfoModelViewset,basename='teamsmodelviewset')
urlpatterns = urlpatterns + router.urls