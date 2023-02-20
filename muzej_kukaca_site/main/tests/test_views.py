from django.test import TestCase, Client
from django.urls import reverse
from main.models import Kukac

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_kukac_list_GET(self):
        response = self.client.get(reverse('main:kukacs'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/kukac_list.html')

    def test_kukac_detail_GET(self):
        kukac = Kukac.objects.create(
            vrsta = "1",
            porodica = "2",
            red = "3",
            spol = "M",
            duljina = "5",
            lokalitet = "6",
            datum_sakupljanja = "2022-07-03",
            opis = "8",
            slika = "images\images\Scolopendra_cingulata_Mt._Carmel_2TvhblA.jpg",
            lovac = None
        )
        response = self.client.get(reverse('main:detail', args=[kukac.pk]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/kukac_detail.html')

    def test_kukac_create_GET(self):
        response = self.client.get(reverse('main:create'))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'main/kukac_form.html')

    def test_kukac_edit_GET(self):
        kukac = Kukac.objects.create(
            vrsta = "1",
            porodica = "2",
            red = "3",
            spol = "M",
            duljina = "5",
            lokalitet = "6",
            datum_sakupljanja = "2022-07-03",
            opis = "8",
            slika = "images\images\Scolopendra_cingulata_Mt._Carmel_2TvhblA.jpg",
            lovac = None
        )
        response = self.client.get(reverse('main:edit', args=[kukac.pk]))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'main/kukac_form.html')

    def test_kukac_delete_GET(self):
        kukac = Kukac.objects.create(
            vrsta = "1",
            porodica = "2",
            red = "3",
            spol = "M",
            duljina = "5",
            lokalitet = "6",
            datum_sakupljanja = "2022-07-03",
            opis = "8",
            slika = "images\images\Scolopendra_cingulata_Mt._Carmel_2TvhblA.jpg",
            lovac = None
        )
        response = self.client.get(reverse('main:delete', args=[kukac.pk]))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'main/kukac_confirm_delete.html')