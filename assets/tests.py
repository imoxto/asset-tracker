from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Company, Employee, Device, DeviceLog

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create an admin user for testing (if needed)
        self.admin_user = User.objects.create_user(username='admin', password='adminpassword', is_staff=True)
        self.client.force_authenticate(user=self.admin_user)

        # Create some test data
        self.company = Company.objects.create(name='Test Company')
        self.employee = Employee.objects.create(name='Test Employee', company=self.company)
        self.device = Device.objects.create(name='Test Device', condition='Good', company=self.company)
        self.device_log = DeviceLog.objects.create(device=self.device, employee=self.employee,
                                                   checked_out='2023-09-03T12:00:00Z')

    def test_company_list(self):
        response = self.client.get('/api/companies/')
        self.assertEqual(response.status_code, 200)

    def test_create_company(self):
        response = self.client.post('/api/companies/', {'name': 'New Company'})
        self.assertEqual(response.status_code, 201)

    def test_employee_list(self):
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, 200)

    # Add more test methods for other views and functionality

