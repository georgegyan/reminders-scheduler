from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reminders.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', 
         auth_views.LoginView.as_view(template_name='registration/signup.html'), 
         name='signup'),
]
