from distutils.command.upload import upload
from rest_framework import serializers
from .models import Producto


class ProductoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    descripcion = serializers.CharField()
    precio = serializers.DecimalField(max_digits = 6,
    decimal_places = 2)
    imagen = serializers.ImageField()
    class Meta:
        model = Producto
        fields = ('id', 'descripcion','precio','imagen')
        
        
 

    def create(self, validated_data):
        """
        Create and return a new `Producto` instance, given the validated data.
        """
        return Producto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Producto` instance, given the validated data.
        """
        instance.name = validated_data.get('descripcion', instance.descripcion)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.imagen = validated_data.get('imagen',instance.imagen)
        instance.save()
        return instance
