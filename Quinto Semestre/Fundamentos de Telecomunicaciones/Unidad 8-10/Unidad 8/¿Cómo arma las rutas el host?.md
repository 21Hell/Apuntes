## La decisión de reenvío de host

Con IPv4 e IPv6, los paquetes siempre se crean en el host de origen. El host de origen debe poder dirigir el paquete al host de destino. Para ello, los dispositivos finales de host crean su propia tabla de enrutamiento. En este tema se explica cómo los dispositivos finales utilizan las tablas de enrutamiento.

Otra función de la capa de red es dirigir los paquetes entre hosts. Un host puede enviar un paquete a lo siguiente:

-   **Itself** - A host can ping itself by sending a packet to a special IPv4 address of 127.0.0.1 or an IPv6 address ::1, que se conoce como la interfaz de bucle invertido. El hacer ping a la interfaz de bucle invertido, pone a prueba la pila del protocolo TCP/IP en el host.
-   **Host local** - este es un host de destino que se encuentra en la misma red local que el host emisor. Los hosts de origen y destino comparten la misma dirección de red.
-   **Host remoto** - este es un host de destino en una red remota. Los hosts de origen y destino no comparten la misma dirección de red.

La figura ilustra la conexión de PC1 a un host local en la misma red y a un host remoto ubicado en otra red.

![[Pasted image 20221004173342.png]]

El dispositivo final de origen determina si un paquete está destinado a un host local o a un host remoto. El dispositivo final de origen determina si la dirección IP de destino está en la misma red en la que está el propio dispositivo de origen. El método de determinación varía según la versión IP:

-   **En IPv4** : el dispositivo de origen utiliza su propia máscara de subred junto con su propia dirección IPv4 y la dirección IPv4 de destino para realizar esta determinación.
-   **En IPv6** : el router local anuncia la dirección de red local (prefijo) a todos los dispositivos de la red.

En una red doméstica o comercial, puede tener varios dispositivos cableados e inalámbricos interconectados mediante un dispositivo intermediario, como un switch LAN o un punto de acceso inalámbrico (WAP). Este dispositivo intermediario proporciona interconexiones entre hosts locales en la red local. Los hosts locales pueden conectarse y compartir información sin la necesidad de dispositivos adicionales. Si un host está enviando un paquete a un dispositivo que está configurado con la misma red IP que el dispositivo host, el paquete simplemente se reenvía desde la interfaz del host, a través del dispositivo intermediario, y directamente al dispositivo de destino.

Por supuesto, en la mayoría de las situaciones queremos que nuestros dispositivos puedan conectarse más allá del segmento de red local, como a otros hogares, negocios e Internet. Los dispositivos que no están en el segmento de red local se denominan "módulo remoto de E/S". Cuando un dispositivo de origen envía un paquete a un dispositivo de destino remoto, se necesita la ayuda de los routers y del enrutamiento. El enrutamiento es el proceso de identificación de la mejor ruta para llegar a un destino. El router conectado al segmento de red local se denomina gateway predeterminado.

## Puerta de Enlace Predeterminada (Gateway)

La puerta de enlace predeterminada es el dispositivo de red (es decir, el router o el switch de capa 3) que puede enrutar el tráfico a otras redes. Si se piensa en una red como si fuera una habitación, el gateway predeterminado es como la puerta. Si desea ingresar a otra habitación o red, debe encontrar la puerta.

En una red, una puerta de enlace predeterminada suele ser un router con estas características:

-   Tiene una dirección IP local en el mismo rango de direcciones que otros hosts en la red local.
-   Puede aceptar datos en la red local y reenviar datos fuera de la red local.
-   Enruta el tráfico a otras redes.

Se requiere una puerta de enlace predeterminada para enviar tráfico fuera de la red local. El tráfico no se puede reenviar fuera de la red local si no hay una puerta de enlace predeterminada, la dirección de la puerta de enlace predeterminada no está configurada o la puerta de enlace predeterminada está desactivada.

## Un host enruta a la puerta de enlace predeterminada

Una tabla de enrutamiento de host generalmente incluirá una puerta de enlace predeterminada. En IPv4, el host recibe la dirección IPv4 de la puerta de enlace predeterminada, ya sea dinámicamente desde el Protocolo de configuración dinámica de host (DHCP) o configurado manualmente. En IPv6, el router anuncia la dirección de la puerta de enlace predeterminada o el host se puede configurar manualmente.

En la figura, PC1 y PC2 están configuradas con la dirección IPv4 de 192.168.10.1 como la puerta de enlace predeterminada.

![[Pasted image 20221004173423.png]]

La configuración de un gateway predeterminado genera una ruta predeterminada en la tabla de enrutamiento de la PC. Una ruta predeterminada es la ruta o camino que la PC utiliza cuando intenta conectarse a la red remota.

Tanto la PC1 como la PC2 tendrán una ruta predeterminada para enviar todo el tráfico destinado a las redes remotas al R1.

## Tablas de enrutamiento de host

En un host de Windows, el comando **route print** o **netstat -r** se puede usar para mostrar la tabla de enrutamiento del host. Los dos comandos generan el mismo resultado. Al principio, los resultados pueden parecer abrumadores, pero son bastante fáciles de entender.

La figura muestra una topología de ejemplo y la salida generada por el **netstat –r** comando.

![[Pasted image 20221004173455.png]]

### Tabla de enrutamiento IPv4 para la PC1
![[Pasted image 20221004173518.png]]

**Nota:** La salida sólo muestra la tabla de rutas IPv4.

Al ingresar el **netstat -r**comando o el comando equivalente, **route print**se muestran tres secciones relacionadas con las conexiones de red TCP / IP actuales:

-   **Lista de interfaces: -** enumera la dirección de control de acceso a medios (MAC) y el número de interfaz asignado de cada interfaz con capacidad de red en el host, incluidos los adaptadores Ethernet, Wi-Fi y Bluetooth.
-   **Tabla de rutas IPv4: -** enumera todas las rutas IPv4 conocidas, incluidas las conexiones directas, la red local y las rutas locales predeterminadas.
-   **Tabla de rutas IPv6: -** Tabla de rutas IPv6: enumera todas las rutas IPv6 conocidas, incluidas las conexiones directas, la red local y las rutas locales predeterminadas.