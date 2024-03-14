from rest_framework import serializers

from .models import Rolle, RolleKontaktErreichbarkeit, RolleKontaktVerstaendigung

from core_apps.kontakte.models import Kontakt


class RolleSerializer(serializers.ModelSerializer):
    erreichbarkeit = serializers.PrimaryKeyRelatedField(many=True, queryset=Kontakt.objects.all())
    verstaendigung = serializers.PrimaryKeyRelatedField(many=True, queryset=Kontakt.objects.all())


    def create(self, validated_data):
        erreichbarkeit_data = validated_data.pop('erreichbarkeit')
        verstaendigung_data = validated_data.pop('verstaendigung')
        all_entries = Rolle.objects.all()
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

        validated_data["kuerzel"] = f"R{kuerzel_new}"


        instance = Rolle.objects.create(**validated_data)

        for kon in erreichbarkeit_data:
            RolleKontaktErreichbarkeit.objects.create(rol_id=instance, kon_id=kon)
        
        for kon in verstaendigung_data:
            RolleKontaktVerstaendigung.objects.create(rol_id=instance, kon_id=kon)
        
        return instance

    def update(self, instance, validated_data):
        erreichbarkeit_data = validated_data.pop('erreichbarkeit')
        verstaendigung_data = validated_data.pop('verstaendigung')

        instance.name = validated_data.get("name", instance.name)
        instance.beschreibung = validated_data.get("beschreibung", instance.beschreibung)
        instance.notruf = validated_data.get("notruf", instance.notruf)
        instance.aufgaben = validated_data.get("aufgaben", instance.aufgaben)

        instance.save()

        if len(erreichbarkeit_data) > 0:
            for erreichbarkeit in erreichbarkeit_data:
                instance.erreichbarkeit.add(erreichbarkeit)
        else:
            instance.erreichbarkeit.set([])
        
        if len(verstaendigung_data) > 0:
            for verstaendigung in verstaendigung_data:
                instance.verstaendigung.add(verstaendigung)
        else:
            instance.verstaendigung.set([])

        return instance

    class Meta:
        model = Rolle
        fields = '__all__'

