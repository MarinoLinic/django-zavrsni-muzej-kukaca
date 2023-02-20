from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import homepage, KukacList, KukacDetailView, KukacCreateView, KukacUpdateView, KukacDeleteView, display_kukac_images

class TestUrls(SimpleTestCase):

    def test_homepage_url_resolves(self):
        url = reverse('main:homepage')
        self.assertEqual(resolve(url).func, homepage)

    def test_kukac_detail_url_resolves(self):
        url = reverse('main:detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, KukacDetailView)

    def test_kukac_create_url_resolves(self):
        url = reverse('main:create')
        self.assertEqual(resolve(url).func.view_class, KukacCreateView)

    def test_kukac_update_url_resolves(self):
        url = reverse('main:edit', args=[1])
        self.assertEqual(resolve(url).func.view_class, KukacUpdateView)

    def test_kukac_delete_url_resolves(self):
        url = reverse('main:delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, KukacDeleteView)

    def test_kukac_list_images_url_resolves(self):
        url = reverse('main:list')
        self.assertEqual(resolve(url).func, display_kukac_images)