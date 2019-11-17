from django.contrib import admin
from app.models import User, Historia, Pub, PubComentario, PubLike, PubSave, Follow

admin.site.register(User)
admin.site.register(Historia)
admin.site.register(Pub)
admin.site.register(PubComentario)
admin.site.register(PubLike)
admin.site.register(PubSave)
admin.site.register(Follow)