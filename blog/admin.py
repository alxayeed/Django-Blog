from material.admin.options import MaterialModelAdmin
from material.admin.decorators import register
from .models import Post

# Register your models here.
@register(Post)
class PostAdmin(MaterialModelAdmin):
	list_display = ('title','content','author','date_posted',)
	list_filter = ('title','content','author','date_posted',)
	search_fields = ['title','date_posted','author__username']

