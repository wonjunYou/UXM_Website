"""uxmWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from uxmweb_app import views

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path('',views.main, name="main"),
    path(r'^publication/',views.publication, name="publication"),
    path(r'project/',views.project,name="project"),
    path('publication/',views.publication, name="publication"),
    path('member/',views.member, name="member"),
    path('project/',views.project, name ="project"),
    path('notice/',views.notice, name="notice")
]
