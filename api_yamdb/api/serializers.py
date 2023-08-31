from rest_framework import serializers

from reviews.models import Review, Comments


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data
        title_id = self.context['view'].kwargs.get('title_id')
        author = self.context['request'].user
        if Review.objects.filter(title=title_id, author=author).exists():
            raise serializers.ValidationError(
                'Уже существует отзыв от пользователя к данному произведению'
            )
        return data

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Comments
        fields = ('id', 'text', 'author', 'pub_date')
        read_only_fields = ('title',)
