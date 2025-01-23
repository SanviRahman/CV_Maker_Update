from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (home, registers, logins, 
                    approved , cvmaker, cv_update, 
                    cv_details,cv_delete,logout,)


urlpatterns = [
   path('home/',home,name='home'),
   path('cv_details/<int:pk>/',cv_details,name='cv_details'),
   path('cv_update/<int:pk>/',cv_update,name='cv_update'),
   path('cv_delete/<int:pk>/',cv_delete,name='cv_delete'),
   path('registers/',registers,name='registers'),
   path('logins/',logins,name='logins'),
   path('cvmaker/',cvmaker,name='cvmaker'),
   path('approved/<int:pk>',approved,name='approved'),
   path('logout/',logout,name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
