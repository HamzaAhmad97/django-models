from django.test import TestCase
from django.urls import reverse

class TestSnackTracker(TestCase):
    def test_snack_list_status_code(self):
        url = reverse("snack_list_view")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_snack_list_view_uses_correct_template(self):
        response = self.client.get(reverse('snack_list_view'))
        self.assertTemplateUsed(response, 'snacks/snack_list.html')