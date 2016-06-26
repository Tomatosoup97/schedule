from rest_framework import serializers

from .models import Meeting, Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'color')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'
        readonly_fields = ('slug', 'created', 'modified')

    def validate(self, data):
        if data['start'] > data['end']:
            raise serializers.ValidationError('End must be later than start')
        return data