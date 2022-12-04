from django.urls import path
from .views import index, by_category, PostCreateView

urlpatterns = [
    path('add/', PostCreateView.as_view(), name='add'),
    path('<int:category_id>/', by_category, name='by_category'),
    path('', index, name='index'),
]
