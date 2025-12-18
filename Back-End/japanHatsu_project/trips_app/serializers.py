from rest_framework import serializers
from .models import Trip, ItineraryItem


class ItineraryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryItem
        fields = [
            "id",
            "trip",
            "day_number",
            "title",
            "category",
            "description",
            "location",
            "image_url",
            "start_time",
            "end_time",
            "api_source",
        ]
        read_only_fields = ["id", "trip", "api_source"]

    def validate_category(self, value):
        allowed = {"touristy", "iconic", "local", "unique", "morning", "afternoon", "evening"}
        if value.lower() not in allowed:
            raise serializers.ValidationError("Category must be one of: " + ", ".join(sorted(allowed)))
        return value


class TripSerializer(serializers.ModelSerializer):
    items = ItineraryItemSerializer(many=True, read_only=True)

    class Meta:
        model = Trip
        fields = [
            "id",
            "user",
            "start_date",
            "end_date",
            "budget",
            "group_type",
            "group_details",
            "interests",
            "preferred_cities",
            "created_at",
            "items",
        ]
        read_only_fields = ["id", "user", "created_at", "items"]

    def validate(self, attrs):
        if attrs["start_date"] > attrs["end_date"]:
            raise serializers.ValidationError("Start date must be earlier than end date.")
        return attrs
