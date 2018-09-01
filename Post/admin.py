from django.contrib import admin
from .models import Post, Comment
from contact.models import Contact#aynı dosya dizininde olduğumuz için . ile bu dizindeki model anlamı katıldı.
# Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'publishing_date','slug']
    list_display_links = ['title', 'publishing_date'] #üzerine tıklandığında link verir
    list_filter = ['publishing_date']
    search_fields = ['title', 'content']



    class Meta:
        model = Post

class ContactAdmin(admin.ModelAdmin):

    list_display = ['name', 'message', 'sending_date']
    list_display_links = ['message']
    list_filter = ['sending_date']
    search_fields = ['message','name']

    class Meta:
        model = Contact

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'content', 'created_date']
    list_display_links = ['post','content']
    list_filter = ['created_date']
    search_fields = ['content', 'post']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)