from django.urls import path
from . import views

urlpatterns=[
    path('',views.createnote,name='createnote'),
    path('<int:pk>/delete/' ,views.delete ,name='delete'),
    # path('<int:pk>/update/' ,views.Update ,name='update')
]