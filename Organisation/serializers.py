from rest_framework import serializers
from .models import Organisation

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = [
            'uuid', 'name', 'description', 'type',
            'address', 'address_line_one', 'address_line_two',
            'address_line_county', 'address_line_city', 'address_line_postcode'
        ]
