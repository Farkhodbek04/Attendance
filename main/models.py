from django.db import models

class Staff(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    status = models.CharField(max_length=25)
    tel_num = models.CharField(max_length=20, null=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            super(Staff, self).save(*args, **kwargs)

class Attendace(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField(auto_now_add=True)
    presence = models.BooleanField(default=False)


