"""TestMonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from test_monitor_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('signup/', views.signup_and_login_view),
    path('<user>/dashboard/', views.dashboard_view),
    path('<user>/dashboard/edit_account/', views.edit_account_view),
    path('<user>/dashboard/create_test/', views.create_test_view),
    path('<user>/dashboard/<int:id>/edit_test/', views.edit_test_view), 
    path('<user>/dashboard/<int:id>/execute_test/', views.execute_test_view)
]
