from django.core.management.base import BaseCommand
from django.conf import settings
from chronoguess.core.models import Occurrence

class Command(BaseCommand):
    help = "Loads occurrences from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            default=f"{settings.BASE_DIR}/occurrences.csv",
            help="Path to the occurrences CSV file (defaults to <BASE_DIR>/occurrences.csv)",
        )

    def handle(self, *args, **options):
        print("Loading occurrences from CSV...")
        with open(options["file"], 'r', encoding='utf-8') as file:
            for line in file.readlines()[1:]:
                parts = line.strip().split(',')
                if len(parts) != 5:
                    continue
                title, summary, photo_url, year, lang = parts
                Occurrence.objects.get_or_create(
                    title=title,
                    summary=summary,
                    photo_url=photo_url,
                    year=int(year),
                    language=lang
                )
