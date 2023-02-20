from django.test import TestCase
from main.models import Kukac
from django.utils import timezone

class TestModels(TestCase):

    def setUp(self):
        self.kukac1 = Kukac.objects.create(
            vrsta = "1",
            porodica = "2",
            red = "3",
            spol = "M",
            duljina = "5",
            lokalitet = "6",
            datum_sakupljanja = timezone.now(),
            opis = "8",
            slika = "images\images\Scolopendra_cingulata_Mt._Carmel_2TvhblA.jpg",
            lovac = None
        )

    def test_kukac(self):
        self.assertEquals(self.kukac1.vrsta, "1")