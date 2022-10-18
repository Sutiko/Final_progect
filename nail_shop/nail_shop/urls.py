from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from user import views as userViews
from django.contrib.auth import views as authViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/',include('shop.urls')),
    path('reset/',include('django.contrib.auth.urls')),
    path('registration/', userViews.register, name="reg"),
    path('login/', authViews.LoginView.as_view(template_name='user/login.html'), name="login"),
    path('exit/', authViews.LogoutView.as_view(template_name='base.html'), name="exit"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)