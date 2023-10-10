## conexión Fisica
[[red cableada]]. Los datos se transmiten a través de un cable 

Los dispositivos en una [[red inalámbrica]] deben estar conectados a un punto de acceso inalámbrico (AP) o router inalámbrico
### Router inalámbrico
1.  Las antenas inalámbricas (Estas están integradas dentro de la versión del router que se muestra en la figura anterior).
2.  Varios puertos de switch de Ethernet
3.  Un puerto de internet

tarjetas de interfaz de red (NIC) conectan un dispositivo a la red. Las NIC de Ethernet se usan para una conexión por cable

mientras que las NIC de la red de área local inalámbrica (WLAN) se usan para la conexión inalámbrica.

Los dispositivos para usuarios finales pueden incluir *un tipo de NIC o ambos*

EJ:
Una impresora de red, por ejemplo, puede contar solo con una NIC Ethernet y, por lo tanto, se debe conectar a la red mediante un cable Ethernet. Otros dispositivos, como las tabletas y los teléfono inteligentes, pueden contener solo una NIC WLAN y deben utilizar una conexión inalámbrica


## La capa física

La capa física de OSI proporciona los **medios de transporte de los bits** que conforman una trama de la capa de enlace de datos a través de los medios de red. Esta capa acepta una trama completa desde la capa de enlace de datos y la codifica como una secuencia de señales que se transmiten en los medios locales. Un dispositivo final o un dispositivo intermediario recibe los bits codificados que componen una *trama*.

La **capa física del nodo de destino recupera estas señales individuales de los medios**, las restaura a sus representaciones en bits y pasa los bits a la capa de enlace de datos en forma de trama completa
![[Pasted image 20220920173314.png]]

![[Pasted image 20220920173504.png]]