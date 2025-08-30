"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from recipes.views import CategoryViewSet, RecipeViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipe')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/accounts/', include('accounts.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # This line redirects the root URL to the API endpoint
    path('', RedirectView.as_view(url='/api/', permanent=False)),
]