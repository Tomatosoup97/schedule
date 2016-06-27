from rest_framework import serializers

from .models import Meeting, Category, Tag, Suggestion

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ('id', 'title', 'description', 'owner', 'meeting')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'color')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')

class MeetingSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Meeting
        fields = '__all__'
        readonly_fields = ('slug', 'created', 'modified')

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        tags_data = validated_data.pop('tags')
        meeting = Meeting.objects.create(**validated_data)
        category = Category.objects.get_or_create(**category_data)
        category.meetings.add(meeting)

        for tag_data in tags_data:
            tag = Tag.objects.get_or_create(**validated_data)
            tag.meetings.add(meeting)

    def validate(self, data):
        if data['start'] > data['end']:
            raise serializers.ValidationError(_('End must be later than start'))
        if data['private'] is True and data['public'] is True:
            raise serializer.ValidationError(
                _('Meeting can not be both private and public'))
        return data
