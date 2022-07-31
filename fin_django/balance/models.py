from django.db import models


class Transaction(models.Model):
    choices = [('debet', 'debet'), ('credit','credit')]
    type = models.CharField(max_length=6, choices=choices, default='credit')
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.type == 'debet':
            return  f'debet: {self.amount} UAH | {self.category} | on {self.date.strftime("%Y-%m-%d %H:%M:%S")}'
        elif self.type == 'credit':
            return f'credit: {self.amount} UAH | {self.category} | on {self.date.strftime("%Y-%m-%d %H:%M:%S")}'
        else:
            return f'type error'

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
