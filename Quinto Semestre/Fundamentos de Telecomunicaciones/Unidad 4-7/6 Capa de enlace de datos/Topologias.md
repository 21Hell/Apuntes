## Topologías física y lógica

Como aprendió en el tema anterior, la capa de enlace de datos prepara los datos de red para la red física. Debe conocer la topología lógica de una red para poder determinar lo que se necesita para transferir tramas de un dispositivo a otro. En este tema se explican las formas en que la capa de vínculo de datos funciona con diferentes topologías de red lógicas.

La topología de una red es la configuración o relación de los dispositivos de red y las interconexiones entre ellos.

Existen dos tipos de topologías utilizadas al describir redes LAN y WAN:

-   **Topología física** – Identifica las conexiones físicas y cómo se interconectan los dispositivos finales y los dispositivos intermedios (es decir, routers, switches y puntos de acceso inalámbrico). La topología también puede incluir la ubicación específica del dispositivo, como el número de habitación y la ubicación en el rack del equipo. Las topologías físicas generalmente son punto a punto o en estrella.
-   **Topología lógica** - Se refiere a la forma en que una red transfiere tramas de un nodo al siguiente. Esta topología identifica las conexiones virtuales mediante interfaces de dispositivo y esquemas de direccionamiento IP de capa 3.

La capa de enlace de datos “ve” la topología lógica de una red al controlar el acceso de datos a los medios. Es la topología lógica la que influye en el tipo de trama de red y control de acceso a los medios que se utilizan.

La figura muestra una topología **física** de ejemplo para una red de ejemplo pequeña.
### Topología física
![[Pasted image 20220920190437.png]]


### Topología lógica
![[Pasted image 20220920190529.png]]




## Topología WAN de punto a punto

Las topologías físicas punto a punto conectan dos nodos directamente, como se muestra en la figura. En esta disposición, los dos nodos no tienen que compartir los medios con otros hosts. Además, cuando se utiliza un protocolo de comunicaciones en serie, como el Protocolo punto a punto (PPP), un nodo no tiene que hacer ninguna determinación sobre si una trama entrante está destinada para él u otro nodo. Por lo tanto, los protocolos de enlace de datos lógicos pueden ser muy simples, dado que todas las tramas en los medios solo pueden transferirse entre los dos nodos. El nodo coloca las tramas en los medios en un extremo y esas tramas son tomadas de los medios por el nodo en el otro extremo del circuito punto a punto.

![[Pasted image 20220920190642.png]]

**Nota**: Una conexión punto a punto a través de Ethernet requiere que el dispositivo determine si la trama entrante está destinada a este nodo.

Un nodo de origen y destino puede estar conectado indirectamente entre sí a través de cierta distancia geográfica utilizando múltiples dispositivos intermedios. Sin embargo, el uso de dispositivos físicos en la red no afecta la topología lógica, como se ilustra en la figura. En la figura, agregar conexiones físicas intermedias puede no cambiar la topología lógica. La conexión lógica punto a punto es la misma.

![[Pasted image 20220920190711.png]]



## Topologías de LAN

En las LAN multiacceso, los dispositivos finales (es decir, nodos) están interconectados utilizando topologías estrella o estrella extendida, como se muestra en la figura. En este tipo de topología, los dispositivos finales están conectados a un dispositivo intermediario central, en este caso, un switch Ethernet. A **extended star** extiende esta topología interconectando varios switches Ethernet. La topología en estrella es fácil de instalar, muy escalable (es fácil agregar y quitar dispositivos finales) y de fácil para la resolución de problemas. Las primeras topologías en estrella interconectaban terminales mediante Ethernet hubs.

A veces, es posible que solo haya dos dispositivos conectados en la LAN Ethernet. Un ejemplo son dos routers interconectados. Este sería un ejemplo de Ethernet utilizado en una topología punto a punto.

**Topologías LAN heredadas**

Las tecnologías antiguas Ethernet y Token Ring LAN heredadas incluían otros dos tipos de topologías:

-   **Bus** - Todos los sistemas finales se encadenan entre sí y terminan de algún modo en cada extremo. No se requieren dispositivos de infraestructura, como switches, para interconectar los dispositivos finales. Las redes Ethernet heredadas a menudo eran topologías de bus que usaban cables coaxiales porque era económico y fácil de configurar.
-   **Anillo** - Los sistemas finales se conectan a su respectivo vecino y forman un anillo. El anillo no necesita ser terminado, a diferencia de la topología del bus. La interfaz de datos distribuidos de fibra heredada (FDDI) y las redes Token Ring usaban topologías de anillo.

Las figuras ilustran cómo los dispositivos finales están interconectados en las LAN. Es común que una línea recta en un gráfico de redes represente una red LAN Ethernet que incluye una estrella simple y una estrella extendida.

### Topologías físicas

![[Pasted image 20220920190756.png]]



## Comunicación Dúplex completo y semidúplex

Comprender la comunicación dúplex es importante cuando se habla de las topologías LAN, ya que se refiere a la dirección de la transmisión de datos entre dos dispositivos. Hay dos modos comunes de dúplex.

**Comunicación semidúplex**

Los dos dispositivos pueden transmitir y recibir en los medios pero no pueden hacerlo simultáneamente. Las WLAN y las topologías de bus heredadas con swithes Ethernet utilizan el modo semidúplex. Semidúplex permite que solo un dispositivo envíe o reciba a la vez en el medio compartido. Haga clic en Reproducir en la figura para ver la animación que muestra la comunicación semidúplex.


**Comunicación dúplex completa**

Ambos dispositivos pueden transmitir y recibir simultáneamente en los medios compartidos. La capa de enlace de datos supone que los medios están disponibles para transmitir para ambos nodos en cualquier momento. Los switches Ethernet operan en el modo de dúplex completo de forma predeterminada, pero pueden funcionar en semidúplex si se conectan a un dispositivo como un dispositivo externo. Haga clic en Reproducir en la figura para ver la animación que muestra la comunicación dúplex completo.


## Métodos de control de acceso

Las LAN Ethernet y WLAN son un ejemplo de una red de accesos múltiples. Una red multiacceso es una red que puede tener dos o más dispositivos finales que intentan acceder a la red simultáneamente.

Algunas redes de acceso múltiple requieren reglas que rijan la forma de compartir los medios físicos. Hay dos métodos básicos de control de acceso al medio para medios compartidos:

-   Acceso por contienda
-   Acceso controlado

**Acceso basado en la contención** 

En las redes multiacceso basadas en contencion, todos los nodos operan en semidúplex, compitiendo por el uso del medio. Sin embargo, solo un dispositivo puede enviar a la vez. Por lo tanto, hay un proceso si más de un dispositivo transmite al mismo tiempo. Algunos ejemplos de métodos de acceso basados en contencion son los siguientes:

-   Acceso múltiple con detección de colisiones (CSMA/CD) utilizado en LAN Ethernet de topología de bus heredada
-   El operador detecta el acceso múltiple con prevención de colisiones (CSMA / CA) utilizado en LAN inalámbricas
![[Pasted image 20220920190851.png]]


**Acceso controlado**

En una red de acceso múltiple basada en control, cada nodo tiene su propio tiempo para usar el medio. Estos tipos deterministas de redes no son eficientes porque un dispositivo debe aguardar su turno para acceder al medio. Algunos ejemplos de redes multiacceso que utilizan acceso controlado son los siguientes:

-   Anillo de TokenLegacy
-   ARCNETheredado

![[Pasted image 20220920190919.png]]


## Acceso por contención: CSMA/CD

Entre los ejemplos de redes de acceso basadas en controversias se incluyen los siguientes:

-   LAN inalámbrica (utiliza CSMA/CA)
-   LAN Ethernet de topología de bus heredada (utiliza CSMA/CD)
-   LAN Ethernet heredada con un hub (utiliza CSMA/CD)

Estas redes funcionan en modo semidúplex, lo que significa que solo un dispositivo puede enviar o recibir a la vez. Esto requiere un proceso para gestionar cuándo puede enviar un dispositivo y qué sucede cuando múltiples dispositivos envían al mismo tiempo.

Si dos dispositivos transmiten al mismo tiempo, se produce una colisión. Para las LAN Ethernet heredadas, ambos dispositivos detectarán la colisión en la red. Esta es la parte de detección de colisiones (CD) de CSMA/CD. La NIC compara los datos transmitidos con los datos recibidos, o al reconocer que la amplitud de la señal es más alta de lo normal en los medios. Los datos enviados por ambos dispositivos se dañarán y deberán enviarse nuevamente.


**PC1 envía una trama**


La PC1 tiene una trama que se debe enviar a la PC3. La NIC de PC1 necesita determinar si algún dispositivo está transmitiendo en el medio. Si no detecta un proveedor de señal, en otras palabras, si no recibe transmisiones de otro dispositivo, asumirá que la red está disponible para enviar.

La NIC PC1 envía la trama Ethernet cuando el medio está disponible, como se muestra en la figura.

![[Pasted image 20220920191125.png]]

**El hub recibe la trama**

El hub Ethernet recibe y envía la trama. Un hub de Ethernet también se conoce como repetidor multipuerto. Todos los bits que se reciben de un puerto entrante se regeneran y envían a todos los demás puertos, como se indica en la figura.

Si otro dispositivo, como una PC2, quiere transmitir, pero está recibiendo una trama, deberá esperar hasta que el canal esté libre.
![[Pasted image 20220920191107.png]]


**El Hub envia la trama**

Todos los dispositivos que están conectados al hub reciben la trama. Dado que la trama tiene una dirección destino de enlace de datos para la PC3, solo ese dispositivo aceptará y copiará toda la trama. Todas las demás NIC del dispositivo ignorarán la trama, como se muestra en la figura.

![[Pasted image 20220920191226.png]]


## Acceso por contención: CSMA/CA

Otra forma de CSMA utilizada por las WLAN IEEE 802.11 es el acceso múltiple / detección de colisión de detección de portadora (CSMA / CA).

CSMA/CA utiliza un método similar a CSMA/CD para detectar si el medio está libre. CSMA/CA usa técnicas adicionales. En entornos inalámbricos, es posible que un dispositivo no detecte una colisión. CSMA/CA no detecta colisiones pero intenta evitarlas ya que aguarda antes de transmitir. Cada dispositivo que transmite incluye la duración que necesita para la transmisión. Todos los demás dispositivos inalámbricos reciben esta información y saben durante cuánto tiempo el medio no estará disponible.

En la figura, si el host A recibe una trama inalámbrica desde el punto de acceso, los hosts B y C también verán la trama y cuánto tiempo el medio no estará disponible.


![[Pasted image 20220920191355.png]]



Luego de que un dispositivos inalámbricos envía una trama 802.11, el receptor devuelve un acuso de recibo para que el emisor sepa que se recibió la trama.

Ya sea que es una red LAN Ethernet con concentradores o una red WLAN, los sistemas por contención no escalan bien bajo un uso intensivo de los medios.

**Nota**: Las redes LAN Ethernet con switches no utilizan sistemas por contención porque el switch y la NIC de host operan en el modo de dúplex completo.