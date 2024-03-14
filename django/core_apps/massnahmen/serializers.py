from rest_framework import serializers

from .models import Massnahme, MasFahrzeuge, MasKontakte

from core_apps.kontakte.models import Kontakt
from core_apps.fahrzeuge.models import Fahrzeug


class MassnahmeSerializer(serializers.ModelSerializer):
    verstaendigung = serializers.PrimaryKeyRelatedField(many=True, queryset=Kontakt.objects.all())
    fahrzeuge = serializers.PrimaryKeyRelatedField(many=True, queryset=Fahrzeug.objects.all())

    def create(self, validated_data):
        verstaendigung_data = validated_data.pop('verstaendigung')
        fahrzeuge_data = validated_data.pop('fahrzeuge')
        all_entries = Massnahme.objects.all()
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

        validated_data["kuerzel"] = f"M{kuerzel_new}"

        instance = Massnahme.objects.create(**validated_data)

        for fah in fahrzeuge_data:
            MasFahrzeuge.objects.create(mas_id=instance, fah_id=fah)
        
        for kon in verstaendigung_data:
            MasKontakte.objects.create(mas_id=instance, kon_id=kon)
        
        return instance

    def update(self, instance, validated_data):
        verstaendigung_data = validated_data.pop('verstaendigung')
        fahrzeuge_data = validated_data.pop('fahrzeuge')

        instance.name = validated_data.get("name", instance.name)
        instance.beschreibung = validated_data.get("beschreibung", instance.beschreibung)
        instance.kategorie = validated_data.get("kategorie", instance.kategorie)
        instance.verantwortung = validated_data.get("verantwortung", instance.verantwortung)
        instance.staerke = validated_data.get("staerke", instance.staerke)
        instance.feld1Name = validated_data.get("feld1Name", instance.feld1Name)
        instance.feld1Value = validated_data.get("feld1Value", instance.feld1Value)
        instance.feld2Name = validated_data.get("feld2Name", instance.feld2Name)
        instance.feld2Value = validated_data.get("feld2Value", instance.feld2Value)
        instance.feld3Name = validated_data.get("feld3Name", instance.feld3Name)
        instance.feld3Value = validated_data.get("feld3Value", instance.feld3Value)
        instance.feld4Name = validated_data.get("feld4Name", instance.feld4Name)
        instance.feld4Value = validated_data.get("feld4Value", instance.feld4Value)
        instance.feld5Name = validated_data.get("feld5Name", instance.feld5Name)
        instance.feld5Value = validated_data.get("feld5Value", instance.feld5Value)
        instance.durchfuehrung = validated_data.get("durchfuehrung", instance.durchfuehrung)
        instance.rueckbau = validated_data.get("rueckbau", instance.rueckbau)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)

        instance.save()

        if len(fahrzeuge_data) > 0:
            for fahrzeuge in fahrzeuge_data:
                instance.fahrzeuge.add(fahrzeuge)
        else:
            instance.fahrzeuge.set([])
        
        if len(verstaendigung_data) > 0:
            for verstaendigung in verstaendigung_data:
                instance.verstaendigung.add(verstaendigung)
        else:
            instance.verstaendigung.set([])

        return instance

    class Meta:
        model = Massnahme
        fields = '__all__'