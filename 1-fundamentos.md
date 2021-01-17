# FUNDAMENTOS

## Distinción entre Seguridad de la Información y Seguridad Informática

La seguridad de la información es un concepto más amplio que el de la seguridad informática: seguridad informática, ausencia de normas, errores, temas de ciberdelincuencia, metodologías, comportamientos de personal…

La seguridad informática trata de: malware, tipos de ataques, vulnerabilidades, contraseñas, denegación de servicios, configuración de firewalls y sensores de red…

La seguridad informática está incluída dentro de la seguridad de la información.

## Distinción entre vulnerabilidad, amenaza y ataque

Una vulnerabilidad es una debilidad. Puede ser una debilidad de un activo (tanto _hardware_ como _software_), una debilidad de control de acceso, falta de métodos de respuesta contra incidentes...

## Vulnerabilidades

Una vulnerabilidad es una debilidad de un activo o control que puede ser explotada por una amenaza.

### CVE (_Common Vulnerabiities and Exposures_)

[CVE] es una lista de entradas, cada una con un número de identificación, una descripción y al menos una referencia pública, para vulnerabilidades de seguridad cibernética conocidas públicamente.

Las entradas [CVE] se utilizan en numerosos productos y servicios de ciberseguridad de todo el mundo, incluida la base de datos nacional de vulnerabilidades ([NVD]) de EEUU.

Para cada vulnerabilidad, el [CVE] tiene: un identificador numérico (CVE-ID), una descripción, y al menos una referencia pública.

### CVSS (_Common Vulnerability Scoring System_)

Índice que muestra el grado de agresividad de una vulnerabilidad. Cerca del 0 tienen menos gravedad, y cerca del 10 son más críticas.

||CVSS v2.0 Ratings|CVSS v3.0 Ratings
|:--|:--:|:--:|
Severity|Base Score Range|Base Score Range
None||0.0|
Low|0.0-3.9|0.1-3.9
Medium|4.0-6.9|4.0-6.9
High|7.0-10.0|7.0-8.9
Critical||9.0-10.0

### CWE (_Common Weakness Enumeration_)

Clasificación de clases de vulnerabilidades de forma que están asociadas según su tipología.

### OVAL (_Open Vulnerability and Assessment Language_)

[OVAL] es un esfuerzo de la comunidad de seguridad de la información para estandarizar cómo evaluar e informar sobre el estado de la máquina de los sistemas informáticos. [OVAL] incluye un lenguaje para codificar los detalles del sistema y una variedad de repositorios de contenido en toda la comunidad.

Las herramientas y los servicios que utilizan [OVAL] para los tres pasos de la evaluación del sistema (representar información del sistema, expresar estados específicos de la máquina e informar los resultados de una evaluación) brindan a las empresas información precisa, consistente y procesable para que puedan mejorar su seguridad. El uso de [OVAL] también proporciona métricas de garantía de información confiables y reproducibles y permite la interoperabilidad y la automatización entre las herramientas y los servicios de seguridad.

### NVD (_National Vulnerability Database_)

La [NVD] es el repositorio del gobierno de EEUU de datos de gestión de vulnerabilidades basados ​​en estándares representados mediante el protocolo SCAP. Estos datos permiten la automatización de la gestión de vulnerabilidades, la medición de la seguridad y la conformidad.

La [NVD] incluye bases de datos de referencias de listas de verificación de seguridad, fallas de software relacionadas con la seguridad, configuraciones incorrectas, nombres de productos y métricas de impacto.

### _Zero day_

Vulnerabilidades no registradas, sin parches ni protección. Son las más críticas al no haber información ni forma de protegerse de ellas.

## Amenazas

Una amenaza es una posibilidad de violación de la seguridad, que existe cuando se da una circunstancia, capacidad, acción o evento que pudiera romper la seguridad y causar perjuicio, es decir, un peligro posible que podría explotar una vulnerabilidad.

## Ataques

Un asalto a la seguridad del sistema, derivado de una amenaza inteligente; es decir, un acto inteligente y deliberado (especialmente en el sentido de método o técnica) para eludir los servicios de seguridad y violar la política de seguridad de un sistema.

<!--Enlaces-->
[CVE]: https://cve.mitre.org/index.html
[NVD]: https://nvd.nist.gov/
[OVAL]: http://oval.mitre.org/
