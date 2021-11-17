from rest_framework import serializers

from movie.models import Category, Movie


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=30)

    def create(self, validated_data):
        """
        Create and return a new `Movie` instance, given the validated data.
        :param validated_data:
        """
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Movie` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=30)
    sinopse = serializers.CharField(max_length=255)
    rating = serializers.IntegerField()
    like = serializers.BooleanField(default=False)
    category = CategorySerializer(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Movie` instance, given the validated data.
        :param validated_data:
        """
        category_data = {}
        if 'category' in validated_data:
            category_data = validated_data.pop('category')

        if category_data:
            category = Category.objects.create(**category_data)
            movie = Movie.objects.create(category=category, **validated_data)
        else:
            movie = Movie.objects.create(**validated_data)

        return movie

    def update(self, instance, validated_data):
        """
        Update and return an existing `Movie` instance, given the validated data.
        """
        if 'category' in validated_data:
            category_data = validated_data.pop('category')
            title = category_data.get('title')
            category, _ = Category.objects.get_or_create(title=title)
            # Atualiza a categoria
            instance.category = category

        # Atualiza a instância
        instance.title = validated_data.get('title', instance.title)
        instance.sinopse = validated_data.get('sinopse', instance.sinopse)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.like = validated_data.get('like', instance.like)
        instance.save()

        return instance
