from rest_framework import serializers

from .models import KatMaterial


class KatMaterialSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        instance = KatMaterial.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.artikel = validated_data.get("artikel", instance.artikel)
        instance.bemerkung = validated_data.get("bemerkung", instance.bemerkung)
        instance.menge = validated_data.get("menge", instance.menge)
        instance.stationierungsort = validated_data.get(
            "stationierungsort", instance.stationierungsort
        )
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)

        instance.save()
        return instance

    class Meta:
        model = KatMaterial
        fields = '__all__'
