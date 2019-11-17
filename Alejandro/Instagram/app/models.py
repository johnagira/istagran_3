from django.db import models

class User(models.Model): 
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='app/usuarios/', blank=True, null=True)
    
class Historia(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='app/historias/', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

class Pub(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='app/publicaciones/', blank=True, null=True)
    
class PubComentario(models.Model):
    id_publicacion = models.ForeignKey(Pub, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()
    
class PubLike(models.Model):
    id_publicacion = models.ForeignKey(Pub, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
class PubSave(models.Model): 
    id_publicacion = models.ForeignKey(Pub, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Follow(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='id_usuario')
    id_usuario_seguido = models.ForeignKey(User, on_delete=models.CASCADE, related_name='id_usuario_seguido')