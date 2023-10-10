## La capa de enlace de datos

La capa de enlace de datos del modelo OSI (Capa 2), como se muestra en la figura, prepara los datos de red para la red física. La capa de enlace de datos es responsable de las comunicaciones de tarjeta de interfaz de red (NIC) a tarjeta de interfaz de red. La capa de vínculo de datos realiza lo siguiente:

-   Permite que las capas superiores accedan a los medios. El protocolo de capa superior no conoce completamente el tipo de medio que se utiliza para reenviar los datos.
-   Acepta datos, generalmente paquetes de Capa 3 (es decir, IPv4 o IPv6) y los encapsula en tramas de Capa 2.
-   Controla cómo los datos se colocan y reciben en los medios.
-   Intercambia tramas entre puntos finales a través de los medios de red.
-   Recibe datos encapsulados, generalmente paquetes de Capa 3, y los dirige al protocolo de capa superior adecuado.
-   Realiza la detección de errores y rechaza cualquier trama dañada.

![[Pasted image 20220920190023.png]]

En redes de equipos, un nodo es un dispositivo que puede recibir, crear, almacenar o reenviar datos a lo largo de una ruta de comunicaciones. Un nodo puede ser un dispositivo final como un portátil o un teléfono móvil, o un dispositivo intermediario como un Ethernet switch.

Sin la capa de enlace de datos, un protocolo de capa de red, tal como IP, tendría que tomar medidas para conectarse con todos los tipos de medios que pudieran existir a lo largo de la ruta de envío. Además, cada vez que se desarrolla una nueva tecnología de red o medio IP, tendría que adaptarse.

La figura muestra un ejemplo de cómo la capa de enlace de datos agrega información de destino Ethernet de Capa 2 y NIC de origen a un paquete de Capa 3. A continuación, convertiría esta información a un formato compatible con la capa física (es decir, Capa 1).
![[Pasted image 20220920190109.png]]


## Subcapas de enlace de datos IEEE 802 LAN/MAN

Los estándares IEEE 802 LAN/MAN son específicos para LAN Ethernet, LAN inalámbricas (WLAN), redes de área personal inalámbrica (WPAN) y otros tipos de redes locales y metropolitanas. La capa de enlace de datos IEEE 802 LAN/MAN consta de las dos subcapas siguientes:

-   **Control de enlace lógico (LLC)** - Esta subcapa IEEE 802.2 se comunica entre el software de red en las capas superiores y el hardware del dispositivo en las capas inferiores. Coloca en la trama información que identifica qué protocolo de capa de red se utiliza para la trama. Esta información permite que múltiples protocolos de Capa 3, como IPv4 e IPv6, utilicen la misma interfaz de red y medios.
-   **Control de acceso a medios (MAC)** - implementa esta subcapa (IEEE 802.3, 802.11 o 802.15) en hardware. Es responsable de la encapsulación de datos y el control de acceso a los medios. Proporciona direccionamiento de capa de enlace de datos y está integrado con varias tecnologías de capa física.

La figura muestra las dos subcapas (LLC y MAC) de la capa de enlace de datos.

![[Pasted image 20220920190245.png]]


La subcapa LLC toma los datos del protocolo de red, que generalmente es un paquete IPv4 o IPv6, y agrega información de control de Capa 2 para ayudar a entregar el paquete al nodo de destino. 

La subcapa MAC controla la NIC y otro hardware que es responsable de enviar y recibir datos en el medio LAN/MAN con cable o inalámbrico.

La subcapa MAC proporciona encapsulación de datos:

-   **Delimitación de tramas** - El proceso de entramado proporciona delimitadores importantes que se utilizan para identificar un grupo de bits que componen una trama. Estos bits delimitadores proporcionan sincronización entre los nodos de transmisión y de recepción.
-   **Direccionamiento** - proporciona direccionamiento de origen y destino para transportar la trama de capa 2 entre dispositivos en el mismo medio compartido.
-   **Detección de errores** - Cada trama contiene un tráiler utilizado para detectar errores de transmisión.

La subcapa MAC también proporciona control de acceso a medios, lo que permite que varios dispositivos se comuniquen a través de un medio compartido (semidúplex). Las comunicaciones dúplex completo no requieren control de acceso.


## Provisión de acceso a los medios

Cada entorno de red que los paquetes encuentran cuando viajan desde un host local hasta un host remoto puede tener características diferentes. Por ejemplo, una LAN Ethernet generalmente consta de muchos hosts que compiten por el acceso en el medio de red. La subcapa MAC resuelve esto. Con los enlaces serie, el método de acceso sólo puede consistir en una conexión directa entre solo dos dispositivos, generalmente dos routers. Por lo tanto, no requieren las técnicas empleadas por la subcapa MAC IEEE 802.

Las interfaces del router encapsulan el paquete en la trama apropiada. Se utiliza un método adecuado de control de acceso a los medios para acceder a cada enlace. En cualquier intercambio de paquetes de capas de red, puede haber muchas transiciones de medios y capa de enlace de datos.

En cada salto a lo largo de la ruta, un router realiza las siguientes funciones de Capa 2:

1.  Aceptan una trama proveniente de un medio.
2.  Desencapsulan la trama.
3.  Vuelven a encapsular el paquete en una trama nueva.
4.  Reenvían la nueva trama adecuada al medio de ese segmento de la red física.

Pulse Reproducir para ver la animación. El router de la figura tiene una interfaz Ethernet para conectarse a la LAN y una interfaz serial para conectarse a la WAN. A medida que el router procesa tramas, utilizará los servicios de la capa de enlace de datos para recibir la trama desde un medio, desencapsularlo en la PDU de la Capa 3, volver a encapsular la PDU en una trama nueva y colocar la trama en el medio del siguiente enlace de la red.

## Estándares de la capa de enlace de datos

Los protocolos de capa de enlace de datos generalmente no están definidos por la Solicitud de comentarios (RFC), a diferencia de los protocolos de las capas superiores del conjunto TCP / IP. El Grupo de trabajo de ingeniería de Internet (IETF) mantiene los protocolos y servicios funcionales para el conjunto de protocolos TCP / IP en las capas superiores, pero no definen las funciones y el funcionamiento de la capa de acceso a la red TCP / IP.

Las organizaciones de ingeniería que definen estándares abiertos y protocolos que se aplican a la capa de acceso a la red (es decir, las capas físicas y de enlace de datos OSI) incluyen lo siguiente:

-   Instituto de Ingenieros Eléctricos y Electrónicos (IEEE)
-   Unión Internacional de Telecomunicaciones (ITU)
-   Organización Internacional para la Estandarización (ISO)
-   Instituto Nacional Estadounidense de Estándares (ANSI)

Los logotipos de estas organizaciones se muestran en la figura.