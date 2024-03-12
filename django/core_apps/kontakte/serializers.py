from rest_framework import serializers

from .models import Kontakt


class KontaktSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        all_entries = Kontakt.objects.all()
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

        validated_data["kuerzel"] = f"C{kuerzel_new}"

        instance = Kontakt.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
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
