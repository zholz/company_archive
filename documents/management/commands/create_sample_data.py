from django.core.management.base import BaseCommand
from documents.models import Document
import random
import lorem  # If you're using the lorem package for generating text

class Command(BaseCommand):
    help = 'Generates sample documents'

    def handle(self, *args, **kwargs):
        for _ in range(35):
            Document.objects.create(
                title=lorem.sentence(),
                content=lorem.paragraph()
            )
        self.stdout.write(self.style.SUCCESS('Successfully created 35 sample documents'))
