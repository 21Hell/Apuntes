## Pasos básicos en la configuración de un router

Las siguientes tareas deben completarse al configurar la configuración inicial en un enrutador.

![[Pasted image 20221004180800.png]]


## Configuración básica de un router


![[Pasted image 20221004180837.png]]


Para configurar el nombre del dispositivo para R1, utilice los siguientes comandos .

![[Pasted image 20221004180901.png]]

**Nota:** Observe cómo el indicador del enrutador muestra ahora el nombre de host del enrutador.

Todo el acceso al router debe estar asegurado. El modo EXEC privilegiado proporciona al usuario acceso completo al dispositivo y su configuración. Por lo tanto, es el modo más importante para asegurar.

Los siguientes comandos aseguran el modo EXEC privilegiado y el modo EXEC de usuario, habilitan el acceso remoto Telnet y SSH y cifran todas las contraseñas de texto sin formato (es decir, EXEC de usuario y línea VTY).
![[Pasted image 20221004180917.png]]
La notificación legal advierte a los usuarios que solo deben acceder al dispositivo los usuarios permitidos. La notificación legal se configura de la siguiente manera.
![[Pasted image 20221004180954.png]]
Si se configuraron los comandos anteriores y el router perdió energía accidentalmente, se perderían todos los comandos configurados. Por esta razón, es importante guardar la configuración cuando se implementen los cambios. Los sigueintes comandos guardan la configuración en ejecución en la NVRAM.

![[Pasted image 20221004181008.png]]
