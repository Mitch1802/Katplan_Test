from rest_framework import serializers

from .models import Katastrophe, KatGefahren, KatMassnahmen, KatRollen

from core_apps.rollen.models import Rolle
from core_apps.massnahmen.models import Massnahme
from core_apps.gefahren.models import Gefahr


class KatastropheSerializer(serializers.ModelSerializer):
    rollen = serializers.PrimaryKeyRelatedField(many=True, queryset=Rolle.objects.all())
    massnahmen = serializers.PrimaryKeyRelatedField(many=True, queryset=Massnahme.objects.all())
    gefahren = serializers.PrimaryKeyRelatedField(many=True, queryset=Gefahr.objects.all())

    def create(self, validated_data):
        rollen_data = validated_data.pop('rollen')
        massnahmen_data = validated_data.pop('massnahmen')
        gefahren_data = validated_data.pop('gefahren')

        instance = Katastrophe.objects.create(**validated_data)

        for rol in rollen_data:
            KatRollen.objects.create(kat_id=instance, rol_id=rol)
        
        for mas in massnahmen_data:
            KatMassnahmen.objects.create(kat_id=instance, mas_id=mas)
        
        for gef in gefahren_data:
            KatGefahren.objects.create(kat_id=instance, gef_is=gef)
        
        return instance

    def update(self, instance, validated_data):
        rollen_data = validated_data.pop('rollen')
        massnahmen_data = validated_data.pop('massnahmen')
        gefahren_data = validated_data.pop('gefahren')

        instance.kuerzel = validated_data.get("kuerzel", instance.kuerzel)
        instance.name = validated_data.get("name", instance.name)
        instance.beschreibung = validated_data.get("beschreibung", instance.beschreibung)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)

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
        
        if len(gefahren_data) > 0:
            for gefahren in gefahren_data:
                instance.gefahren.add(gefahren)
        else:
            instance.gefahren.set([])

        return instance

    class Meta:
        model = Katastrophe
        fields = '__all__'
