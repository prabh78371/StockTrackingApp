from dataclasses import field, fields
from email.policy import default
from pyexpat import model
from unicodedata import category
from .models import Product,Inventory,Category,Transaction
from rest_framework import serializers

       
class Categoryserilizer(serializers.ModelSerializer):
    # product = serializers.HiddenField(default = 1)
    # barcode_no = serializers.IntegerField(source= 'Product.name',default = 000)
    class Meta:
        model = Category
        fields = ['product','product_code','packs_per_carton']
        depth = 0


class Productserilizer(serializers.ModelSerializer):
    # barcode_number = serializers.HiddenField(default=100)
    category_set = Categoryserilizer(many=True,read_only= True)
    class Meta:
        model = Product
        fields = ['barcode_number','name','category_set']
        

class Inventoryserilizer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['product','quantity']
        depth = 2

class Transactionserilizer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        depth = 0
