from django.db import models


class Producent(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=60)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"


class Kategoria(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


class Apteka(models.Model):
    kategoria = models.ForeignKey(Kategoria, null=True, blank=True, on_delete=models.CASCADE)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE, null=True)
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)
    obraz = models.ImageField(upload_to='obrazy/', default=True)

    def __str__(self):
        return self.nazwa

    # nazwa = models.CharField(max_length=60)
    # opis = models.TextField(blank=True)
    # cena = models.DecimalField(max_digits=99999, decimal_places=2)

    class Meta:
        verbose_name = "Apteka"
        verbose_name_plural = "Apteki"


class Obrazy(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=60)
    opis = models.TextField(blank=True)
    obraz = models.ImageField(upload_to='uploads/')

    class Meta:
        verbose_name = "Obraz"
        verbose_name_plural = "Obrazy"


class Recepty(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=60)
    opis = models.TextField(blank=False)
    nabyto = models.BooleanField(default=False)
    komu_zapisano = models.TextField(blank=False)

    class Meta:
        verbose_name = "Recepta"
        verbose_name_plural = "Recepty"
