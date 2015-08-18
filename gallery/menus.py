from menu import Menu, MenuItem
from django.core.urlresolvers import reverse


Menu.add_item("main", MenuItem("Home",reverse("index"),weight=10))
Menu.add_item("main", MenuItem("Add Image",reverse("create"),weight=20))
Menu.add_item("main", MenuItem("About Us",reverse("about"),	weight=20))
Menu.add_item("main", MenuItem("Contact us",reverse("contact"),weight=20))