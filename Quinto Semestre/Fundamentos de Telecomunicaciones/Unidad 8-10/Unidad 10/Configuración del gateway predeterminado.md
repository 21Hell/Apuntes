## Gateway predeterminado para un host

Si su red local sólo tiene un enrutador, será el enrutador de puerta de enlace y todos los hosts y conmutadores de su red deben estar configurados con esta información. Si la red local tiene varios enrutadores, debe seleccionar uno de ellos para que sea el enrutador de puerta de enlace predeterminado. En este tema se explica cómo configurar la puerta de enlace predeterminada en hosts y conmutadores.

Para que un terminal se comunique a través de la red, se debe configurar con la información de dirección IP correcta, incluida la dirección de gateway predeterminado. El gateway predeterminado se usa solamente cuando el host desea enviar un paquete a un dispositivo de otra red. En general, la dirección de gateway predeterminado es la dirección de la interfaz de router conectada a la red local del host. La dirección IP del dispositivo host y la dirección de interfaz de router deben estar en la misma red.

Por ejemplo, supongamos que una topología de red IPv4 consiste en un enrutador que interconecta dos LAN independientes. G0/0 está conecta a la red 192.168.10.0, mientras que G0/1 está conectada a la red 192.168.11.0. Cada dispositivo host está configurado con la dirección de gateway predeterminado apropiada.

En este ejemplo, si PC1 envía un paquete a PC2, no se utiliza la puerta de enlace predeterminada. En cambio, PC1 dirige el paquete con la dirección IPv4 de PC2 y lo reenvía directamente a PC2 a través del switch.

![[Pasted image 20221004181718.png]]

¿Qué pasa si PC1 envió un paquete a PC3? PC1 dirigiría el paquete con la dirección IPv4 de PC3, pero reenviaría el paquete a su puerta de enlace predeterminada, que es la interfaz G0/0/0 de R1. El router acepta el paquete, accede a su tabla de routing para determinar la interfaz de salida apropiada según la dirección de destino. R1 reenvía el paquete fuera de la interfaz apropiada para llegar a PC3.


![[Pasted image 20221004181732.png]]

El mismo proceso ocurriría en una red IPv6, aunque esto no se muestra en la topología. Los dispositivos usarían la dirección IPv6 del enrutador local como puerta de enlace predeterminada.

## Gateway predeterminado para un switch

Por lo general, un switch de grupo de trabajo que interconecta equipos cliente es un dispositivo de capa 2. Como tal, un switch de capa 2 no necesita una dirección IP para funcionar adecuadamente. Sin embargo, se puede configurar una configuración IP en un conmutador para dar a un administrador acceso remoto al conmutador.

Para conectarse y administrar un switch a través de una red IP local, debe tener configurada una interfaz virtual de switch (SVI). El SVI se configura con una dirección IPv4 y una máscara de subred en la LAN local. El conmutador también debe tener una dirección de puerta de enlace predeterminada configurada para administrar el conmutador de forma remota desde otra red.

Por lo general, la dirección del gateway predeterminado se configura en todos los dispositivos que desean comunicarse más allá de la red local.

Para configurar un gateway predeterminado en un switch, use el comando de configuración global **ip default-gateway** ip default-gateway. La dirección IP que se configura es la dirección IPv4 de la interfaz del enrutador local conectada al switch


![[Pasted image 20221004181803.png]]

En este ejemplo, el host administrador usaría su puerta de enlace predeterminada para enviar el paquete a la interfaz G0/0/1 de R1. R1 reenviaría el paquete a S1 desde su interfaz G0/0/0. Dado que la dirección IPv4 de origen del paquete provenía de otra red, S1 requeriría una puerta de enlace predeterminada para reenviar el paquete a la interfaz G0/0/0 de R1. Por lo tanto, el switch S1 se debe configurar con un gateway predeterminado, para que pueda responder y establecer una conexión SSH con el host administrativo.

**Nota:** Los paquetes que se originan en servidores conectados al switch ya deben crearse con la dirección de gateway predeterminado configurada en el sistema operativo de su servidor.

Un conmutador de grupo de trabajo también se puede configurar con una dirección IPv6 en un SVI. Sin embargo, el conmutador no requiere que la dirección IPv6 de la puerta de enlace predeterminada se configure manualmente. El conmutador recibirá automáticamente su puerta de enlace predeterminada del mensaje ICMPv6 Router Advertisement del router.

