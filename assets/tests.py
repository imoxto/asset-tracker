from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework import status
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
        company_data = {'name': 'New Company'}

        response = self.client.post('/api/companies/', company_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_company = Company.objects.get(name=company_data['name'])

        self.assertEqual(created_company.name, company_data['name'])

    def test_employee_list(self):
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, 200)

