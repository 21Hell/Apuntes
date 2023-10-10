## Características del cableado de cobre

El cableado de cobre es el tipo más común de cableado utilizado en las redes hoy en día. De hecho, el cableado de cobre no es solo un tipo de cable. Hay tres tipos diferentes de cableado de cobre que se utilizan cada uno en situaciones específicas.

Las redes utilizan medios de cobre porque son económicos y fáciles de instalar, y tienen baja resistencia a la corriente eléctrica. Sin embargo, estos medios están limitados por la distancia y la interferencia de señal.

Los datos se transmiten en cables de cobre como impulsos eléctricos. Un detector en la interfaz de red de un dispositivo de destino debe recibir una señal que pueda decodificarse exitosamente para que coincida con la señal enviada. No obstante, cuanto más lejos viaja una señal, más se deteriora. Esto se denomina atenuación de señal. Por este motivo, todos los medios de cobre deben seguir limitaciones de distancia estrictas según lo especifican los estándares que los rigen.

Los valores de temporización y voltaje de los pulsos eléctricos también son vulnerables a las interferencias de dos fuentes:

-   **Interferencia electromagnética (EMI) o interferencia de radiofrecuencia (RFI)**: las señales de EMI y RFI pueden distorsionar y dañar las señales de datos que transportan los medios de cobre. Las posibles fuentes de EMI y RFI incluyen las ondas de radio y dispositivos electromagnéticos, como las luces fluorescentes o los motores eléctricos.
-   **Crosstalk** - Crosstalk se trata de una perturbación causada por los campos eléctricos o magnéticos de una señal de un hilo a la señal de un hilo adyacente. En los circuitos telefónicos, el crosstalk puede provocar que se escuche parte de otra conversación de voz de un circuito adyacente. En especial, cuando una corriente eléctrica fluye por un hilo, crea un pequeño campo magnético circular alrededor de dicho hilo, que puede captar un hilo adyacente.

En la figura, se muestra la forma en que la interferencia puede afectar la transmisión de datos.

El diagrama es de cuatro gráficos, cada uno con voltaje a lo largo del tiempo. El primer gráfico muestra ondas cuadradas de una señal digital pura y su equivalente binario, 1011001001101. El segundo gráfico es de una señal de interferencia con diversos grados de voltaje. El tercer gráfico muestra la señal digital con la interferencia. El cuarto gráfico muestra cómo el ordenador lee la señal cambiada como el equivalente binario de 1011001011101.

1.  Se transmite una señal digital pura
2.  En el medio, hay una señal de interferencia
3.  La señal digital está dañada por la señal de interferencia.
4.  El equipo receptor lee una señal cambiada. Observe que un bit 0 ahora se interpreta como un bit 1.

Para contrarrestar los efectos negativos de la EMI y la RFI, algunos tipos de cables de cobre se empaquetan con un blindaje metálico y requieren una conexión a tierra adecuada.

Para contrarrestar los efectos negativos del crosstalk, algunos tipos de cables de cobre tienen pares de hilos de circuitos opuestos trenzados que cancelan dicho tipo de interferencia en forma eficaz.

La susceptibilidad de los cables de cobre al ruido electrónico también se puede limitar utilizando estas recomendaciones:

-   La elección del tipo o la categoría de cable más adecuados a un entorno de red determinado.
-   El diseño de una infraestructura de cables para evitar las fuentes de interferencia posibles y conocidas en la estructura del edificio.
-   El uso de técnicas de cableado que incluyen el manejo y la terminación apropiados de los cables.

## Tipos de cableado de cobre

Existen tres tipos principales de medios de cobre que se utilizan en las redes.

La figura se compone de imágenes que muestran los tres tipos de cableado de cobre, cada uno con una parte de la cubierta del cable exterior despojada para exponer la construcción del cable. La primera imagen muestra un cable de par trenzado sin blindaje (UTP) con cuatro pares de colores de cables trenzados: azul, naranja, verde y marrón. La segunda imagen es un cable de par trenzado blindado (STP) que muestra cuatro pares de cables trenzados - azul, verde, marrón y naranja - con un escudo de aluminio que rodea a los cuatro pares. La última imagen muestra un conductor de cobre central rodeado de aislamiento plástico rodeado por un escudo trenzado.

![this is the image’s alt text](https://contenthub.netacad.com/courses/itn-dl/aeece082-34fa-11eb-ad9a-f74babed41a6/af202582-34fa-11eb-ad9a-f74babed41a6/assets/2dd80184-1c25-11ea-81a0-ffc2c49b96bc.png)![this is the image’s alt text](https://contenthub.netacad.com/courses/itn-dl/aeece082-34fa-11eb-ad9a-f74babed41a6/af202582-34fa-11eb-ad9a-f74babed41a6/assets/2dd82890-1c25-11ea-81a0-ffc2c49b96bc.png)![The image shows a copper cable with the protective jacket cut away, thus exposing a copper core surrounded by insulation that is surrounded by the braided metal shielding.](https://contenthub.netacad.com/courses/itn-dl/aeece082-34fa-11eb-ad9a-f74babed41a6/af202582-34fa-11eb-ad9a-f74babed41a6/assets/2dd82891-1c25-11ea-81a0-ffc2c49b96bc.png)

Cable de par trenzado no blindado (UTP)Cable de par trenzado blindado (STP)Cable coaxial

## Par trenzado no blindado (UTP)

El cableado de par trenzado no blindado (UTP) es el medio de red más común. El cableado UTP, que se termina con conectores RJ-45, se utiliza para interconectar hosts de red con dispositivos intermediarios de red, como switches y routers.

En las redes LAN, el cable UTP consta de cuatro pares de hilos codificados por colores que están trenzados entre sí y recubiertos con un revestimiento de plástico flexible que los protege contra daños físicos menores. El trenzado de los hilos ayuda a proteger contra las interferencias de señales de otros hilos.

Como se muestra en la figura, los códigos por colores identifican los pares individuales con sus alambres y sirven de ayuda para la terminación de cables.

Cable UTP que muestra la cubierta del cable exterior (etiquetado 1), los pares de cables trenzados (etiquetado 2) y el aislamiento naranja, verde, azul y marrón (etiquetado 3)

![](https://contenthub.netacad.com/courses/itn-dl/aeece082-34fa-11eb-ad9a-f74babed41a6/af202582-34fa-11eb-ad9a-f74babed41a6/assets/2dd84fa3-1c25-11ea-81a0-ffc2c49b96bc.jpg)

Los números en la figura identifican algunas características clave del cable de par trenzado sin blindaje:

1.  La cubierta exterior protege los cables de cobre del daño físico.
2.  Los pares trenzados protegen la señal de interferencia.
3.  El aislamiento de plástico codificado por colores aísla eléctricamente los cables entre sí e identifica cada par.

## Par trenzado blindado (STP)

El par trenzado blindado (STP) proporciona una mejor protección contra ruido que el cableado UTP. Sin embargo, en comparación con el cable UTP, el cable STP es mucho más costoso y difícil de instalar. Al igual que el cable UTP, el STP utiliza un conector RJ-45.

El cable STP combina las técnicas de blindaje para contrarrestar la EMI y la RFI, y el trenzado de hilos para contrarrestar el crosstalk. Para obtener los máximos beneficios del blindaje, los cables STP se terminan con conectores de datos STP blindados especiales. Si el cable no se conecta a tierra correctamente, el blindaje puede actuar como antena y captar señales no deseadas.

El cable STP que se muestra utiliza cuatro pares de hilos. Cada uno de estos pares está empaquetado primero con un blindaje de hoja metálica y, luego, el conjunto se empaqueta con una malla tejida o una hoja metálica.

Cable STP que muestra la cubierta del cable exterior (etiquetado 1), un blindaje trenzado alrededor de todos los pares de cables (etiquetado 2), escudos de lámina alrededor de los pares de cables individuales (etiquetado 3) y los pares de cables trenzados de colores (etiquetado 4)

![](https://contenthub.netacad.com/courses/itn-dl/aeece082-34fa-11eb-ad9a-f74babed41a6/af202582-34fa-11eb-ad9a-f74babed41a6/assets/2dd89dc2-1c25-11ea-81a0-ffc2c49b96bc.jpg)

Los números en la figura identifican algunas características clave del cable de par trenzado blindado:

1.  Cubierta exterior
2.  Escudo trenzado o de aluminio
3.  Escudos de aluminio
4.  Pares trenzados

## Cable coaxial

El cable coaxial obtiene su nombre del hecho de que hay dos conductores que comparten el mismo eje. Como se muestra en la figura, el cable coaxial consta de lo siguiente:

-   Se utiliza un conductor de cobre para transmitir las señales electrónicas.
-   Una capa de aislamiento plástico flexible que rodea al conductor de cobre.
-   Sobre este material aislante, hay una malla de cobre tejida o una hoja metálica que actúa como segundo hilo en el circuito y como blindaje para el conductor interno. La segunda capa o blindaje reduce la cantidad de interferencia electromagnética externa.
-   La totalidad del cable está cubierta por un revestimiento para evitar daños físicos menores.

Existen diferentes tipos de conectores con cable coaxial. Los conectores Bayoneta Neill—Concelman (BNC), tipo N y tipo F se muestran en la figura.

Aunque el cable UTP ha reemplazado esencialmente el cable coaxial en las instalaciones de Ethernet modernas, el diseño del cable coaxial se usa en las siguientes situaciones:

-   **Instalaciones inalámbricas** - Los cables coaxiales conectan antenas a los dispositivos inalámbricos. También transportan energía de radiofrecuencia (RF) entre las antenas y el equipo de radio.
-   **Instalaciones de Internet por cable** - Los proveedores de servicios de cable proporcionan conectividad a Internet a sus clientes mediante el reemplazo de porciones del cable coaxial y la admisión de elementos de amplificación con cables de fibra óptica. Sin embargo, el cableado en las instalaciones del cliente sigue siendo cable coaxial.

tres figuras que muestran la construcción de un cable coaxial, una sección transversal de un cable coaxial y tres tipos de conectores de cable coaxial

![this is the image’s alt text](https://contenthub.netacad.com/courses/itn-dl/aeece082-34fa-11eb-ad9a-f74babed41a6/af202582-34fa-11eb-ad9a-f74babed41a6/assets/2dd8c4d3-1c25-11ea-81a0-ffc2c49b96bc.jpg)

Conectores coaxialesTipo FTipo NBNC

Los números en la figura identifican algunas características clave del cable coaxial:

1.  Cubierta exterior
2.  Blindaje de cobre trenzado
3.  Aislamiento plástico
4.  Conductor de cobre