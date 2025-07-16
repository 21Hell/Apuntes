## Destino en la misma red

A veces, un host debe enviar un mensaje, pero solo conoce la dirección IP del dispositivo de destino. El host necesita saber la dirección MAC de ese dispositivo, pero ¿cómo se puede descubrir? Ahí es donde la resolución de direcciones se vuelve crítica.

Hay dos direcciones primarias asignadas a un dispositivo en una LAN Ethernet:

-   **Dirección física (la dirección MAC)** – Se utiliza para comunicaciones NIC a NIC en la misma red Ethernet.
-   **Dirección lógica (la dirección IP)** – Se utiliza para enviar el paquete desde el dispositivo de origen al dispositivo de destino. La dirección IP de destino puede estar en la misma red IP que la de origen o en una red remota.

Las direcciones físicas de capa 2 (es decir, las direcciones MAC de Ethernet) se utilizan para entregar la trama de enlace de datos con el paquete IP encapsulado de una NIC a otra NIC que está en la misma red. Si la dirección IP de destino está en la misma red, la dirección MAC de destino es la del dispositivo de destino.

Considere el siguiente ejemplo utilizando representaciones de direcciones MAC simplificadas.

La imagen es un diagrama de red con PC 1 en IP 192.168.10.10/24 con MAC simplificado aa-aa-aa, conectado a un switch en IP 192.168.10.0/24, conectado a PC 2 en IP 192.168.10.11/24 con MAC simplificado 55-55. Debajo del diagrama hay cuatro cuadros que leen de izquierda a derecha: Destino MAC 55-55, MAC de origen aa-aa-aa, IPv4 192.168.10.10 y Destino IPv4 192.168.10.11.

![[Pasted image 20221004175845.png]]

En este ejemplo, PC1 desea enviar un paquete a PC2. La figura muestra las direcciones MAC de origen y destino de Capa 2 y el direccionamiento IPv4 de Capa 3 que se incluirían en el paquete enviado desde PC1.

La trama Ethernet de capa 2 contiene lo siguiente:

-   **Dirección MAC de destino**: esta es la dirección MAC simplificada de PC2, 55-55.
-   **Dirección MAC de origen**: es la dirección MAC simplificada de la NIC Ethernet en PC1, aa-aa-aa.

El paquete IP de capa 3 contiene lo siguiente:

-   **Dirección IPv4 de origen**: esta es la dirección IPv4 de PC1, 192.168.10.10.
-   **Dirección IPv4 de destino**: esta es la dirección IPv4 de PC2, 192.168.10.11.

## Destino en una red remota

Cuando la dirección IP de destino (IPv4 o IPv6) está en una red remota, la dirección MAC de destino será la dirección de gateway predeterminada del host (es decir, la interfaz del router).

Considere el siguiente ejemplo utilizando una representación de dirección MAC simplificada.

![[Pasted image 20221004175925.png]]


En este ejemplo, PC1 desea enviar un paquete a PC2. PC2 se encuentra en una red remota. Dado que la dirección IPv4 de destino no está en la misma red local que PC1, la dirección MAC de destino es la del gateway predeterminado local en el router.

Los routers examinan la dirección IPv4 de destino para determinar la mejor ruta para reenviar el paquete IPv4. Cuando el router recibe una trama de Ethernet, desencapsula la información de capa 2. Por medio de la dirección IP de destino, determina el dispositivo del siguiente salto y desencapsula el paquete IP en una nueva trama de enlace de datos para la interfaz de salida.

En nuestro ejemplo, R1 ahora encapsularía el paquete con la nueva información de dirección de Capa 2 como se muestra en la figura.

![[Pasted image 20221004175942.png]]

La nueva dirección MAC de destino sería la de la interfaz R2 G0/0/1 y la nueva dirección MAC de origen sería la de la interfaz R1 G0/0/1.

A lo largo de cada enlace de una ruta, un paquete IP se encapsula en una trama. El trama es específico de la tecnología de enlace de datos asociada a ese vínculo, como Ethernet. Si el dispositivo del siguiente salto es el destino final, la dirección MAC de destino será la del NIC de Ethernet del dispositivo, como se muestra en la figura.


![[Pasted image 20221004175959.png]]

¿Cómo se asocian las direcciones IP de los paquetes IP en un flujo de datos con las direcciones MAC en cada enlace a lo largo de la ruta hacia el destino? Para los paquetes IPv4, esto se realiza a través de un proceso llamado Protocolo de resolución de direcciones (ARP). Para los paquetes IPv6, el proceso es ICMPv6 Neighbor Discovery (ND).
