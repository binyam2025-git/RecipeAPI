# recipes/serializers.py
#Enhance error handling with custom exceptions and responses for specific validation failures.

from rest_framework import serializers
from .models import Category, Recipe
from django.contrib.auth.models import User

#creatting a userserializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

#creating a categoryserializer.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

#creating a RecipeSerializer
class RecipeSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'ingredients', 'instructions',
            'preparation_time_minutes', 'cooking_time_minutes', 'servings',
            'category', 'owner', 'created_at', 'updated_at'
        ]
