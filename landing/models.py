from django.db import models
import xml.etree.cElementTree as et


def is_svg(filename):
    tag = None
    with open(filename, "r") as f:
        try:
            for event, el in et.iterparse(f, ('start',)):
                tag = el.tag
                break
        except et.ParseError:
            pass
    return tag == '{http://www.w3.org/2000/svg}svg'


def validate_svg(file):
    if not is_svg(file):
        raise ValidationError("File not svg")


class Address(models.Model):
    title = models.CharField('Название', max_length=50, unique=True)
    address = models.CharField('Адрес', max_length=50, unique=True)
    phone = models.CharField('Телефон', max_length=50)
    metro = models.CharField('Метро', max_length=50)
    email = models.CharField('Почта', max_length=50)
    time = models.CharField('Время работы', max_length=50)
    time_weekend = models.CharField('Время работы в выходные', max_length=50, null=True, blank=True)
    icon = models.ImageField('Иконка')

    class Meta:
        verbose_name = 'адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.title


class Social(models.Model):
    title = models.CharField('Название', max_length=50, unique=True)
    url = models.CharField('Ссылка', max_length=50, unique=True)
    icon = models.ImageField('Иконка', unique=True)

    class Meta:
        verbose_name = 'социальную сеть'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField('Название', max_length=50, unique=True)
    slug = models.SlugField('Slug', unique=True)

    class Meta:
        verbose_name = 'событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField('Название', max_length=255)
    image = models.ImageField()
    events = models.ManyToManyField(Event, related_name='images')

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'Изображения'


class Menu(models.Model):
    title = models.CharField('Название', max_length=50)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, verbose_name='Событие')
    special = models.BooleanField('Специальное предложение', default=False)

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return str(self.event) + ': ' + self.title


class MenuItem(models.Model):
    title = models.CharField('Название', max_length=50)
    composition = models.CharField('Состав', max_length=50, null=True)
    weight = models.CharField('Вес, г.', max_length=50, null=True)
    price = models.CharField('Цена', max_length=50, null=True)

    menus = models.ManyToManyField(Menu, related_name='items', verbose_name='Меню')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title + ' | ' + self.weight + ' | ' + self.price
