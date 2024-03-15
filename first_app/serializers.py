from rest_framework import serializers
from first_app.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    event_age = serializers.SerializerMethodField(help_text="Custom Field")

    def get_event_age(self, instance):
        return True if instance.age < 30 else False

    class Meta:
        model = UserModel
        fields = "__all__"

    def validate_email(self, instance):
        if "admin" in instance:
            raise serializers.ValidationError(detail="사용할 수 없는 메일 계정입니다.")

        return instance

    def validate_name(self, instance):
        if len(instance) < 2:
            raise serializers.ValidationError(detail="이름이 올바르지 않습니다.")

        return instance

    def validate_age(self, instance):
        if instance < 19:
            raise serializers.ValidationError(detail="회원 가입이 불가능한 나이입니다.")

        return instance

    def validate_nationality(self, instance):
        return instance