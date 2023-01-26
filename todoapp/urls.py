from django.urls import path
from . import views

urlpatterns=[
    path('login',views.login,name='login'),
    path('',views.createnote,name='createnote'),
    path('<int:pk>/delete/' ,views.delete ,name='delete'),
    path('<int:pk>/update/' ,views.update ,name='update'),
    path('logout',views.logout,name='logout')
    # path('<int:pk>/update/' ,views.Update ,name='update')
]