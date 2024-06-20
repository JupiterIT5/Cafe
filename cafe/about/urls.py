from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('all/', catalog_list, name='catalog_dish_page'),
    path('all/dish/<int:id>/', dish, name='menu_dish'),
    path('provider/', all_provider, name='all_provider_list'),
    path('provider/<int:id>/', provider, name='provider_menu'),
    path('provider/addprover/', add_provider, name="add_new_provider"),
    path('reg/', user_registraion, name='registr'),
    path('login/', user_login, name='log in'),
    path('logout/', user_logout, name='log out'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)