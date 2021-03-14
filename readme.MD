# Integración vía gRPC entre Django y Golang — Parte 1
Este repositorio hace parte del una serie de tutoriales enfocados a desarrollar un sistema de microservicios con Django y Golang en donde los servicios se comuniquen via gRPC.

En el siguiente link se encuentran descritos:
[Link](https://andrescendales.medium.com/integraci%C3%B3n-v%C3%ADa-grpc-entre-django-y-golang-parte-1-cd9de0b11324)

## Descripcion del proyecto
Simularemos un escenario en donde requieras construir dos servicios. Supongamos que deseas construir el backend de tu e-commerce, en el cual el frontend se comunica con el primer servicio Products Service, este se encargara de gestionar todas las relaciones de los productos con usuarios, clientes, etc.
Por otro lado, decides crear un segundo servicio Specs Service que te permita gestionar las especificaciones tecnicas y de calidad de los productos. Ya que tienen una estructura NoSQL tambien decides usar una base de datos exclusiva para ese servicio en MongoDB.
De esa manera la arquitectura se vera reflejada asi:
![](https://miro.medium.com/max/700/1*cGr6UJG-ezZ82UPUzBzDVg.jpeg)