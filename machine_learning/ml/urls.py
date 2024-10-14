from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/api/', include('prediction.urls')),
    path('django/api/recommend/', include('Recommendation.urls')),
]

