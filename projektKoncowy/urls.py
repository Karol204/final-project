"""projektKoncowy URL Configuration

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
from django.urls import path, include
from django.views.generic import TemplateView

from portalPacjenta import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('loged_in/', views.homeView),
    path('doctors/', views.docListView),
    path('placowki/', views.placesView),
    path('visits/', views.visitsView),
    path('new-visit/', views.newVisitForm.as_view()),
    path('update_profil/', views.profilFormView.as_view()),
    path('delete_visit/<int:pk>', views.delete_visit),
    path('profil/', views.profilView),
    path('profil/<int:pk>', views.ProfilUpdateView.as_view()),
    path('place/<int:id>', views.singlePlaceView)

]