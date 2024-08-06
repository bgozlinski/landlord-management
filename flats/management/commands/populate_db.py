# your_app/management/commands/populate_db.py

from django.core.management.base import BaseCommand
from flats.models import Flat
from tenants.models import Tenant
from rents.models import Rent
from costs.models import Cost
from datetime import date, timedelta
import random
from faker import Faker


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create Flats
        flats = []
        for i in range(6):  # 6 flats
            flat = Flat.objects.create(
                city_name=fake.city(),
                street_name=fake.street_name(),
                street_number=fake.building_number(),
                flat_number=f'{random.randint(1, 20)}{random.choice("ABCD")}',
                flat_floor=random.randint(1, 10),
                flat_size_sqm=round(random.uniform(50.0, 200.0), 2)
            )
            flats.append(flat)

        # Create Tenants
        tenants = []
        for i in range(20):  # 20 tenants
            tenant = Tenant.objects.create_user(
                email=fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone_number=fake.phone_number(),
                password=fake.password()
            )
            tenants.append(tenant)

        # Assign one current tenant per flat
        today = date.today()
        for i in range(6):
            tenants[i].flat = flats[i]
            tenants[i].save()
            Rent.objects.create(
                flat=flats[i],
                tenant=tenants[i],
                amount_total=round(random.uniform(1000.0, 3000.0), 2),
                rent_begin=today,
                rent_stop=None  # Current tenants have no end date yet
            )

        # Create Rent Records for previous tenants
        for i in range(6, 20):
            flat = random.choice(flats)
            rent_begin = today - timedelta(days=random.randint(365, 1095))  # Random start date between 1-3 years ago
            rent_stop = rent_begin + timedelta(days=random.randint(180, 365))  # Random end date 6-12 months later
            Rent.objects.create(
                flat=flat,
                tenant=tenants[i],
                amount_total=round(random.uniform(1000.0, 3000.0), 2),
                rent_begin=rent_begin,
                rent_stop=rent_stop
            )

        # Create Costs for flats
        cost_types = ['electricity', 'gas', 'water', 'other']
        for flat in flats:
            for _ in range(random.randint(3, 7)):  # Each flat has 3 to 7 cost entries
                Cost.objects.create(
                    flat=flat,
                    cost_type=random.choice(cost_types),
                    amount=round(random.uniform(50.0, 500.0), 2),
                    invoice_number=fake.unique.numerify(text='INV#####'),
                    invoice_date=fake.date_this_year(),
                    cost_date_to_pay=fake.date_this_year(),
                    cost_is_paid=fake.boolean()
                )

        self.stdout.write(self.style.SUCCESS('Database populated with sample data'))
