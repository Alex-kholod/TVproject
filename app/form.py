from django import forms

from .models import Supply, Shipment


class AddSupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ('tv', 'count', 'supplier', 'staff', 'storehouse')


class AddShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ('tv', 'count', 'car', 'distributor', 'staff', 'storehouse')