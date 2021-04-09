from django.contrib import admin
from django.urls import path, include

# connects our apps to the root address
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('frontend.urls')),
    path('spotify/', include('spotify.urls'))
]
