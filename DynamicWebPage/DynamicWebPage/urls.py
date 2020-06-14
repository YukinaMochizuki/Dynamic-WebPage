"""DynamicWebPage URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from articles import views as articlesView
from account import views as accountView
from event import views as eventView

router = DefaultRouter()
router.register(r'articles', articlesView.ArticleViewSet)
router.register(r'kanban', articlesView.KanbanViewSet)
router.register(r'account', accountView.AccountViewSet)
router.register(r'event', eventView.EventViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url('^api/v1/event/(?P<accountname>.+)/(?P<eventType>.+)/$', eventView.EventList.as_view())
]
