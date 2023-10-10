## Propiedades del cableado UTP

En el tema anterior, aprendió un poco sobre el cableado de cobre de par trenzado sin blindaje (UTP). Dado que el cableado UTP es el estándar para su uso en las LAN, en este tema se detallan sus ventajas y limitaciones, y qué se puede hacer para evitar problemas.

Cuando se utiliza como medio de red, el cableado (UTP) consta de cuatro pares de hilos codificados por colores que están trenzados entre sí y recubiertos con un revestimiento de plástico flexible. Su tamaño pequeño puede ser una ventaja durante la instalación.

Los cables UTP no utilizan blindaje para contrarrestar los efectos de la EMI y la RFI. En cambio, los diseñadores de cable han descubierto otras formas de limitar el efecto negativo del crosstalk:

-   **Anulación -** Los diseñadores ahora emparejan los hilos en un circuito. Cuando dos hilos en un circuito eléctrico están cerca, los campos magnéticos son exactamente opuestos entre sí. Por lo tanto, los dos campos magnéticos se anulan y también anulan cualquier señal de EMI y RFI externa.
-   **Variando el número de vueltas por par de hilos -** Para mejorar aún más el efecto de anulación de los pares de hilos del circuito, los diseñadores cambian el número de vueltas de cada par de hilos en un cable. Los cables UTP deben seguir especificaciones precisas que rigen cuántas vueltas o trenzas se permiten por metro (3,28 ft) de cable. Observe en la figura que el par naranja y naranja/blanco está menos trenzado que el par azul y azul/blanco. Cada par coloreado se trenza una cantidad de veces distinta.

Los cables UTP dependen exclusivamente del efecto de anulación producido por los pares de hilos trenzados para limitar la degradación de la señal y proporcionar un autoblindaje eficaz de los pares de hilos en los medios de red.

![The figure shows a UTP cable with the jacket partially removed and four twisted pairs which each has a different twist ratio](https://contenthub.netacad.com/courses/itn-dl/aeece082-34fa-11eb-ad9a-f74babed41a6/af204c90-34fa-11eb-ad9a-f74babed41a6/assets/2dd9af32-1c25-11ea-81a0-ffc2c49b96bc.jpg)

4.4.2

## Conectores y estándares de cableado UTP

El cableado UTP cumple con los estándares establecidos en conjunto por la TIA/EIA. En particular, la TIA/EIA-568 estipula los estándares comerciales de cableado para las instalaciones LAN y es el estándar de mayor uso en entornos de cableado LAN. Algunos de los elementos definidos son los siguientes:

Tipos de cables Longitudes del cable Conectores Terminación del cable Métodos para realizar pruebas de cable

El Instituto de Ingenieros Eléctricos y Electrónicos (IEEE) define las características eléctricas del cableado de cobre. IEEE califica el cableado UTP según su rendimiento. Los cables se dividen en categorías según su capacidad para transportar datos de ancho de banda a velocidades mayores. Por ejemplo, el cable de Categoría 5 se utiliza comúnmente en las instalaciones de FastEthernet 100BASE-TX. Otras categorías incluyen el cable de categoría 5 mejorada, la categoría 6 y la categoría 6a.

Los cables de categorías superiores se diseñan y fabrican para admitir velocidades superiores de transmisión de datos. A medida que se desarrollan y adoptan nuevas tecnologías Ethernet de velocidad gigabit, la categoría 5e es ahora el tipo de cable mínimamente aceptable, y la categoría 6 es el tipo recomendado para nuevas instalaciones de edificios.

La figura muestra tres categorías de cable UTP:

-   La categoría 3 se utilizó originalmente para la comunicación de voz a través de líneas de voz, pero más tarde para la transmisión de datos.
-   Las categorías 5 y 5e se utilizan para la transmisión de datos. La categoría 5 soporta 100Mbps y la categoría 5e soporta 1000 Mbps
-   La categoría 6 tiene un separador añadido entre cada par de cables para soportar velocidades más altas. Categoría 6 soporta hasta 10 Gbps.
-   Categoría 7 también soporta 10 Gbps.
-   Categoría 8 soporta 40 Gbps.

Algunos fabricantes producen cables que exceden las especificaciones de la categoría 6a de la TIA/EIA y se refieren a estos como cables de Categoría 7.

La figura muestra la diferencia en la construcción entre las categorías de cable UTP. En la parte superior está la categoría 3 con cuatro cables. En el medio está la categoría 5 y 5e con cuatro pares de cables trenzados. En la parte inferior está la categoría 6 con cuatro pares de cables trenzados, cada uno con un separador de plástico.

Cable de Categoría 3 (UTP)Cable de Categoría 5 o 5e (UTP)Cable de Categoría 6 (STP)

Los cables UTP generalmente se terminan con un conector RJ-45. El estándar TIA/EIA-568 describe las asignaciones de los códigos por colores de los hilos a la asignación de pines (diagrama de pines) de los cables Ethernet.

Como se muestra en la figura, el conector RJ-45 es el componente macho, engarzado al final del cable.

un conector RJ45 y un cable terminado con un conector RJ45

### Conectores RJ-45 para UTP

![this is the image’s alt text](https://contenthub.netacad.com/courses/itn-dl/aeece082-34fa-11eb-ad9a-f74babed41a6/af204c90-34fa-11eb-ad9a-f74babed41a6/assets/2dd9fd55-1c25-11ea-81a0-ffc2c49b96bc.jpg)![this is the image’s alt text](https://contenthub.netacad.com/courses/itn-dl/aeece082-34fa-11eb-ad9a-f74babed41a6/af204c90-34fa-11eb-ad9a-f74babed41a6/assets/2dd9fd56-1c25-11ea-81a0-ffc2c49b96bc.jpg)

El socket, que se muestra en la figura, es el componente hembra de un dispositivo de red, pared, salida de partición de cubículo o panel de conexiones. Cuando se realizan las terminaciones de manera incorrecta, cada cable representa una posible fuente de degradación del rendimiento de la capa física.

vista frontal y lateral de un socket UTP RJ45, incluido el código de color para la terminación del cable

### Socket RJ-45 para UTP

![this is the image’s alt text](https://contenthub.netacad.com/courses/itn-dl/aeece082-34fa-11eb-ad9a-f74babed41a6/af204c90-34fa-11eb-ad9a-f74babed41a6/assets/2dda2464-1c25-11ea-81a0-ffc2c49b96bc.jpg)![this is the image’s alt text](https://contenthub.netacad.com/courses/itn-dl/aeece082-34fa-11eb-ad9a-f74babed41a6/af204c90-34fa-11eb-ad9a-f74babed41a6/assets/2dda2465-1c25-11ea-81a0-ffc2c49b96bc.jpg)

Esta figura muestra un ejemplo de un cable UTP mal terminado. Este conector defectuoso tiene cables que están expuestos, sin torcer y no cubiertos completamente por la funda..

Cable UTP mal terminado que muestra cables sin torsión que se extienden fuera del conector RJ45

### Cable UTP mal terminado

![this is the image's alt text](https://contenthub.netacad.com/courses/itn-dl/aeece082-34fa-11eb-ad9a-f74babed41a6/af204c90-34fa-11eb-ad9a-f74babed41a6/assets/2dda4b73-1c25-11ea-81a0-ffc2c49b96bc.jpg)

La siguiente figura muestra un cable UTP correctamente terminado. Es un buen conector, los hilos están sin trenzar solo en el trecho necesario para unir el conector.

Cable UTP de terminación correcta que muestra la cubierta del cable que se extiende al conector RJ45 lo suficiente como para engarzar de forma segura con los ocho cables que llegan al extremo del conector

### Cable UTP correctamente terminado

![this is image's alt text](https://contenthub.netacad.com/courses/itn-dl/aeece082-34fa-11eb-ad9a-f74babed41a6/af204c90-34fa-11eb-ad9a-f74babed41a6/assets/2dda7281-1c25-11ea-81a0-ffc2c49b96bc.jpg)

**Nota**: La terminación incorrecta de los cables puede afectar el rendimiento de la transmisión.

4.4.3

## Cables UTP directos y cruzados

Según las diferentes situaciones, es posible que los cables UTP necesiten armarse según las diferentes convenciones para los cableados. Esto significa que los hilos individuales del cable deben conectarse en diferente orden para distintos grupos de pins en los conectores RJ-45.

A continuación se mencionan los principales tipos de cables que se obtienen al utilizar convenciones específicas de cableado:

-   **Cable directo de Ethernet -** El tipo más común de cable de red. Por lo general, se utiliza para interconectar un host con un switch y un switch con un router.
-   **Cable cruzado Ethernet -** El cable utilizado para interconectar dispositivos similares. Por ejemplo, para conectar un switch a un switch, un host a un host o un router a un router. Sin embargo, los cables de cruce ahora se consideran heredados, ya que las NIC utilizan cruzado de interfaz dependiente medio (Auto-MDIX) para detectar automáticamente el tipo de cable y realizar la conexión interna.

**Nota**: Otro tipo de cable es un rollover, que es propiedad de Cisco. Se utiliza para conectar una estación de trabajo al puerto de consola de un router o de un switch.

Es posible que el uso de un cable de conexión cruzada o de conexión directa en forma incorrecta entre los dispositivos no dañe los dispositivos pero tampoco se producirá la conectividad y la comunicación entre los dispositivos. Este es un error común de laboratorio. Si no se logra la conectividad, la primera medida para resolver este problema es verificar que las conexiones de los dispositivos sean correctas.

La figura identifica los pares de cables individuales para los estándares T568A y T568B.

La figura muestra diagramas de los estándares de cableado T568A y T568B. Cada uno muestra el pinout correcto para los pares de cables individuales. Cada par de cables de color está numerado y consta de un cable de color sólido y un cable rayado blanco. El par 1 es azul, el par 2 es naranja, el par 3 es verde y el par 4 es marrón. Cada estándar alterna entre cables blancos rayados y sólidos. Para el estándar T568A, el par azul se termina en los pines 4 y 5, el par naranja se termina en los pines 3 y 6, el par verde se termina en los pines 1 y 2, y el par marrón se termina en los pines 7 y 8. Para el estándar T568B, el par azul se termina en los pines 4 y 5, el par naranja se termina en los pines 1 y 2, el par verde es la terminación en los pines 3 y 6, y el par marrón se termina en los pines 7 y 8.

### T568A and T568B Standards
![[Pasted image 20220920183103.png]]

### Cable Types and Standards

![[Pasted image 20220920183222.png]]