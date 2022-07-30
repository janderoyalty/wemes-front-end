"""wemes URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as n_routers
from wemes import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
## generates:
# /users/
# /users/{pk}/

user_router = n_routers.NestedSimpleRouter(router, r'users', lookup='user')
user_router.register(r'transactions', views.TransactionViewSet, basename='transactions')
## generates:
# /users/{user_pk}/transactions/
# /users/{user_pk}/transactions/{pk}/

transactions_router = n_routers.NestedSimpleRouter(user_router, r'transactions', lookup='transaction')
transactions_router.register(r'items', views.ItemViewSet, basename='items')
## generates:
# /users/{user_pk}/transactions/{transaction_pk}/items/
# /users/{user_pk}/transactions/{transaction_pk}/items/{pk}/

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    # path(r'', include(user_router.urls)),
    # path(r'', include(transactions_router.urls)),
]