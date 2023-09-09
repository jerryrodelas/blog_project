


from django.contrib import admin
from django.urls import path,include
# from blog import views---comment
from django.contrib.auth.views import LoginView,LogoutView


# HINT: https://learndjango.com/tutorials/django-login-and-logout-tutorial

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('',include('blog.urls')),
    path('accounts/login/',LoginView.as_view(),name='login'),
    path('accounts/logout/',LogoutView.as_view(),name='logout',kwargs={'next_page':'/'})

]    
   
#  python manage.py createsuperuser  
# Username: jerryrodelas
# Email address: jerriandrodelas@gmail.com
# Password: jazzriff70

