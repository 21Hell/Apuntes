## Encapsulamiento de Ethernet

Este módulo comienza con una discusión de la tecnología Ethernet incluyendo una explicación de la subcapa MAC y los campos de trama Ethernet.

Ethernet es una de las dos tecnologías LAN utilizadas hoy en día, siendo la otra LAN inalámbricas (WLAN). Ethernet utiliza comunicaciones por cable, incluyendo pares trenzados, enlaces de fibra óptica y cables coaxiales.

Ethernet funciona en la capa de enlace de datos y en la capa física. Es una familia de tecnologías de red definidas en los estándares IEEE 802.2 y 802.3. Ethernet soporta los siguientes anchos de banda de datos:

-   10 Mbps
-   100 Mbps
-   1000 Mbps (1 Gbps)
-   10.000 Mbps (10 Gbps)
-   40,000 Mbps (40 Gbps)
-   100,000 Mbps (100 Gbps)

Como se muestra en la figura, los estándares de Ethernet definen tanto los protocolos de Capa 2 como las tecnologías de Capa 1.

![[Pasted image 20220920192038.png]]
## Subcapas de enlace de datos

Los protocolos IEEE 802 LAN/MAN, incluyendo Ethernet, utilizan las dos subcapas independientes siguientes de la capa de enlace de datos para operar. Son el Control de enlace lógico (LLC) y el Control de acceso a medios (MAC), como se muestra en la figura.

Recuerde que LLC y MAC tienen los siguientes roles en la capa de enlace de datos:

-   **Subcapa LLC** - Esta subcapa IEEE 802.2 se comunica entre el software de red en las capas superiores y el hardware del dispositivo en las capas inferiores. Coloca en la trama información que identifica qué protocolo de capa de red se utiliza para la trama. Esta información permite que múltiples protocolos de Capa 3, como IPv4 e IPv6, utilicen la misma interfaz de red y medios.
-   **Subcapa MAC** - Esta subcapa (IEEE 802.3, 802.11 o 802.15, por ejemplo) se implementa en hardware y es responsable de la encapsulación de datos y control de acceso a medios. Proporciona direccionamiento de capa de enlace de datos y está integrado con varias tecnologías de capa física.
![[Pasted image 20220920192457.png]]

## Subcapa MAC

La subcapa MAC es responsable de la encapsulación de datos y el acceso a los medios.

**Encapsulación de datos**

La encapsulación de datos IEEE 802.3 incluye lo siguiente:

-   **Trama de Ethernet** - Esta es la estructura interna de la trama Ethernet.
-   **Direccionamiento Ethernet** - la trama Ethernet incluye una dirección MAC de origen y destino para entregar la trama Ethernet de NIC Ethernet a NIC Ethernet en la misma LAN.
-   **Detección de errores Ethernet** - La trama Ethernet incluye un avance de secuencia de verificación de trama (FCS) utilizado para la detección de errores.

**Accediendo a los medios**

Como se muestra en la figura, la subcapa MAC IEEE 802.3 incluye las especificaciones para diferentes estándares de comunicaciones Ethernet sobre varios tipos de medios, incluyendo cobre y fibra.

### Estándares Ethernet en la subcapa MAC
![[Pasted image 20220920192535.png]]
Recuerde que Ethernet heredado utiliza una topología de bus o hubs, es un medio compartido, medio dúplex. Ethernet a través de un medio medio dúplex utiliza un método de acceso basado en contencion, detección de accesos múltiples/detección de colisiones (CSMA/CD) Esto garantiza que sólo un dispositivo esté transmitiendo a la vez. CSMA/CD permite que varios dispositivos compartan el mismo medio medio dúplex, detectando una colisión cuando más de un dispositivo intenta transmitir simultáneamente. También proporciona un algoritmo de retroceso para la retransmisión.

Las LAN Ethernet de hoy utilizan switches que funcionan en dúplex completo. Las comunicaciones dúplex completo con switches Ethernet no requieren control de acceso a través de CSMA/CD.

## Campos de trama de Ethernet

El tamaño mínimo de trama de Ethernet es de 64 bytes, y el máximo es de 1518 bytes. Esto incluye todos los bytes del campo de dirección MAC de destino a través del campo de secuencia de verificación de trama (FCS). El campo preámbulo no se incluye al describir el tamaño de una trama.

Cualquier trama de menos de 64 bytes de longitud se considera un fragmento de colisión o una trama corta, y es descartada automáticamente por las estaciones receptoras. Las tramas de más de 1500 bytes de datos se consideran “jumbos” o tramas bebés gigantes.

Si el tamaño de una trama transmitida es menor que el mínimo o mayor que el máximo, el dispositivo receptor descarta la trama. Es posible que las tramas descartadas se originen en colisiones u otras señales no deseadas. Ellas se consideran inválidas Las tramas jumbo suelen ser compatibles con la mayoría de los switches y NIC Fast Ethernet y Gigabit Ethernet.

La figura muestra cada campo en la trama Ethernet. Consulte la tabla para obtener más información sobre la función de cada campo.

### Campos de trama en internet

![[Pasted image 20220920192646.png]]