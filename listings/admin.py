from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
  list_display_links = ('id','title') #!to can click in title and go 
  list_filter=('realtor',) # ?to filter
  list_editable = ('is_published',)#* to can publish and un published
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')#$ to search 
  list_pre_page=25



admin.site.register(Listing, ListingAdmin)