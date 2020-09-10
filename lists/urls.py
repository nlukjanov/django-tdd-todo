from django.urls import path
from .views import view_list, new_list

urlpatterns = [
    path('new', new_list),
    path('<int:list_id>/', view_list)
]
