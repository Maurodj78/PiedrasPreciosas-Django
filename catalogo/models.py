from django.db import models


# Create your models here.
class Producto(models.Model):
    oid = models.AutoField(primary_key=True, unique=True)
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=20, verbose_name="titulo")
    description = models.TextField(verbose_name="descripcion")
    image = models.ImageField(verbose_name="imagen", upload_to="catalogos")
    create = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    update = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Catalogo"
        verbose_name_plural = "Catalogos"
        ordering = ["oid"]
