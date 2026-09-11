import datetime
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from members.models import Member



class Command(BaseCommand):
    help = "Popule la base de données avec la liste initiale des membres."

    def handle(self, *args, **kwargs):
        members_list = [
            {'firstname': 'Emil', 'lastname': 'Refsnes', 'phone': 5551234, 'joined_date': datetime.date(2022, 1, 5)},
            {'firstname': 'Tobias', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None},
            {'firstname': 'Linus', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None},
            {'firstname': 'Lene', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None},
            {'firstname': 'Stalikken', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None}
        ]

        objs = [
            Member(**m, slug=slugify(f"{m['firstname']}-{m['lastname']}")) for m in members_list
        ]

        Member.objects.bulk_create(objs, ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS("Membres ajoutés avec succès !"))
