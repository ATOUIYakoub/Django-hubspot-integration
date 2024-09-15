from rest_framework import serializers
from datetime import datetime

class LeadPropertiesSerializer(serializers.Serializer):
    createdate = serializers.DateTimeField()
    email = serializers.EmailField()
    firstname = serializers.CharField(max_length=100)
    hs_object_id = serializers.CharField(max_length=100)
    lastmodifieddate = serializers.DateTimeField()
    lastname = serializers.CharField(max_length=100)

class LeadSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    properties = LeadPropertiesSerializer()
    createdAt = serializers.DateTimeField(required=False)
    updatedAt = serializers.DateTimeField(required=False)
    archived = serializers.BooleanField()

    def update(self, instance, validated_data):
        # Update the properties
        properties_data = validated_data.pop('properties', {})
        for attr, value in properties_data.items():
            setattr(instance.properties, attr, value)
        
        # Update the other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Set updatedAt to current time
        instance.updatedAt = datetime.now()
        
        return instance