## Decisión de envío de paquetes del router

En el tema anterior se discutieron las tablas de enrutamiento de host. La mayoría de las redes también contienen routers, que son dispositivos intermediarios. Los routers también contienen tablas de enrutamiento. En este tema se tratan las operaciones del router en la capa de red. Cuando un host envía un paquete a otro host, consulta su tabla de enrutamiento para determinar dónde enviar el paquete. Si el host de destino está en una red remota, el paquete se reenvía a la puerta de enlace predeterminada, que generalmente es el router local.

¿Qué sucede cuando llega un paquete a la interfaz de un router?

El router examina la dirección IP de destino del paquete y busca en su tabla de enrutamiento para determinar dónde reenviar el paquete. La tabla de enrutamiento contiene una lista de todas las direcciones de red conocidas (prefijos) y a dónde reenviar el paquete. Estas entradas se conocen como entradas de ruta o rutas. El router reenviará el paquete utilizando la mejor entrada de ruta que coincida (más larga).
![[Pasted image 20221004173618.png]]
La siguiente tabla muestra la información pertinente de la tabla de ruteo R1.
![[Pasted image 20221004173632.png]]

## Tabla de enrutamiento IP del router

La tabla de enrutamiento del router contiene entradas de ruta de red que enumeran todos los posibles destinos de red conocidos.

La tabla de enrutamiento almacena tres tipos de entradas de ruta:

-   **Redes conectadas directamente** - estas entradas de ruta de red son interfaces de router activas. Los routers agregan una ruta conectada directamente cuando una interfaz se configura con una dirección IP y se activa. Cada interfaz de router está conectada a un segmento de red diferente. En la figura, las redes conectadas directamente en la tabla de enrutamiento IPv4 R1 serían 192.168.10.0/24 y 209.165.200.224/30.
-   **Redes remotas** - estas entradas de ruta de red están conectadas a otros routers. Los routers aprenden acerca de las redes remotas ya sea mediante la configuración explícita de un administrador o mediante el intercambio de información de ruta mediante un protocolo de enrutamiento dinámico. En la figura, la red remota en la tabla de enrutamiento IPv4 R1 sería 10.1.1.0/24.
-   **Ruta predeterminada** - al igual que un host, la mayoría de los routers también incluyen una entrada de ruta predeterminada, una puerta de enlace de último recurso. La ruta predeterminada se utiliza cuando no hay una mejor coincidencia (más larga) en la tabla de enrutamiento IP. En la figura, la tabla de enrutamiento IPv4 R1 probablemente incluiría una ruta predeterminada para reenviar todos los paquetes al router R2.

La figura identifica las redes directamente conectadas y remotas del router R1.

![[Pasted image 20221004173653.png]]


Un router puede descubrir redes remotas de dos maneras:

-   **Manualmente** - las redes remotas se ingresan manualmente en la tabla de rutas mediante rutas estáticas.
-   **Dinámicamente** - las rutas remotas se aprenden automáticamente mediante un protocolo de enrutamiento dinámico.


## Enrutamiento estático

Las rutas estáticas son entradas de ruta que se configuran manualmente. La figura muestra un ejemplo de una ruta estática que se configuró manualmente en el router R1. La ruta estática incluye la dirección de red remota y la dirección IP del router de salto siguiente.

![[Pasted image 20221004173712.png]]

Si hay un cambio en la topología de la red, la ruta estática no se actualiza automáticamente y debe reconfigurarse manualmente. Por ejemplo, en la figura R1 tiene una ruta estática para llegar a la red 10.1.1.0/24 a través de R2. Si esa ruta ya no está disponible, R1 tendría que reconfigurarse con una nueva ruta estática a la red 10.1.1.0/24 a través de R3. Por lo tanto, el router R3 necesitaría tener una entrada de ruta en su tabla de enrutamiento para enviar paquetes destinados a 10.1.1.0/24 a R2.

![[Pasted image 20221004173728.png]]


El enrutamiento estático tiene las siguientes características:

-   Una ruta estática debe configurarse manualmente.
-   El administrador necesita volver a configurar una ruta estática si hay un cambio en la topología y la ruta estática ya no es viable.
-   Una ruta estática es apropiada para una red pequeña y cuando hay pocos o ninguno de los enlaces redundantes.
-   Una ruta estática se usa comúnmente con un protocolo de enrutamiento dinámico para configurar una ruta predeterminada.


## Enrutamiento dinámico

Un protocolo de enrutamiento dinámico permite a los routers aprender automáticamente sobre redes remotas, incluida una ruta predeterminada, de otros routers. Los routers que usan protocolos de enrutamiento dinámico comparten automáticamente la información de enrutamiento con otros routers y compensan cualquier cambio de topología sin que sea necesaria la participación del administrador de la red. Si se produce un cambio en la topología de red, los routers comparten esta información mediante el protocolo de enrutamiento dinámico y actualizan automáticamente sus tablas de enrutamiento.

Los protocolos de enrutamiento dinámico incluyen OSPF y Enhanced Interior Gateway Routing Protocol (EIGRP). La figura muestra un ejemplo de routers R1 y R2 que comparten automáticamente información de red mediante el protocolo de enrutamiento OSPF.

![[Pasted image 20221004174335.png]]

La configuración básica sólo requiere que el administrador de red habilite las redes conectadas directamente dentro del protocolo de enrutamiento dinámico. El protocolo de enrutamiento dinámico hará automáticamente lo siguiente:

-   Detectar redes remotas.
-   Mantener información de enrutamiento actualizada.
-   Elija el mejor camino hacia las redes de destino
-   Intente encontrar una nueva mejor ruta si la ruta actual ya no está disponible

Cuando un router se configura manualmente con una ruta estática o aprende acerca de una red remota dinámicamente mediante un protocolo de enrutamiento dinámico, la dirección de red remota y la dirección de salto siguiente se introducen en la tabla de enrutamiento IP. Como se muestra en la figura, si hay un cambio en la topología de red, los routers se ajustarán automáticamente e intentarán encontrar una nueva mejor ruta.

![[Pasted image 20221004174410.png]]


## Introducción a una tabla de enrutamiento IPv4

Observe en la figura que R2 está conectado a Internet. Por lo tanto, el administrador configuró R1 con una ruta estática predeterminada que envía paquetes a R2 cuando no hay ninguna entrada específica en la tabla de enrutamiento que coincida con la dirección IP de destino. R1 y R2 también están utilizando el enrutamiento OSPF para anunciar redes conectadas directamente.

![[Pasted image 20221004174459.png]]


El comando **show ip route** de EXEC mode privilegiado se utiliza para ver la tabla de enrutamiento IPv4 en un router Cisco IOS. El ejemplo muestra la tabla de enrutamiento IPv4 del router R1. Al principio de cada entrada de tabla de enrutamiento hay un código que se utiliza para identificar el tipo de ruta o cómo se aprendió la ruta. Entre las fuentes de ruta comunes (códigos) se incluyen las siguientes:

-   **L** - Dirección IP de interfaz local conectada directamente
-   **C** – Red conectada directamente
-   **S** — La ruta estática fue configurada manualmente por un administrador
-   **O** - OSPF
-   **D** - EIGRP

La tabla de enrutamiento muestra todas las rutas de destino IPv4 conocidas para R1.

Una ruta conectada directamente se crea automáticamente cuando se configura una interfaz de router con información de dirección IP y se activa. El router añade dos entradas de ruta con los códigos C (es decir, la red conectada) y L (es decir, la dirección IP de la interfaz local de la red conectada). Las entradas de ruta también identifican la interfaz de salida que se utilizará para llegar a la red. Las dos redes conectadas directamente en este ejemplo son 192.168.10.0/24 y 209.165.200.224/30.

Los routers R1 y R2 también están utilizando el protocolo de enrutamiento dinámico OSPF para intercambiar información de router. En la tabla de enrutamiento de ejemplo, R1 tiene una entrada de ruta para la red 10.1.1.0/24 que aprendió dinámicamente del router R2 a través del protocolo de enrutamiento OSPF.

Una ruta predeterminada tiene una dirección de red de todos los ceros. Por ejemplo, la dirección de red IPv4 es 0.0.0.0. Una entrada de ruta estática en la tabla de enrutamiento comienza con un código de S



