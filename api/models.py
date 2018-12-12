from django.db import models


class CountyData(models.Model):
    """SQLAlchemy model for the Psql database
    """
    SurveyYr = models.IntegerField()
    Name = models.CharField(max_length=1024)
    Population = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)