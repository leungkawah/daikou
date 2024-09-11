from django.db import models
import uuid


# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="images/")  # MEDIA_ROOT/images/


class GoodsInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    goods = models.ForeignKey("Goods", on_delete=models.RESTRICT, null=True)
