from django.contrib import admin
from .models import wigs
from .models import bundlecart
from .models import cart_wigs
from .models import bundle
from .models import bundleoptions
from .models import single_drawn
from .models import double_drawn
from .models import superdouble_drawn
from .models import customer_details

admin.site.register(single_drawn)
admin.site.register(double_drawn)
admin.site.register(superdouble_drawn)
admin.site.register(wigs)
admin.site.register(cart_wigs)
admin.site.register(bundle)
admin.site.register(bundlecart)
admin.site.register(customer_details)


# Register your models here.
