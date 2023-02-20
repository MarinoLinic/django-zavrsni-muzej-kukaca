from django.test import TestCase
from main.models import Kukac
from django.contrib.auth import get_user_model 
from django.utils import timezone

class TestModels(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@example.com',
            password='testpassword',
        )

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
            lovac = self.user
        )

    def test_kukac(self):
        self.assertEquals(self.kukac1.vrsta, "1")