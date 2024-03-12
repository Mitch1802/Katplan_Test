import logging

from rest_framework import serializers

from .models import Dokument

logger = logging.getLogger(__name__)

class DokumentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        all_entries = Dokument.objects.all()
        kuerzel_new = ""
        
        list_of_kuerzel = [sub.kuerzel[1:] for sub in all_entries]

        for i in range(1, 1000):
            test = ""
            if i < 10: test = "00" + str(i)
            elif i < 100: test = "0" + str(i)
            else: test = str(i)

            if not test in list_of_kuerzel:
                kuerzel_new = test
                break
            
        logger.error(
            f"Kürzel Neu: D{kuerzel_new}"
        )

        validated_data["kuerzel"] = "D" + kuerzel_new
        instance = Dokument.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.kuerzel = validated_data.get("kuerzel", instance.kuerzel)
        instance.name = validated_data.get("name", instance.name)
        instance.file = validated_data.get("file", instance.file)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)

        instance.save()
        return instance

    class Meta:
        model = Dokument
        fields = '__all__'
