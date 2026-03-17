import flet as ft

class SistemaVentas:
    def __init__(self):
        self.productos = []

    def main(self, page: ft.Page):
        page.title = "Sistema de Ventas"

        nombre = ft.TextField(label="Nombre del producto")
        precio = ft.TextField(label="Precio", keyboard_type="number")

        lista = ft.Column()

        def agregar(e):
            if nombre.value and precio.value:
                producto = {
                    "nombre": nombre.value,
                    "precio": float(precio.value)
                }
                self.productos.append(producto)

                lista.controls.append(
                    ft.Text(f"{producto['nombre']} - ${producto['precio']}")
                )

                nombre.value = ""
                precio.value = ""

                page.update()

        page.add(
            ft.Text("📦 Productos", size=20),
            nombre,
            precio,
            ft.ElevatedButton("Agregar", on_click=agregar),
            ft.Divider(),
            ft.Text("Lista"),
            lista
        )

app = SistemaVentas()
ft.app(target=app.main)