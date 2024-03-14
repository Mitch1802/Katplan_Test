from rest_framework import serializers

from .models import Fahrzeug


class FahrzeugSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        all_entries = Fahrzeug.objects.all()
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

        validated_data["kuerzel"] = f"F{kuerzel_new}"
        instance = Fahrzeug.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.foto = validated_data.get("foto", instance.foto)
        instance.name = validated_data.get("name", instance.name)
        instance.fahrzeug = validated_data.get("fahrzeug", instance.fahrzeug)
        instance.anhaenger = validated_data.get("anhaenger", instance.anhaenger)
        instance.type = validated_data.get("type", instance.type)
        instance.lenkerberechtigung = validated_data.get(
            "lenkerberechtigung", instance.lenkerberechtigung
        )
        instance.stationierung = validated_data.get(
            "stationierung", instance.stationierung
        )
        instance.personenkapazitaet = validated_data.get(
            "personenkapazitaet", instance.personenkapazitaet
        )
        instance.treibstoff = validated_data.get("treibstoff", instance.treibstoff)
        instance.nutzlast = validated_data.get("nutzlast", instance.nutzlast)
        instance.ladebordwand = validated_data.get(
            "ladebordwand", instance.ladebordwand
        )
        instance.ladekran = validated_data.get("ladekran", instance.ladekran)
        instance.wassertank = validated_data.get("wassertank", instance.wassertank)
        instance.wassertankAbnehmbar = validated_data.get(
            "wassertankAbnehmbar", instance.wassertankAbnehmbar
        )
        instance.geschlossenerAufbau = validated_data.get(
            "geschlossenerAufbau", instance.geschlossenerAufbau
        )
        instance.wechselaufbau = validated_data.get(
            "wechselaufbau", instance.wechselaufbau
        )
        instance.anhaengervorrichtung = validated_data.get(
            "anhaengervorrichtung", instance.anhaengervorrichtung
        )
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)

        instance.save()
        return instance

    class Meta:
        model = Fahrzeug
        fields = '__all__'
