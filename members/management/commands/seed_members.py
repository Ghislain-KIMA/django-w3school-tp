import datetime
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from members.models import Member


class Command(BaseCommand):
    help = "Popule la base de données avec la liste initiale des membres."

    def handle(self, *args, **kwargs):
        members_list = [
            {'firstname': 'Emil', 'lastname': 'Refsnes', 'phone': 55512304, 'joined_date': datetime.date(2022, 1, 5)},
            {'firstname': 'Tobias', 'lastname': 'Refsnes', 'phone': 00000000, 'joined_date': None},
            {'firstname': 'Linus', 'lastname': 'Refsnes', 'phone': 42004100, 'joined_date': None},
            {'firstname': 'Lene', 'lastname': 'Refsnes', 'phone': 12121212, 'joined_date': None},
            {'firstname': 'Stalikken', 'lastname': 'Refsnes', 'phone': 99999999, 'joined_date': None}
        ]

        created_count = 0

        for m in members_list:
            slug = slugify(f"{m['firstname']}-{m['lastname']}")
            
            # get_or_create vérifie si le slug existe déjà
            obj, created = Member.objects.get_or_create(
                slug=slug,
                defaults={
                    'firstname': m['firstname'],
                    'lastname': m['lastname'],
                    'phone': m['phone'],
                    'joined_date': m['joined_date'],
                }
            )
            
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f"Seeding terminé : {created_count} nouveau(x) membre(s) ajouté(s) !")
        )