from flask import Flask, render_template, request
from services.aula_service import obtener_aulas

app = Flask(__name__)


@app.route("/")
def inicio():
    try:
        aulas = obtener_aulas()

        return render_template(
            "index.html",
            aulas=aulas
        )

    except Exception as e:

        return render_template(
            "resultado.html",
            mensaje=f"Error cargando las aulas: {str(e)}",
            tipo="danger"
        )


@app.route("/reservar", methods=["POST"])
def reservar():

    try:

        aula_id = int(request.form["aula_id"])
        asistentes = int(request.form["asistentes"])

        aulas = obtener_aulas()

        for aula in aulas:

            if aula["id"] == aula_id:

                # Regla de negocio 1
                if aula["estado"] != "Disponible":

                    return render_template(
                        "resultado.html",
                        mensaje="Esta sala está inhabilitada.",
                        tipo="warning"
                    )

                # Regla de negocio 2
                if asistentes > aula["capacidad"]:

                    return render_template(
                        "resultado.html",
                        mensaje=f"Capacidad excedida. Máximo permitido: {aula['capacidad']}",
                        tipo="danger"
                    )

                return render_template(
                    "resultado.html",
                    mensaje=f"Reserva realizada correctamente para {aula['nombre']}",
                    tipo="success"
                )

        return render_template(
            "resultado.html",
            mensaje="Aula no encontrada.",
            tipo="danger"
        )

    except ValueError:

        return render_template(
            "resultado.html",
            mensaje="Los datos ingresados no son válidos.",
            tipo="danger"
        )

    except KeyError:

        return render_template(
            "resultado.html",
            mensaje="Faltan campos obligatorios en el formulario.",
            tipo="danger"
        )

    except Exception as e:

        return render_template(
            "resultado.html",
            mensaje=f"Error inesperado: {str(e)}",
            tipo="danger"
        )


@app.errorhandler(404)
def pagina_no_encontrada(error):

    return render_template(
        "resultado.html",
        mensaje="Página no encontrada.",
        tipo="warning"
    ), 404


@app.errorhandler(500)
def error_servidor(error):

    return render_template(
        "resultado.html",
        mensaje="Error interno del servidor.",
        tipo="danger"
    ), 500


if __name__ == "__main__":
    app.run(debug=True)