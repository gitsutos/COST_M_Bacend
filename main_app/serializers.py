from rest_framework import serializers

from .models import Costs , Family , Membership

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        feilds = ["name"]

class CostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costs
        fields = '__all__'