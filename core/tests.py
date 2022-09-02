from django.test import TestCase
from core.models import Post



class PostTesting(TestCase):


    def setUp(self):
        self.blog = Post.objects.create(title='Django', author='dj', slug='django')




    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'django')