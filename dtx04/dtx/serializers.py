#product/serializers.py
# from rest_framework import serializers
from .models import User

class ProductSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User       # product 모델 사용
        fields = '__all__'            # 모든 필드 포함