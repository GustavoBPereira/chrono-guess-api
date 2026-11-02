from pathlib import Path

from django.test.runner import DiscoverRunner
from django.core.management import call_command

TEST_OCCURRENCES_CSV = Path(__file__).resolve().parent / "core" / "tests" / "fixtures" / "occurrences.csv"


class CustomTestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        dbs = super().setup_databases(**kwargs)
        call_command("load_occurrences", file=str(TEST_OCCURRENCES_CSV))
        return dbs
