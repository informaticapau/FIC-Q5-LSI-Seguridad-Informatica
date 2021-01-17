# CATEGORÍAS DE ATAQUES

## Ataques pasivos y activos

Un **ataque pasivo** intenta conocer o hacer uso de información del sistema, pero no afecta a los recursos del mismo. Se dan en forma de escucha o de observación no autorizada de las transmisiones. El objetivo del oponente es obtener información que se esté transmitiendo. Son muy difíciles de detectar, ya que no implican alteraciones en los datos. Contra estos ataques se debe poner más énfasis en la prevención que en la detección.

Un **ataque activo** intenta alterar los recursos del sistema o afectar a su funcionamiento. Implican alguna modificación del flujo de datos o la creación de un flujo falso. Son difíciles de prevenir por completo, el objetivo es detectarlos y recuperarse de ellos. Se pueden dividir en cuatro categorías:

- Suplantación de identidad: una entidad finge ser otra.
- Repetición: la captura pasiva de una unidad de datos y su retransmisión posterior para producir un efecto no autorizado.
- Modificación de mensajes: una parte de un mensaje es alterada, o los mensajes se han retrasado o reordenado, para producir un efecto no autorizado.
- Interrupción del servicio: impide el uso o la gestión normal de las utilidades de comunicación.

## Interceptación

El atacante escucha el flujo de datos entre el origen y el destino para robar información y conseguir acceso a recursos. Es difícil de detectar. En este tipo de ataque se incluyen: ataques contra la confidencialidad, copia y pirateo de _software_, escuchas de líneas telefónicas, _sniffing_...

## Suplantación

El atacante finge ser el origen o el destino (o ambos) del flujo de datos. Ejemplos: DNS _spoofing_, IP __spoofing_, MAC _spoofing_, _fake mails_...

## Generación o fabricación

No se interactúa con el flujo origen-destino, se inyectan entidades falsas para obtener privilegios. Es un ataque contra la autenticidad: Ejemplos: añadir transacciones falsas en red, insertar peticiones...

## Manipulación

Una entidad no autorizada accede a un recurso y lo altera. Es un ataque contra la integridad. Ejemplos: _SqlInjection_, _man in the middle_, _buffer overflow_...

## Interrupción

Se rompe el flujo entre origen y destino. Se daña, se pierde o se deja de dar una determinada funcionalidad. La detección de este tipo de ataque es inmediata. Ejemplos: cortes de líneas, robar CPU, robar RAM, inyectar ácido sulfúrico por la ranura de la tarjeta de las máquinas de la ORA...

### Ataques de denegación de servicio

Un ataque de denegación de servicio, también llamado ataque **DoS** (_Denial of Service_, es un ataque a un sistema de computadoras o red que causa que un servicio o recurso sea inaccesible a los usuarios legítimos. Normalmente provoca la pérdida de la conectividad con la red por el consumo del ancho de banda de la red de la víctima o sobrecarga de los recursos computacionales del sistema atacado.

Una ampliación del ataque DoS es el llamado ataque de denegación de servicio distribuido, también llamado **DDoS** (_Distributed Denial of Service_) el cual se lleva a cabo generando un gran flujo de información desde varios puntos de conexión hacia un mismo punto de destino. La forma más común de realizar un DDoS es a través de una red de bots, siendo esta técnica el ciberataque más usual y eficaz por su sencillez tecnológica.
