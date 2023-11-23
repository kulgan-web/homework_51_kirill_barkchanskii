from django.urls import path
from webapp.views import index_page, actions_with_cat


urlpatterns = [
    path('', index_page),
    path('cat_stats/', actions_with_cat),
]