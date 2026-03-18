import flet as ft

class SistemaVentas:
    def __init__(self):
        self.productos = []

    def main(self, page: ft.Page):
        page.title = "Sistema de Ventas"
        page.snack_bar = ft.SnackBar(ft.Text(""))

        nombre = ft.TextField(label="Nombre del producto")
        precio = ft.TextField(label="Precio", keyboard_type="number")
        cantidad = ft.TextField(label="Cantidad", keyboard_type="number") 
        mensaje = ft.Text("")

        lista = ft.Column()

        def mostrar_mensaje(texto):
                page.snack_bar = ft.SnackBar(ft.Text(texto))
                page.snack_bar.open = True
                page.update()
                #print("CLICK FUNCION AGREGAR")#
            
        def agregar(e):
                #print("Entro AGREGAR")#
                if not nombre.value or not precio.value or not cantidad.value:
                    mensaje.value = "⚠️ Todos los campos son obligatorios"
                    page.update()
                    return

                try:
                    precio_valor = float(precio.value)
                    cantidad_valor = int(cantidad.value)
                except:
                    mensaje.value = "❌ Precio y cantidad deben ser números"
                    page.update()
                    return
                print("TODO OK")
                producto = {
                    "nombre": nombre.value,
                    "precio": precio_valor,
                    "cantidad": cantidad_valor
                }

                self.productos.append(producto)

                lista.controls.append(
                    ft.Text(f"{producto['nombre']} - ${producto['precio']} | Stock: {producto['cantidad']}")
                )

                nombre.value = ""
                precio.value = ""
                cantidad.value = ""

                mensaje.value = ("✅ Producto agregado")

                page.update()

        page.add(
                ft.Text("📦 Productos", size=20),
                nombre,
                precio,
                cantidad,
                ft.ElevatedButton("Agregar", on_click=agregar),
                mensaje,
                ft.Divider(),
                ft.Text("Lista"),
                lista
        )

app = SistemaVentas()
ft.app(target=app.main)