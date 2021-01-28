from django.contrib import admin
from django.conf.urls import url,include
from django.conf import settings
from user import views
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('user.urls')),
    url(r'^accounts/logout/', auth_views.LogoutView, {'next_page': '/'}, name='logout'),
]