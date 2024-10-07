# sistema_reserva

> *Descripción: Desarrolla una aplicación web en Django que permita a los usuarios reservar asientos en eventos de manera que la información sobre los asientos disponibles se actualice en tiempo real para todos los usuarios. El primer equipo que lo logre de manera funcional y con un diseño limpio, gana.*

## Requisitos

#### **Modelos de Django**

Crear un modelo Event con al menos los siguientes campos: nombre del evento, fecha, y cantidad de asientos disponibles.
Crear un modelo Reservation que almacene las reservas de los usuarios para los eventos, con un campo que refiera al evento y al usuario que hizo la reserva.
Autenticación de Usuarios:

Implementar **autenticación** de usuarios para que solo usuarios registrados puedan realizar reservas.
Disponibilidad en Tiempo Real

Utilizar **WebSockets** (puede ser implementado con Django Channels) para actualizar la cantidad de asientos disponibles en tiempo real para todos los usuarios conectados a la página del evento.

**Validación de Asientos**
Asegurar que no se puedan reservar más asientos de los disponibles y manejar concurrentemente varias reservas de distintos usuarios.

**Interfaz de Usuario**

Diseñar una interfaz intuitiva que muestre los eventos disponibles y permita a los usuarios realizar la reserva de asientos. Debe actualizarse en tiempo real cuando se haga una reserva.

## Funcionalidad Extra (Opcional pero se premia)

Añadir un sistema de notificaciones para los usuarios cuando se queden sin asientos disponibles para un evento específico.
Implementar un historial de reservas para cada usuario.

## Objetivo

El equipo que logre completar la implementación primero y tenga una aplicación funcional, con un código limpio y una interfaz de usuario clara, obtiene la nota.
