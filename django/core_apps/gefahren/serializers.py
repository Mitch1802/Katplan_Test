from rest_framework import serializers

from .models import Gefahr, GefRollen, GefDokumente, GefMassnahmen

from core_apps.rollen.models import Rolle
from core_apps.massnahmen.models import Massnahme
from core_apps.dokumente.models import Dokument


class GefahrSerializer(serializers.ModelSerializer):
    rollen = serializers.PrimaryKeyRelatedField(many=True, queryset=Rolle.objects.all())
    massnahmen = serializers.PrimaryKeyRelatedField(many=True, queryset=Massnahme.objects.all())
    dokumente = serializers.PrimaryKeyRelatedField(many=True, queryset=Dokument.objects.all())

    def create(self, validated_data):
        rollen_data = validated_data.pop('rollen')
        massnahmen_data = validated_data.pop('massnahmen')
        dokumente_data = validated_data.pop('dokumente')

        instance = Gefahr.objects.create(**validated_data)

        for rol in rollen_data:
            GefRollen.objects.create(gef_id=instance, rol_id=rol)
        
        for mas in massnahmen_data:
            GefMassnahmen.objects.create(gef_id=instance, mas_id=mas)
        
        for dok in dokumente_data:
            GefDokumente.objects.create(gef_id=instance, dok_id=dok)
        
        return instance

    def update(self, instance, validated_data):
        rollen_data = validated_data.pop('rollen')
        massnahmen_data = validated_data.pop('massnahmen')
        dokumente_data = validated_data.pop('dokumente')

        instance.kuerzel = validated_data.get("kuerzel", instance.kuerzel)
        instance.name = validated_data.get("name", instance.name)
        instance.beschreibung = validated_data.get( "beschreibung", instance.beschreibung)
        instance.ausloeser = validated_data.get("ausloeser", instance.ausloeser)
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
        instance.folgen = validated_data.get("folgen", instance.folgen)
        instance.gefahren = validated_data.get("gefahren", instance.gefahren)

        instance.save()

        if len(rollen_data) > 0:
            for rollen in rollen_data:
                instance.rollen.add(rollen)
        else:
            instance.rollen.set([])
        
        if len(massnahmen_data) > 0:
            for massnahmen in massnahmen_data:
                instance.massnahmen.add(massnahmen)
        else:
            instance.massnahmen.set([])
        
        if len(dokumente_data) > 0:
            for dokumente in dokumente_data:
                instance.dokumente.add(dokumente)
        else:
            instance.dokumente.set([])

        return instance

    class Meta:
        model = Gefahr
        fields = '__all__'
