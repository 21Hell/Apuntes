# Características de la capa física

## Estándares de la capa física

En el tema anterior, obtuvo una visión general de alto nivel de la capa física y su lugar en una red. Este tema profundiza un poco más en los detalles de la capa física. Esto incluye los componentes y los medios utilizados para construir una red, así como los estándares necesarios para que todo funcione en conjunto.

Los protocolos y las operaciones de las capas OSI superiores se llevan a cabo en software diseñado por ingenieros en software e informáticos. El grupo de trabajo de ingeniería de Internet (IETF) define los servicios y protocolos del conjunto TCP/IP.

La capa física consta de circuitos electrónicos, medios y conectores desarrollados por ingenieros. Por lo tanto, es necesario que las principales organizaciones especializadas en ingeniería eléctrica y en comunicaciones definan los estándares que rigen este hardware.

Existen muchas organizaciones internacionales y nacionales, organizaciones de regulación gubernamentales y empresas privadas que intervienen en el establecimiento y el mantenimiento de los estándares de la capa física. Por ejemplo, los estándares de hardware, medios, codificación y señalización de la capa física están definidos y regidos por estas organizaciones de estándares:

-   Organización Internacional para la Estandarización (ISO)
-   Asociación de las Industrias de las Telecomunicaciones (TIA) y Asociación de Industrias Electrónicas (EIA)
-   Unión Internacional de Telecomunicaciones (ITU)
-   Instituto Nacional Estadounidense de Estándares (ANSI)
-   Instituto de Ingenieros Eléctricos y Electrónicos (IEEE)
-   Autoridades nacionales reguladoras de las telecomunicaciones, incluida la Federal Communication Commission (FCC) de los Estados Unidos y el Instituto Europeo de Estándares de Telecomunicaciones (ETSI)

Además de estos, a menudo hay grupos de normas de cableado regionales como CSA (Asociación de Normas Canadienses), CENELEC (Comité Europeo de Normalización Electrotécnica) y JSA / JIS (Asociación de Normas Japonesas), que desarrollan especificaciones locales.

Los estándares de la capa física se implementan en hardware, y los rigen diversos organismos, incluidos los siguientes:  

-   ISO
-   EIA/TIA
-   ITU-T
-   ANSI
-   IEEE

Los estándares TCP/IP se implementan en software, y los rige la IETF.AplicaciónPresentaciónSesiónTransporteRedEnlace de datosFísica

## Componentes físicos

Los estándares de la capa física abarcan tres áreas funcionales:

-   Componentes físicos
-   Codificación
-   Señalización

**Componentes físicos**

Los componentes físicos son los dispositivos de hardware electrónico, medios y otros conectores que transmiten las señales que representan los bits. Todos los componentes de hardware, como NIC, interfaces y conectores, materiales y diseño de los cables, se especifican en los estándares asociados con la capa física. Los diversos puertos e interfaces de un router Cisco 1941 también son ejemplos de componentes físicos con conectores y diagramas de pines específicos derivados de los estándares.

## Codificación

La codificación, o codificación de línea, es un método que se utiliza para convertir una transmisión de bits de datos en un “código” predefinido. Los códigos son grupos de bits utilizados para ofrecer un patrón predecible que pueda reconocer tanto el emisor como el receptor. En otras palabras, la codificación es el método o patrón utilizado para representar la información digital. Similar a la forma en que el código Morse codifica un mensaje con una serie de puntos y guiones.

Por ejemplo, en la codificación Manchester los 0 se representan mediante una transición de voltaje de alto a bajo y los 1 se representan como una transición de voltaje de bajo a alto. Un ejemplo de codificación Manchester se ilustra en la figura. La transición se produce en el medio de cada período de bit. Este tipo de codificación se usa en Ethernet de 10 Mbps. Las velocidades de datos más rápidas requieren codificación más compleja. La codificación Manchester se utiliza en estándares Ethernet más antiguos, como 10BASE-T. Ethernet 100BASE-TX usa codificación 4B / 5B y 1000BASE-T usa codificación 8B / 10B.

La imagen es un gráfico de línea de voltaje a lo largo del tiempo que representa la codificación Manchester de una corriente de siete bits. Hay líneas horizontales separadas uniformemente que representan períodos de bits. También hay una línea vertical dibujada a mitad del eje y utilizada como punto de referencia. A medida que se envía el flujo de bits (señal), hay caídas y aumentos en los niveles de voltaje en el medio de cada período de bits. Si el bit es un cero binario, entonces el voltaje cae en el medio. Si el bit es binario, entonces el voltaje aumenta en el medio. Los bits transmitidos son 0100110.



## Señalización

La capa física debe generar las señales inalámbricas, ópticas o eléctricas que representan los “1” y los “0” en los medios. La forma en que se representan los bits se denomina método de señalización. Los estándares de la capa física deben definir qué tipo de señal representa un “1” y qué tipo de señal representa un “0”. Esto puede ser tan simple como un cambio en el nivel de una señal eléctrica o de un pulso óptico. Por ejemplo, un pulso largo podría representar un 1 mientras que un pulso corto podría representar un 0.

Esto es similar al método de señalización que se utiliza en el código Morse, que puede utilizar una serie de tonos de encendido/apagado, luces o clics para enviar texto a través de cables telefónicos o entre barcos en el mar.

Las figuras muestran señalización

Haga clic en cada botón para ver ilustraciones de señalización para cable de cobre, cable de fibra óptica y medios inalámbricos.

**Señales eléctricas sobre cable**

gráfico de voltaje a lo largo del tiempo que muestra ondas cuadradas con diferentes niveles de picos y valles

VoltajeTiempo

4.2.5

## Ancho de banda

Los diferentes medios físicos admiten la transferencia de bits a distintas velocidades. La transferencia de datos generalmente se discute en términos de ancho de banda. El ancho de banda es la capacidad a la que un medio puede transportar datos. El ancho de banda digital mide la cantidad de datos que pueden fluir desde un lugar hacia otro en un período de tiempo determinado. El ancho de banda generalmente se mide en kilobits por segundo (kbps), megabits por segundo (Mbps) o gigabits por segundo (Gbps). En ocasiones, el ancho de banda se piensa como la velocidad a la que viajan los bits, sin embargo, esto no es adecuado. Por ejemplo, tanto en Ethernet a 10 Mbps como a 100 Mbps, los bits se envían a la velocidad de la electricidad. La diferencia es el número de bits que se transmiten por segundo.

Una combinación de factores determina el ancho de banda práctico de una red:

-   Las propiedades de los medios físicos
-   Las tecnologías seleccionadas para la señalización y la detección de señales de red

Las propiedades de los medios físicos, las tecnologías actuales y las leyes de la física desempeñan una función al momento de determinar el ancho de banda disponible.

En la tabla, se muestran las unidades de medida comúnmente utilizadas para el ancho de banda.
![[Pasted image 20220920182607.png]]
## Terminología del ancho de banda

Los términos utilizados para medir la calidad del ancho de banda incluyen:

-   Latencia
-   Rendimiento
-   Capacidad de transferencia útil

**Latencia**

El concepto de latencia se refiere a la cantidad de tiempo, incluidas las demoras, que les toma a los datos transferirse desde un punto determinado hasta otro.

En una internetwork o una red con múltiples segmentos, el rendimiento no puede ser más rápido que el enlace más lento de la ruta de origen a destino. Incluso si todos los segmentos o gran parte de ellos tienen un ancho de banda elevado, solo se necesita un segmento en la ruta con un rendimiento inferior para crear un cuello de botella en el rendimiento de toda la red.

**Rendimiento**

El rendimiento es la medida de transferencia de bits a través de los medios durante un período de tiempo determinado.

Debido a diferentes factores, el rendimiento generalmente no coincide con el ancho de banda especificado en las implementaciones de la capa física. El rendimiento suele ser menor que el ancho de banda. Hay muchos factores que influyen en el rendimiento:

-   La cantidad de tráfico
-   El tipo de tráfico
-   La latencia creada por la cantidad de dispositivos de red encontrados entre origen y destino

Existen muchas pruebas de velocidad en línea que pueden revelar el rendimiento de una conexión a Internet. En la figura, se proporcionan resultados de ejemplo de una prueba de velocidad.

**Capacidad de transferencia útil (Goodput)**

Existe una tercera medición para evaluar la transferencia de datos utilizables, que se conoce como capacidad de transferencia útil. La capacidad de transferencia útil es la medida de datos utilizables transferidos durante un período determinado. La capacidad de transferencia útil es el rendimiento menos la sobrecarga de tráfico para establecer sesiones, acuses de recibo, encapsulación y bits retransmitidos. La capacidad de transferencia útil siempre es menor que el rendimiento, que generalmente es menor que el ancho de banda.