from rest_framework import serializers
from reviews.models import Category, Comment, Company, ImageModel, Product, ProductSize
from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_flex_fields import FlexFieldsModelSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days


class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ["pk", "title", "content", "created", "updated"]
        expandable_fields = {
            "product": "reviews.CategorySerializer",
            "user": "reviews.UserSerializer",
        }


# class UserSerializer(serializers.ModelSerializer):
#     days_since_joined = serializers.SerializerMethodField()

#     class Meta:
#         model = User
#         fields = "__all__"


class CompanySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Company
        fields = ["pk", "name", "url"]


class ProductSizeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSize
        fields = ["pk", "name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["pk", "name"]
        extra_kwargs = {"name": {"read_only": True}}

    # properties validation
    def validate_name(self, value):
        if "django" in value.lower():
            raise serializers.ValidationError("error message")

        return value

    # validation that requires multiple fields
    def validate(self, data):
        if data["start"] > data["finish"]:
            raise serializers.ValidationError("finish must occur after start")
        return data

    # update and create are used to return new instance of the object
    # can also used ot to change of encode password
    def update(self, instance, validated_data):
        # instance.email = validated_data.get('email', instance.email)
        # instance.title = validated_data.get('content', instance.title)
        # instance.save()
        return instance


class ProductSerializer(FlexFieldsModelSerializer):
    # category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "content",
            "category",
        ]
        expandable_fields = {
            "category": ("reviews.CategorySerializer", {"many": True}),
            "sites": ("reviews.ProductSiteSerializer", {"many": True}),
            "comments": ("reviews.CommentSerializer", {"many": True}),
            "image": ("reviews.ImageSerializer", {"many": True}),
        }
        permit_list_expands = [
            "category",
            "sites",
            "comments",
            "sites.company",
            "sites.productsize",
        ]


class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
        ]
    )

    class Meta:
        model = ImageModel
        fields = ["pk", "name", "image"]
