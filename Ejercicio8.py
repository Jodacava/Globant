from flask import Flask, Blueprint, jsonify, request
from Ejercicio2 import Employee


def webapi():
    try:
        state = "200"
        message = "ok"
        listemployee = []
        app = Flask(__name__)

        @app.route("/")
        def hello():
            message = "Bienvenido al sistema de control de empleados"
            return message

        @app.route("/crud/create", methods=['POST'])
        def createemp():
            try:
                values = request.get_json()
                emp = Employee.create(values["code"], values["name"], values["lastname"], values["address"], values["age"], values["start_date"], values["salary"], values["position"], values["department"])
                listemployee.append(emp)
                state = "200"
                message = "Empleado creado exitosamente."
            except Exception as ex:
                state = "400"
                message = "Empleado NO creado. Error: " + str(ex)

            data = [{"State": state, "Message": message}]
            return jsonify(data), state

        @app.route("/crud/delete", methods=['DELETE'])
        def delemp():
            ansok = False
            try:
                values = request.get_json()
                if "code" in values:
                    for emp in listemployee:
                        if emp["code"] == values["code"]:
                            listemployee.remove(emp)
                            ansok = True
                            break
                elif "name" in values:
                    for emp in listemployee:
                        if emp["name"] == values["name"]:
                            listemployee.remove(emp)
                            ansok = True
                            break
                if ansok:
                    state = "200"
                    message = "Empleado borrado exitosamente"
                else:
                    state = "400"
                    message = "Empleado NO borrado. Error: Empleado no encontrado"
            except Exception as ex:
                state = "400"
                message = "Empleado NO borrado. Error: " + str(ex)
            data = [{"State": state, "Message": message}]
            return jsonify(data), state

        if __name__ == "__main__":
            app.run(host="localhost", port=8082, debug=True)
    except Exception as ex:
        print(str(ex))

webapi()