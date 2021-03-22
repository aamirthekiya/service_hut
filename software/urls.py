"""software URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from document import views as d_views
from accounts import views as a_views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('home/', d_views.index, name='home'),
	path('create/', d_views.create, name='create'),
	path('search/', d_views.search, name='search'),
	path('', a_views.login, name='login'),
	path('signup/', a_views.signup, name='signup'),
	path('logout/', a_views.logout, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
