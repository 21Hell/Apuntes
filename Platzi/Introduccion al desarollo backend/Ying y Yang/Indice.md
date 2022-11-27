![[Pasted image 20221126114706.png]]
Codigo Frontend
[[Front End]]

Diseño 
	Adobe XD
	Sketck
	Figma
Ui Design
Ux Design


Backend
	JS
		Express
	Java
		Spring
	GO
	Rust
	Ruby
		Ruby on rails
	Python
		Fast API
		Flask
		Django


**[[Framework]]:**
> Conjunto de librerias, reglas y estandares para construir un producto digital
> Marco de trabajo (conseguir lo que queremos)


# Como se une frontend con backend
## API
> Application Programming Interface

### SOAP
	 Simple Objetct Access Protocol
Usando XML
Extensuible Markup language
```xml
<\?xml version="1.0" encoding="UTF-8" ?>
<note>
	<to>Tove</to>
	<from>Jani</from>
	<heading>Reminder</heading>
	<body>Don't forget me this weekend!</body>
</note>
```

### REST
	Representational State Transfer

Usando JSON
Javascript Object Notation
```json
{
	"nombre": "Juan",
	"edad": 20
}
```

## HTTP
> Hypertext Transfer Protocol
### Request
	GET       
	POST      
	PUT       
	DELETE
### Response
	200 OK
	201 Created
	400 Bad Request
	404 Not Found
	500 Internal Server Error
### Example
```
GET /api/usuarios HTTP/1.1
Host: platzi.com
Accept-Language: en-US

HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 1234
[
	{
		"nombre": "Juan",
		"edad": 20
	},
	{
		"nombre": "Pedro",
		"edad": 20
	}
]
```
