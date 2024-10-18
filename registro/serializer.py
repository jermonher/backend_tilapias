from rest_framework import serializers
from .models import Monitoreo


class MonitoreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitoreo
        fields = ['ph', 'oxigeno', 'temperatura', 'fecha']

    def validate(self, data):
        if not (6.5 <= data['ph'] <= 8.5):
            raise serializers.ValidationError("El pH debe estar entre 6.5 y 8.5.")
        if data['oxigeno'] < 5:
            raise serializers.ValidationError("El nivel de oxígeno no puede ser menor a 5 mg/L.")
        return data

