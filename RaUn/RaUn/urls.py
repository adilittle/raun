from django.contrib import admin
from django.urls import path
from APP1.views import myMainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myMainView)
]
