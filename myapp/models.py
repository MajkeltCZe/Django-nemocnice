from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


# nedávát ID a primary key

class Doctor(models.Model):
    name = models.CharField(max_length=40, verbose_name='křestní jméno', help_text='Zadejte jméno doktora')
    lastName = models.CharField(max_length=45, verbose_name='příjmení', help_text='Zadejte příjmení doktora')

    SPECIALITIES_LIST = (
        ('neurologie', 'Neurologie'),
        ('ortopedie', 'Ortopedie'),
        ('pediatrie', 'Pediatrie'),
        ('kardiologie', 'Kardiologie'),
        ('jiné', 'Jiné'),
    )

    specialization = models.CharField(max_length=20, choices=SPECIALITIES_LIST, blank=True,
                                      help_text='Vyberte doktorovu specializaci',
                                      verbose_name="Specializace")

    class Meta:
        verbose_name = 'Doktor'
        verbose_name_plural = 'Doktoři'
        ordering = ['lastName', 'name']

    def __str__(self):
        return f'{self.name} {self.lastName} - {self.specialization}'


class Medicine(models.Model):
    name = models.CharField(max_length=55, verbose_name='Název', help_text='Zadejte název léku')
    description = models.TextField(blank=True, verbose_name='Popis', help_text='Zadejte popis léku')
    quantity = models.PositiveIntegerField(blank=True, null=True,
                                           validators=[MinValueValidator(1), MaxValueValidator(10)],
                                           verbose_name='Množství',
                                           help_text='Zadejte množství podání léku za den (1- 10)')

    class Meta:
        verbose_name = 'lék'
        verbose_name_plural = 'léky'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Pacient(models.Model):
    name = models.CharField(max_length=40, verbose_name='Křestní jméno', help_text='Zadejte křestní jméno pacienta')
    lastName = models.CharField(max_length=45, verbose_name='Příjmení', help_text='Zadejte příjmení pacienta')
    admission = models.DateField(default=timezone.now, verbose_name='Přijetí', help_text='Zadejte datum přijetí '
                                                                                         'pacienta')
    doctors = models.ManyToManyField(Doctor)
    medicine = models.ManyToManyField(Medicine)

    class Meta:
        verbose_name = 'Pacient'
        verbose_name_plural = 'Pacienti'
        ordering = ['admission', 'lastName']

    def __str__(self):
        return f' {self.name} {self.lastName}, datum přijetí: {self.admission} '
