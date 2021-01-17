# SERVICIOS Y MECANISMOS DE SEGURIDAD

## Servicios de seguridad

Servicios de procesamiento o de comunicación proporcionados por un sistema para dar un tipo especial de protección a los recursos del sistema; los servicios de seguridad implementan políticas de seguridad y son implementados, a su vez, por mecanismos de seguridad.

- **Autenticación** (_Authentication_): Garantizar que alguien es quien dice ser (login/password, huella dactilar, certificado digital...).
- **Control de acceso** (_Access Control_): Evitar el acceso no autorizado a un recurso (ACLs...).
- **Confidencialidad de los datos** (_Data confidentiality_): Proteger los datos y su flujo de tráfico de su revelación no autorizada (cifrado...).
- **Integridad de los datos** (_Data integrity_): Garantizar que los mensajes se reciben tal y como son enviados: sin duplicación, inserción, modificación, reordenación ni destrucción (hash, firma digital...).
- **No repudio** (_Non-repudiation_): Evitar que emisor o receptor nieguen la transmisión o la recepción de un mensaje, respectivamente (firma digital, notarización...).
- **Disponibilidad** (_Availability_): Evitar que se interrumpa el servicio (duplicación de servicios, discos en RAID, fuentes de alimentación redundantes, servidores en clúster...).

### Servicios vs ataques

|Ataque|Tipo|Autenticación|Control de acceso|Confidencialidad|Integridad|No repudio|Disponibilidad|
|:-----|:---|:-----------:|:---------------:|:--------------:|:--------:|:--------:|:------------:|
|Obtención del contenido|Pasivo|||✔️||||
|Análisis de tráfico|Pasivo|||✔️||||
|Suplantación|Activo|✔️|✔️|||||
|Repetición|Activo||||✔️|||
|Modificación|Activo||||✔️|||
|Interrupción|Activo||||||✔️|
&nbsp;

## Mecanismos de seguridad

Característica diseñada para detectar, prevenir o recuperarse de un ataque. No hay un único mecanismo que soporte todos los servicios de seguridad requeridos, sin embargo, hay un elemento que es común a muchos de los mecanismos: las técnicas criptográficas.

### Generales

No son específicos de ninguna capa de protocolo o sistema de seguridad OSI en particular):

- Funcionalidad fiable
- Etiquetas de seguridad
- Detección de acciones
- Informe para la auditoría de seguridad
- Recuperación de la seguridad

### Específicos

Pueden ser incorporados en la capa de protocolo adecuada:

- Cifrado
- Firma digital
- Control de acceso
- Integridad de los datos
- Intercambio de autenticación
- Relleno del tráfico
- Control de enrutamiento
- Notarización

### Servicios vs mecanismos

|Mecanismo|Autenticación|Control de acceso|Confidencialidad|Integridad|No repudio|Disponibilidad|
|:--------|:-----------:|:---------------:|:--------------:|:--------:|:--------:|:------------:|
|Cifrado|✔️||✔️|✔️|||
|Firma digital|✔️|||✔️|✔️||
|Control de acceso||✔️|||||
|Integridad de datos||||✔️|✔️|✔️|
|Intercambio de autenticación|✔️|||||✔️|
|Relleno de tráfico|||✔️||||
|Control de enrutamiento|||✔️||||
|Notarización|||||✔️||
&nbsp;
