from django.db import models
from api.models.states import State


class County(models.Model):
    GFD_ID = models.IntegerField(primary_key=True)
    State = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        primary_key=False,
    )
    FIPS_County = models.IntegerField()
    Name = models.CharField(max_length=1024)


class CountyRevenue(models.Model):
    County = models.ForeignKey(
        County,
        on_delete=models.CASCADE,
        primary_key=False,
    )
    Name = models.CharField(max_length=1024)
    Year = models.IntegerField()
    Population = models.IntegerField()
    Total_Revenue = models.IntegerField()
    Total_Taxes = models.IntegerField()
    Tot_Sales_Gr_Rec_Tax = models.IntegerField()
    Total_License_Taxes = models.IntegerField()
    Total_Income_Taxes = models.IntegerField()
    Death_and_Gift_Tax = models.IntegerField()
    Docum_and_Stock_Tr_Tax = models.IntegerField()
    Severance_Tax = models.IntegerField()
    Taxes_NEC = models.IntegerField()


class CountyExpenditure(models.Model):
    County = models.ForeignKey(
        County,
        on_delete=models.CASCADE,
        primary_key=False,
    )
    Total_Revenue = models.IntegerField()
    Total_Taxes = models.IntegerField()
    Tot_Sales_Gr_Rec_Tax = models.IntegerField()
    Total_License_Taxes = models.IntegerField()
    Total_Income_Taxes = models.IntegerField()
    Death_and_Gift_Tax = models.IntegerField()
    Docum_and_Stock_Tr_Tax = models.IntegerField()
    Severance_Tax = models.IntegerField()
    Taxes_NEC = models.IntegerField()

# Similar to States models, keep this. But for now, let's just store everything in the County table for proof of concept.
# class CountyData(models.Model):
#     """SQLAlchemy model for the Psql database
#     """
#     County = models.ForeignKey(
#         County,
#         on_delete=models.CASCADE,
#         primary_key=False,
#     )
#     Year = models.IntegerField()
#     Population = models.IntegerField()

#     def __str__(self):
#         return '{}'.format(self.name)