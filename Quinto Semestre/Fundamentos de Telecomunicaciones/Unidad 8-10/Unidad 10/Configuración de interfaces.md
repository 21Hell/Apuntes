## Configurar interfaces de routers

En este punto, los routers tienen sus configuraciones básicas. El siguiente paso es configurar sus interfaces. Esto se debe a que los dispositivos finales no pueden acceder a los enrutadores hasta que se configuran las interfaces. Existen muchos tipos diferentes de interfaces para los routers Cisco. Por ejemplo, el router Cisco ISR 4321 está equipado con dos interfaces Gigabit Ethernet:

-   **GigabitEthernet 0/0/0 (G0/0/0)**
-   **GigabitEthernet 0/0/1 (G0/0/1)**

La tarea de configurar una interfaz de enrutador es muy similar a un SVI de administración en un conmutador. Específicamente, incluye la emisión de los siguientes comandos:

![[Pasted image 20221004181057.png]]


**Nota:** Cuando se habilita una interfaz de enrutador, se deben mostrar mensajes de información confirmando el vínculo habilitado.

Aunque el comando **description** no es necesario para habilitar una interfaz, es una buena práctica usarlo. Puede ser útil para solucionar problemas en redes de producción proporcionando información sobre el tipo de red conectada. Si la interfaz se conecta a un ISP o a un proveedor de servicios de telefonía móvil, **description** resulta útil introducir la información de contacto y de conexión de dichos terceros.

**Nota**: El texto de la descripción tiene un límite de 240 caracteres.

Al usar el comando **no shutdown** se activa la interfaz y es similar a darle energía. La interfaz también debe estar conectada a otro dispositivo , como un switch o un router, para que la capa física se active.

**Nota**: En las conexiones entre enrutadores donde no hay un conmutador Ethernet, ambas interfaces de interconexión deben estar configuradas y habilitadas.

## Ejemplo de Configuración de interfaces de routers

En este ejemplo, se habilitarán las interfaces directamente conectadas de R1 en el diagrama de topología.


![[Pasted image 20221004181141.png]]

Para configurar las interfaces en R1, utilice los siguientes comandos.

![[Pasted image 20221004181316.png]]

**Nota:** Observe los mensajes informativos que nos informan de que G0/0/0 y G0/0/1 están activados.

## Verificación de configuración de interfaz

Existen varios comandos que se pueden utilizar para verificar la configuración de interfaz. El más útil de estos es el comando **show ip interface brief** y **show ipv6 interface brief**, como se muestra en el ejemplo.

![[Pasted image 20221004181350.png]]


## Configuración comandos de Verificación

**show ip interface brief**  
**show ipv6 interface brief**

El resultado muestra todas las interfaces, sus direcciones IP y su estado actual. Las interfaces configuradas y conectadas deben mostrar un Estado de «arriba» y Protocolo de «arriba». Cualquier otra cosa indica que existe un problema con la configuración o con el cableado.

**show ip route**  
**show ipv6 route**

Muestra el contenido de la tabla de routing IP que se almacena en la RAM.

**show interfaces**

Muestra estadísticas de todas las interfaces del dispositivo. Sin embargo, este solo mostrará la información de direccionamiento IPv4.

**show ip interfaces**

Muestra las estadísticas de IPv4 correspondientes a todas las interfaces de un router.

**show ipv6 interface**

Muestra las estadísticas de IPv6 correspondientes a todas las interfaces de un router.