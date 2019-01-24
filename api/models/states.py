from django.db import models


class State(models.Model):
    FIPS_Code_State = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=1024)


class StateRevenue(models.Model):
    State = models.ForeignKey(
        State,
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

