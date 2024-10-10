from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=255)      # Nombre del usuario
    password = models.CharField(max_length=255)  # Contraseña
    email = models.EmailField(unique=True)       # Correo
    rol = models.CharField(max_length=50)        # Rol

    def __str__(self):
        return self.name


class Event(models.Model):
    name_event = models.CharField(max_length=255)  # Nombre del evento
    seating_available = models.IntegerField()      # Asientos disponibles
    date = models.DateField()                      # Fecha del evento
    config = models.JSONField(default=dict)        # Campo de configuración de tipo JSON

    def __str__(self):
        return self.name_event 


class Reservation(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)   # Relación con la tabla Users
    id_event = models.ForeignKey(Event, on_delete=models.CASCADE)  # Relación con Event
    date = models.DateTimeField(auto_now_add=True)                 # Fecha de la reserva

    def __str__(self):
        return f"Reservation by {self.id_user.name} for {self.id_event.name_event}"

class Notification(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)  # Relación con  Users
    message = models.TextField()                                  # notificación
    date = models.DateTimeField(auto_now_add=True)                # Fecha de notificación

    def __str__(self):
        return f"Notification for {self.id_user.name}"