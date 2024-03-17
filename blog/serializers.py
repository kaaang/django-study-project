from rest_framework import serializers
from blog.models import Post
from blog.models import Comment


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post_id", "contents")

    def to_representation(self, instance):
        self.fields['post_id'] = PostRepresentationSerializer(read_only=True)
        return super(CommentSerializers, self).to_representation(instance)


class PostSerializers(serializers.ModelSerializer):
    post = CommentSerializers(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("id", "title", "contents", "post")


class PostRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "contents")
