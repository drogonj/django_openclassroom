
from django.urls import reverse_lazy, reverse
from rest_framework.test import APITestCase
from shop.models import Category
from shop.serializers import ProductSerializer

class TestCategory(APITestCase):
    url = reverse_lazy('category-list')

    def format_datetime(self, value):
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def get_product_detail_data(self, queryset):
        serializer = ProductSerializer(queryset, many=True)
        return serializer.data

    def test_list(self):
        category = Category.objects.create(name='Fruits', active=True)
        Category.objects.create(name='Legumes', active=False)

        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)
        excepted = [
            {
                'id': category.pk,
                'name': category.name,
                'date_created': self.format_datetime(category.date_created),
                'date_updated': self.format_datetime(category.date_updated),
            }
        ]
        self.assertEqual(excepted, response.json())

    def test_detail(self):
        category = Category.objects.create(name='Viennoiseries', active=True)
        url_detail = reverse('category-detail', kwargs={'pk': category.pk})
        response = self.client.get(url_detail)

        self.assertEqual(response.status_code, 200)
        excepted = {
            'id': category.pk,
            'name': category.name,
            'date_created': self.format_datetime(category.date_created),
            'date_updated': self.format_datetime(category.date_updated),
            'products': self.get_product_detail_data(category.products.filter(active=True)),
        }
        self.assertEqual(excepted, response.json())


    def test_create(self):
        self.assertFalse(Category.objects.exists())
        response = self.client.post(self.url, data={'name': 'Nouvelle categorie'})
        self.assertEqual(response.status_code, 405)
        self.assertFalse(Category.objects.exists())