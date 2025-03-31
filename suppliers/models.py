from django.db import models


class Supplier(models.Model):
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=255, verbose_name="Название")
    email = models.EmailField(verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")

    supplier = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name="clients", verbose_name="Поставщик"
    )

    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Задолженность")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES, editable=False, verbose_name="Уровень иерархии")

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return self.name

    def calculate_level(self):
        """Рассчитываем уровень иерархии, проходя вверх по цепочке поставщиков."""
        if not self.supplier:
            return 0  # Завод (нулевой уровень)
        return self.supplier.calculate_level() + 1  # Уровень на 1 больше, чем у поставщика

    def save(self, *args, **kwargs):
        """Перед сохранением вычисляем уровень"""
        self.level = self.calculate_level()
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода на рынок")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="products", verbose_name="Принадлежит")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name} ({self.model})"
