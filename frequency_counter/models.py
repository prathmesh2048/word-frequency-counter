from django.db import models

class Web_address(models.Model):
    url = models.CharField(max_length=2000)

    def __str__(self):
        return self.url
    class Meta:
         verbose_name = "Web addresses"

class Results(models.Model):
    associated_url = models.ForeignKey(Web_address, on_delete=models.CASCADE)
    word = models.CharField(max_length=25)
    frequency = models.PositiveIntegerField()


    def __str__(self):
        frequency1 = f'{ self.frequency}'
        return self.word + ' ' +frequency1
    class Meta:
         verbose_name = "Result"