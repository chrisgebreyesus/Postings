from django.db import models
from django.forms import DateTimeField

class Condition(models.Model):
    condition_description = models.CharField(max_length=50)

    def __str__(self):
        return self.condition_description

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    post_description = models.CharField(max_length=50, \
        help_text='Description of the Posting')
    asking_price = models.FloatField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, \
        help_text='Date of post')
    category = models.ForeignKey(Category, null=True, blank=True, \
        on_delete=models.SET_NULL)
    condition = models.ForeignKey(Condition, null=True, blank=True, \
        on_delete=models.SET_NULL)
    email = models.EmailField(max_length=50, \
        help_text='Email of original poster')

    def __str__(self):
        return self.category.category_name + ': ' + self.post_description 

    def format_asking_price(self):
         return "${:,.2f}".format(self.asking_price)

    class Meta:
        ordering = ('-date_posted',)
    
# Create your models here.
