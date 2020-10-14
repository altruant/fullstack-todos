from django.urls import path

from .views import ItemRetrieveUpdateDestroyView, ItemListCreateView

urlpatterns = [
    path('<int:pk>/', ItemRetrieveUpdateDestroyView.as_view()),
    path('', ItemListCreateView.as_view())
]
