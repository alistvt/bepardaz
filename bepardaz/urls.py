"""bepardaz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views as authtoken_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', authtoken_views.obtain_auth_token, name='api-token-auth'),
    url(r'^merchants/', include(('merchants.urls', 'merchants'), namespace='merchants')),
    url(r'^transactions/', include(('transactions.urls', 'transactions'), namespace='transactions')),
]
