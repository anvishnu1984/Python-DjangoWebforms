from django.urls import path
from . import views

app_name = 'Environments'
urlpatterns = [
      path('', views.HomeView.as_view() ,  name = 'home'),
      path('Environment/', views.EnvironmentListView.as_view() , name = 'Environment'),
      path ('Environment/add/', views.EnvironmentCreateView.as_view(), name = 'Environment_createtagversions'),
      path ('Environment/<int:pk>/', views.EnvironmentDetailView.as_view(), name = 'Environment_detail'),
      path ('Environment/<int:pk>/tagversions/edit/', views.EnvironmentTagversionsEditView.as_view(), name = 'Environment_TagVersion_Edit')

]