"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from recipes.views import CategoryViewSet, RecipeViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipe')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # This is the line you need to add to include your accounts app URLs
    path('api/accounts/', include('accounts.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]