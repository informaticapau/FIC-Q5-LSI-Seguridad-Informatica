output = "lsi.md"
parts = [
"0-title.md",
"1-fundamentos.md",
"2-categorías de ataque.md",

"algoritmos.md",
"protocolos.md",
"términos.md",
]
counter = 0

print(f"Creando \"{output}\"...")
with open(output, 'w', encoding="utf8") as o:
    print(f"Se ha creado \"{output}\".\n")
    for part in parts:
        try:
            print(f"Abriendo \"{part}\"...")
            with open(part, 'r', encoding="utf8") as i:
                count = 0

                #print("Escribiendo comentario...")
                #count += o.write(f"<!-- {part} -->\n")

                print(f"Copiando contenido de \"{part}\"...")
                count += o.write(i.read())

                print("Insertando separador...")
                count += o.write("\n\n---\n")

                print(f"Se han escrito {count} bytes de \"{part}\".")
                counter += count
        except:
            print(f"HA OCURRIDO UN ERROR AL COPIAR \"{part}\"")
        finally:
            print('\n')
print(f"Se ha cerrado \"{output}\"")
print(f"Bytes escritos: {counter}")