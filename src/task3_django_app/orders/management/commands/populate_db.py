from django.core.management.base import BaseCommand
from django.utils import timezone
from orders.models import Customer, Order
import random

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        # Create customers
        customers = []
        for i in range(10):
            customer = Customer.objects.create(
                name=f"Customer {i+1}",
                email=f"customer{i+1}@example.com"
            )
            customers.append(customer)

        # Create orders
        statuses = ['completed', 'pending', 'cancelled']
        for _ in range(100):
            customer = random.choice(customers)
            order_date = timezone.now() - timezone.timedelta(days=random.randint(0, 365))
            Order.objects.create(
                customer=customer,
                order_date=order_date,
                status=random.choice(statuses),
                total_amount=random.uniform(10, 500)
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))