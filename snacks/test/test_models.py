from django.test import TestCase
from django.contrib.auth.models import User
from snacks.models import Product, Favourite


class TestModels(TestCase):
    """Class Testing Models in Snacks App"""

    def setUp(self):
        """Set Up variables used in this test"""
        self.prod_1 = Product.objects.create(
            pk=1,
            ean='3350033118072',
            name='test 1',
            category='cat 1',
            image='product_default.png',
            nutriscore='u'
        )

        self.user_1 = User.objects.create_user(
            pk=1,
            username='Fav Models Unit Test 1',
            email='boggusmail@boggusmail.net'
        )

        self.fav_1 = Favourite.objects.create(
            pk=1,
            date_added='2019-12-20 09:00:00',
            user=self.user_1,
            product=self.prod_1
        )

    def test_Product(self):
        """Testing the Product class' object"""
        self.assertEquals(self.prod_1.pk, 1)
        self.assertEquals(self.prod_1.ean, '3350033118072')
        self.assertEquals(self.prod_1.name, 'test 1')
        self.assertEquals(self.prod_1.nutriscore, 'u')
        self.assertEquals(self.prod_1.category, 'cat 1')

    def test_product_is_saved_on_creation(self):
        """Testing if the overwitten save() methode works, from Product"""
        self.assertEquals(self.prod_1.image, 'product_default.png')

    def test_product_get_absolute_url(self):
        """Testing if the overwitten get_absolute_url() methode works,
        from Product"""
        self.assertEquals(Product.get_absolute_url(self.prod_1),
                          '/snacks/product/1/')

    def test_Favourite(self):
        """Testing the Favourite class' object"""
        self.assertEquals(self.fav_1.pk, 1)
        self.assertEquals(self.fav_1.date_added, '2019-12-20 09:00:00')
        self.assertEquals(self.fav_1.user.pk, 1)
        self.assertEquals(self.fav_1.product.pk, 1)
