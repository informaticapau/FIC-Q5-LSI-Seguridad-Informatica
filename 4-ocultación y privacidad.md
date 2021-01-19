# Ocultación y Privacidad

## Network Address Translation

La traducción de direcciones de red, también llamado enmascaramiento de IP o NAT (del inglés _Network Address Translation_), es un mecanismo utilizado por routers IP para intercambiar paquetes entre dos redes que asignan mutuamente direcciones incompatibles. Consiste en convertir, en tiempo real, las direcciones utilizadas en los paquetes transportados. También es necesario editar los paquetes para permitir la operación de protocolos que incluyen información de direcciones dentro de la conversación del protocolo.

De todas formas el uso de NAT  no proporciona ni privacidad ni ocultación.

## Uso de proxies

### ¿Qué es un proxy?

Un **proxy**, o servidor proxy, en una red informática, es un servidor, programa o dispositivo, que hace de intermediario en las peticiones de recursos que realiza un cliente (A) a otro servidor (C). Por ejemplo, si una hipotética máquina A solicita un recurso a C, lo hará mediante una petición a B, que a su vez trasladará la petición a C; de esta forma C no sabrá que la petición procedió originalmente de A. Esta situación estratégica de punto intermedio le permite ofrecer diversas funcionalidades: control de acceso, registro del tráfico, restricción a determinados tipos de tráfico, mejora de rendimiento, anonimato de la comunicación, caché web, etc.

Hay que tener cuidado al usar proxies de fiabilidad dudosa ya que todo el tráfico va a pasar por ellos.

### Proxies transparentes, anónimos y de élite

#### Proxies transparentes

Los proxies transparentes:

- Son servidores proxy estándar que no alteran la información del usuario y la dejan en su formato original (no proporcionan ni privacidad ni anonimato).
- Revelan direcciones IP.
- Manejan todo el tráfico HTTP.
  - El usuario no necesita ajustar ninguna configuración personal.
- Permiten al usuario acelerar el acceso a los sitios web definidos por él.
  - El rendimiento aumenta al almacenar en caché el contenido.
- Suelen funcionar más rápido que los servidores proxy anónimos y de élite, ya que reducen el uso de ancho de banda ascendente.

Los empresarios aplican este tipo de proxy para restringir el acceso a recursos específicos (redes sociales, etc.).

Su principal inconveniente es el bajo nivel de anonimato. Los proxies transparentes se utilizan principalmente para:

- Aumentar los valores de los contadores.
- Descargar archivos de los servicios de alojamiento de archivos.
- Bloquear los firewalls locales.

#### Proxies anónimos

Los proxies anónimos:

- Tienen las mismas ventajas que los servidores transparentes en cuanto al almacenamiento en caché.
- Ofrecen el anonimato.
  - Ocultan la información del usuario durante la navegación web.
  - Modifican aleatoriamente una dirección IP.
    - La dirección IP resultante no se registra en ningún lugar debido a que el valor de HTTP_X_FORWARDER_FOR no se reenvía al sitio web final.

La cantidad de usuarios de proxy de anonimato está aumentando considerablemente, ya que la confidencialidad en Internet significa que su computadora está protegida contra:

- Piratería.
- Pérdida/corrupción de datos.
- Otras acciones maliciosas.

#### Proxies de élite

El uso de un proxy de élite es el grado de seguridad más avanzado:

- Proporciona la mejor protección y privacidad en Internet.
- No dejan rastros del uso de un servidor proxy.
- Los encabezados HTTP_X_FORWARDED_FOR, HTTP_PROXY_CONNECTION y HTTP_VIA no se reenvían en absoluto.
- A un host no se le comunica una dirección IP o un uso del proxy.

Los proxies de élite tienen una deficiencia: el encabezado REMOTE_ADDR guarda la dirección IP de un proxy. Por lo tanto, al reenviar paquetes de cookies almacenados desde su navegación sin un proxy de élite, los sitios web no lo identificarán. Para evitarlo: limpiar la caché y las cookies por adelantado.

### Proxies ruidosos

Ofrecen privacidad y ocultan utilizando el HTTP_X_FORWARDED_FOR para meter IPs aleatorias (ruido).

### Proxies SOCKS

Se diferencian de otros proxys por utilizar el protocolo SOCKS en vez de HTTP. El programa cliente es a la vez cliente HTTP y cliente SOCKS. El cliente negocia una conexión con el servidor proxy SOCKS usando el protocolo SOCKS de nivel 5 (capa de sesión del modelo OSI). Una vez establecida la conexión todas la comunicaciones entre el cliente y proxy se realizan usando el protocolo SOCKS. El cliente le dice al proxy SOCKS qué es lo que quiere y el proxy se comunica con el servidor web externo, obtiene los resultados y se los manda al cliente. De esta forma el servidor externo solo tiene que estar accesible desde el proxy SOCKS que es el que se va a comunicar con él.

El cliente que se comunica con SOCKS puede estar en la propia aplicación, o bien en la pila de protocolos TCP/IP a donde la aplicación enviará los paquetes a un túnel SOCKS. En el proxy SOCKS es habitual implementar, como en la mayoría de proxys, autenticación y registro de las sesiones.

En los orígenes de la web fue un protocolo de acceso a web popular, pero el rápido desarrollo de los proxies HTTP o incluso de NAT y otras opciones de aseguramiento de las comunicaciones TCP/IP lo hizo caer en desuso prácticamente absoluto llegado el siglo XXI.

### Configuración de proxies en Debian

Existen variables de entorno para configurar los proxies:

- http_proxy
- https_proxy
- ftp_proxy

Una vez asignados valores con `export` todas las peticiones del protocolo se realizarán a través de la IP asignada.

## Uso de VPN

Una VPN. Abre un tunel (normalmente en capa tres) en el que la paquetería va cifrada, proporcionando privacidad y ocultación.

## Borrado seguro

Necesario cuando se quiere evitar dejar trazas en equipos. Software de análisis forense es capaz de recuperar ficheros o sistemas de ficheros.

## Redes de anonimato

Tor
