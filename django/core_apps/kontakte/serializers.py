from rest_framework import serializers

from .models import Kontakt


class KontaktSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        instance = Kontakt.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.kuerzel = validated_data.get("kuerzel", instance.kuerzel)
        instance.name = validated_data.get("name", instance.name)
        instance.funktion = validated_data.get("funktion", instance.funktion)
        instance.telefon = validated_data.get("telefon", instance.telefon)
        instance.telefon2 = validated_data.get("telefon2", instance.telefon2)
        instance.telefon3 = validated_data.get("telefon3", instance.telefon3)
        instance.email = validated_data.get("email", instance.email)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)

        instance.save()
        return instance

    class Meta:
        model = Kontakt
        fields = '__all__'
