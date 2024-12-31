from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


PROPERTY_TYPES = [
    ("Apartment", "Apartment"),
    ("House", "House"),
    ("Commercial", "Commercial"),
]

USER_ROLES = [
    ("Admin", "Admin"),
    ("Landlord", "Landlord"),
    ("Tenant", "Tenant"),
]

class User(AbstractUser):
   
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('landlord', 'Landlord'), ('tenant', 'Tenant')], default='tenant')


    REQUIRED_FIELDS = ["email", "first_name", "last_name"]
    
    def save(self, *args, **kwargs):
      
        if self.role.lower() == 'admin':
            self.is_superuser = True
            self.is_staff = True
        super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.username
    def __str__(self):
        return f"{self.username} ({self.role})"
    
    
class Property(models.Model):
    """Model for properties."""
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'Landlord'})
    title = models.CharField(max_length=200)
    address = models.TextField()
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='property_images/')
    more_images = models.ImageField(upload_to='property_images/', blank=True, null=True)


    
    def __str__(self):
        return self.title
    # def __str__(self):
    #     return f"{self.title} - {self.address}
  

    class Meta:
        ordering = ['title'] 


class Lease(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="leases")
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'Tenant'})
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Lease: {self.property.title} - Tenant: {self.tenant.username}"