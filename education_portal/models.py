from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Service Categories"

class Service(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='services/icons/', blank=True, null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class HomePageImages(models.Model):
    logo_center = models.ImageField(upload_to='home_page_images/', verbose_name='Logo trung trang', blank=True, null=True)
    image_top_right = models.ImageField(upload_to='home_page_images/', verbose_name='Ảnh góc trên bên phải', blank=True, null=True)
    image_bottom_left = models.ImageField(upload_to='home_page_images/', verbose_name='Ảnh góc dưới bên trái', blank=True, null=True)
    image_bottom_right = models.ImageField(upload_to='home_page_images/', verbose_name='Ảnh góc dưới bên phải', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Hình ảnh trang chủ {self.id}"