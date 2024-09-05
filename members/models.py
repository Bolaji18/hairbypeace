from django.db import models



class wigs(models.Model):
    item_name = models.CharField(max_length=500, verbose_name="name of Item", null=True)
    price = models.IntegerField( verbose_name="Price Main USD", null=True)
    number = models.IntegerField( verbose_name="number of items", default=1)
    item_colour = models.CharField(verbose_name="colour of item", max_length=300, null=True)
    item_length = models.CharField(max_length=500, verbose_name="Length of item", null=True)
    image1 = models.ImageField(upload_to='images/', verbose_name="image of item", null=True)

class bundle(models.Model):
    item_name = models.CharField(max_length=500, verbose_name="name of Item", null=True)
    number = models.IntegerField( verbose_name="number of items", default=1)
    item_colour = models.CharField(verbose_name="colour of item", max_length=300, null=True, default="Natural color")
    item_length = models.CharField(max_length=500, verbose_name="Length of item", null=True, default="12-40inches")
    image1 = models.ImageField(upload_to='images/', verbose_name="image of item", null=True)
    image2 = models.ImageField(upload_to='images/', verbose_name="image of item", null=True)
    image3 = models.ImageField(upload_to='images/', verbose_name="image of item", null=True)

class cart(models.Model):
    ip= models.CharField(max_length=500, verbose_name="ip")
    item_name = models.CharField(max_length=500, verbose_name="name of Item", null=True)
    price = models.IntegerField( verbose_name="Price Main USD", null=True)
    number = models.IntegerField( verbose_name="number of items", default=1)
    item_colour = models.CharField(verbose_name="colour of item", max_length=300, null=True)
    item_length = models.CharField(max_length=500, verbose_name="Length of item", null=True)
    image1 =  models.CharField(max_length=500, verbose_name="image_name", null=True)

class cart_id(models.Model):
    ide=models.IntegerField( verbose_name="id", null=True)
    username=models.CharField(max_length=500, verbose_name="username")

class cart_wigs(models.Model):
    username=models.CharField(max_length=500, verbose_name="username", null=True)
    item_name = models.CharField(max_length=500, verbose_name="name of Item", null=True)
    price = models.IntegerField( verbose_name="Price Main USD", null=True)
    number = models.IntegerField( verbose_name="number of items", default=1)
    item_colour = models.CharField(verbose_name="colour of item", max_length=300, null=True)
    item_length = models.CharField(max_length=500, verbose_name="Length of item", null=True)
    image1 = models.ImageField(upload_to='images/', verbose_name="image of item", null=True)

class bundleoptions(models.Model):
    drawn = [
        ('single', 'single'),
        ('double', 'double'),
        ('superdouble', 'superdouble'),
    ]
    style = [
        ('natural', 'natural'),
        ('bone', 'bone'),
        ('kinky', 'kinky'),
        ('body', 'body'),
        ('eurasian', 'eurasian'),
        ('pano', 'pano'),
        ('deep', 'deep'),
        ('magic', 'magic'),
        ('wavy', 'wavy'),
    ]
    length= [
        ('8', '8'),
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('16', '16'),
        ('18', '18'),
        ('20', '20'),
        ('22', '22'),
        ('24', '24'),
        ('26', '26'),
        ('28', '28'),
        ('30', '30'),
        ('32', '32'),
    ]
    color= [
        ('natural', 'natural'),
        ('blonde', 'blonde'),
        ('green', 'green'),
        ('pink', 'pink'),
        ('baby-pink', 'baby-pink'),
        ('red', 'red'),
        ('orange', 'orange'),
        ('ginger', 'ginger'),
        ('brown', 'brown'),
        ('purple', 'purple'),
        ('black', 'black'),

    ]

    choice_field = models.CharField(max_length=20, choices=drawn, verbose_name="Drawn")
    choice_field2 = models.CharField(max_length=20, choices=style, verbose_name="Style")
    choice_field3 = models.CharField(max_length=20, choices=length, verbose_name="Length")
    choice_field4 = models.CharField(max_length=20, choices=color, verbose_name="Color")
    price = models.IntegerField( verbose_name="Price Main USD", null=True)

class double_drawn(models.Model):
    length=models.IntegerField(max_length=500, verbose_name="length", null=True)
    price = models.IntegerField( verbose_name="Price Main USD", null=True)
class superdouble_drawn(models.Model):
    length=models.IntegerField(max_length=500, verbose_name="length", null=True)
    price = models.IntegerField( verbose_name="Price Main USD", null=True)
class single_drawn(models.Model):
    length=models.IntegerField(max_length=500, verbose_name="length", null=True)
    price = models.IntegerField( verbose_name="Price Main USD", null=True)
class bundlecart(models.Model):
    username=models.CharField(max_length=500, verbose_name="username", null=True)
    image=models.CharField(max_length=500, verbose_name="image", null=True)
    product = models.CharField(max_length=500, verbose_name="Product", null=True)
    price = models.IntegerField( verbose_name="Price Main USD", null=True)
class customer_details(models.Model):
    username=models.CharField(max_length=500, verbose_name="username", null=True)
    price = models.IntegerField( verbose_name="Price Main USD", null=True)
    email=models.EmailField(max_length=500, verbose_name="Email", null=True)
    phone = models.IntegerField(max_length=500, verbose_name="Phone No", null=True)
    address= models.CharField(max_length=500, verbose_name="address", null=True)
    state = models.CharField(max_length=500, verbose_name="state", null=True)
    country = models.CharField(max_length=500, verbose_name="country", null=True)


