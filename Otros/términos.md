# TÉRMINOS

## Seguridad de la Información y Seguridad Informática

- Seguridad Informática: Grupo de herramientas diseñadas para
proteger los datos y evitar la intrusión de los hackers.
- Seguridad de la Información: Todas aquellas medidas preventivas y reactivas del hombre, de las organizaciones y de los sistemas tecnológicos que permitan resguardar y proteger la información buscando mantener la tríada CIA.

### La tríada CIA

La Seguridad de la Información ha declarado que la confidencialidad, integridad y disponibilidad (conocida como la Tríada CIA, del inglés: "_Confidentiality_, _Integrity_, _Availability_") son los principios básicos de la seguridad de la información.

- Confidencialidad: Asegurar el acceso a la información únicamente a aquellas personas que cuenten con la debida autorización.
- Integridad: Mantener con exactitud la información tal cual fue generada, sin ser manipulada ni alterada por personas o procesos no autorizados.
- Disponibilidad: Acceder a la información y a los sistemas por personas autorizadas en el momento que así lo requieran.

## Detección de intrusiones

- IDS (_Intrusion Detection System_): Sistema de detección de intrusiones. Trata de detectar posibles ataques y los notifica.
- IPS (_Intrusion Prevention System_): Sistema de prevención de intrusiones. Trata de detectar posibles ataques, los notifica y actúa contra ellos.
- Sensor: Agente que procesa la información de una red.

## Registros DNS

Los registros DNS individuales tienen efecto en el funcionamiento de los servicios del dominio. Determinan qué se debe mostrar, cuando el nombre del dominio es introducido en la barra de direcciones del navegador de internet y también definen donde deben ser entregados los correos electrónicos.

[Tipos](https://es.wikipedia.org/wiki/Anexo:Tipos_de_registros_DNS):

- A: Devuelve una dirección IPv4 de 32 bits, la más utilizada para asignar nombres de host a una dirección IP del host
- AAAA: Devuelve una dirección IPv6 de 128 bits, la más utilizada para asignar nombres de host a una dirección IP del host.
- CNAME: Alias de un nombre a otro: la búsqueda de DNS continuará reintentando la búsqueda con el nuevo nombre.
- MX: Contiene el nombre del servidor de e-mail. Define donde se tienen que entregar los correos electrónicos.
- NS: Asocia un dominio a un servidor DNS.
- PTR: Registros de resolución inversa.
- SOA: Especifica información sobre el DNS primario de la zona.

## _Payloads_ (Metasploit)

Módulo de un _exploit_ que al ejecutarse permite hacer determinadas cosas:

- _Singles_: Únicos y completamente independientes. Pueden ser algo tan simple como agregar un usuario al sistema de destino o ejecutar un programa. Son autónomos, por lo que pueden ser usados sin manejadores de _payload_.
- _Stagers_: Configuran una conexión de red entre el atacante y la víctima y están diseñados para ser pequeños y confiables.
- _Stages_: Componentes de los payloads, que se descargan por los módulos Stagers. Las diversas variedades de payloads proporcionan funciones avanzadas sin límites de tamaño

## Otros términos

- CPE (_Common Platform Enumeration_): Una lista donde se registran las plataformas (tecnologías, software, paquetes…).

- DMZ (_DeMilitarized Zone_): En seguridad informática, una zona desmilitarizada o red perimetral es una red local que se ubica entre la red interna de una organización y una red externa, generalmente en Internet. Su objetivo es que las conexiones desde la red interna y la externa a la DMZ estén permitidas, mientras que las conexiones desde la DMZ solo se permitan a la red externa. Esto permite que los equipos de la DMZ puedan dar servicios a la red externa a la vez que protegen la red interna.

- Firewall de aplicaciones web (WAF: _Web application firewall_): Es un tipo de firewall que supervisa, filtra o bloquea el tráfico HTTP hacia y desde una aplicación web. Se diferencia de un firewall normal en que puede filtrar el contenido de aplicaciones web específicas, mientras que un firewall de red protege el tráfico entre los servidores. Al inspeccionar el tráfico HTTP un WAF protege a las aplicaciones web contra ataques como los de inyección SQL, XSS y falsificación de petición de sitios cruzados (CSRF).

- Firma digital: Mecanismo criptográfico que permite al receptor de un mensaje firmado digitalmente identificar a la entidad originadora de dicho mensaje (autenticación de origen y no repudio), y confirmar que el mensaje no ha sido alterado desde que fue firmado por el originador (integridad).

- PKI (_Public Key Infrastructure_): Combinación de hardware, software, y políticas y procedimientos de seguridad, que permiten la ejecución con garantías de operaciones criptográficas, como el cifrado, la firma digital, y el no repudio de transacciones electrónicas. Permite a los usuarios autenticarse frente a otros usuarios y usar la información de los certificados de identidad para cifrar y descifrar mensajes, firmar digitalmente información, garantizar el no repudio de un envío, y otros usos.

- Punto neutro o punto de intercambio de Internet (IXP, _Internet Exchange Point_): Infraestructura física a través de la cual los proveedores de servicios de Internet intercambian el tráfico de Internet entre sus redes.

- RDSI (red digital de servicios integrados): Red que procede por evolución de la Red Digital Integrada (RDI) y que facilita conexiones digitales extremo a extremo para proporcionar una amplia gama de servicios, tanto de voz como de otros tipos, y a la que los usuarios acceden a través de un conjunto de interfaces normalizados.

- VPN (_Virtual Private Network_): Tecnología de red que se utiliza para conectar una o más computadoras a una red privada utilizando Internet.

- Y2K (efecto 2000): Error de software causado por la costumbre que habían adoptado los programadores de omitir la centuria en el año para el almacenamiento de fechas (generalmente para economizar memoria), asumiendo que el software solo funcionaría durante los años cuyos números comenzaran con 19XX.

## Observatorio

Pentesting
IP SPOOFING
RSA
DIFFIE HELLMAN