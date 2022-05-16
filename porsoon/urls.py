from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sin_jim.urls')),
    path('api_auth/', include('rest_framework.urls'))
]
