# recipes/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Category, Recipe

User = get_user_model()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'ingredients', 'instructions',
            'preparation_time_minutes', 'cooking_time_minutes', 'servings',
            'category', 'owner', 'created_at', 'updated_at'
        ]