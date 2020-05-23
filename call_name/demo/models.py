from django.db import models

# Create your models here.


class Students(models.Model):

    name = models.CharField(max_length=64)
    is_mark = models.BooleanField(default=False)

    class Meta:
        db_table = 'tb_students'
