from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    position = models.CharField(max_length=100, verbose_name="Должность")
    description = models.TextField(verbose_name="Описание", blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    
    services = models.ManyToManyField(
        Service, 
        through='EmployeeService',
        related_name='employees'
    )
    
    def __str__(self):
        return f"{self.name} - {self.position}"
    
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

class EmployeeService(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга")
    
    class Meta:
        verbose_name = "Связь сотрудника и услуги"
        verbose_name_plural = "Связи сотрудников и услуг"
        unique_together = ['employee', 'service'] 
    
    def __str__(self):
        return f"{self.employee.name} - {self.service.name}"
    
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"
        ordering = ['-created_at']