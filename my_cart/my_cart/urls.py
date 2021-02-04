from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.b_urls')),
    path('shop/', include('shop.s_urls'))
]
