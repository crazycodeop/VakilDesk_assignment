from django.db import models
from django.utils import timezone
from django.db.models import Sum

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"

    @classmethod
    def get_top_customers(cls, months=6, limit=5):
        six_months_ago = timezone.now() - timezone.timedelta(days=30*months)
        return cls.objects.filter(
            order_date__gte=six_months_ago,
            status='completed'
        ).values('customer__id', 'customer__name'
        ).annotate(
            total_spent=Sum('total_amount')
        ).order_by('-total_spent')[:limit]
