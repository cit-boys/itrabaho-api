from rest_framework import serializers

from backend.itrabaho import models


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = "__all__"


class ApplicantsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApplicantModel
        fields = "__all__"


class JobPostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobPostModel
        fields = "__all__"


class RecruiterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RecruiterModel
        fields = "__all__"


class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReviewModel
        fields = "__all__"
