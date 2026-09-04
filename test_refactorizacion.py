import pytest

from refactorizacion import (
    cargar_config,
    estadisticas,
    operaciones,
    procesar_items,
    usuarios_mayores,
)


class TestOperaciones:
    def test_suma(self):
        assert operaciones(2, 3, "suma") == 5

    def test_resta(self):
        assert operaciones(10, 4, "resta") == 6

    def test_multiplicacion(self):
        assert operaciones(3, 7, "multi") == 21

    def test_division(self):
        assert operaciones(10, 4, "divi") == 2.5

    def test_division_entera_exacta(self):
        assert operaciones(9, 3, "divi") == 3.0

    def test_operacion_desconocida_devuelve_none(self):
        assert operaciones(1, 2, "potencia") is None
        assert operaciones(1, 2, "") is None
        assert operaciones(1, 2, None) is None

    def test_suma_con_negativos_y_cero(self):
        assert operaciones(-5, 2, "suma") == -3
        assert operaciones(0, 0, "suma") == 0

    def test_resta_resultado_negativo(self):
        assert operaciones(3, 10, "resta") == -7

    def test_multiplicacion_por_cero(self):
        assert operaciones(8, 0, "multi") == 0

    def test_division_por_cero_devuelve_error(self):
        assert operaciones(5, 0, "divi") == "error"

    def test_division_de_cero(self):
        assert operaciones(0, 5, "divi") == 0.0

    def test_numeros_flotantes(self):
        assert operaciones(1.5, 2.5, "suma") == 4.0
        assert operaciones(5.0, 2.0, "divi") == 2.5


class TestUsuariosMayores:
    def test_filtra_mayores_de_edad(self):
        usuarios = [
            {"nombre": "Ana", "edad": 20},
            {"nombre": "Luis", "edad": 17},
            {"nombre": "Marta", "edad": 18},
        ]
        assert usuarios_mayores(usuarios) == ["Ana", "Marta"]

    def test_lista_vacia(self):
        assert usuarios_mayores([]) == []

    def test_ninguno_es_mayor(self):
        usuarios = [
            {"nombre": "Paco", "edad": 10},
            {"nombre": "Eva", "edad": 0},
        ]
        assert usuarios_mayores(usuarios) == []

    def test_todos_son_mayores(self):
        usuarios = [
            {"nombre": "Ana", "edad": 18},
            {"nombre": "Luis", "edad": 99},
        ]
        assert usuarios_mayores(usuarios) == ["Ana", "Luis"]

    def test_ignora_sin_nombre(self):
        usuarios = [
            {"edad": 30},
            {"nombre": "Ana", "edad": 21},
        ]
        assert usuarios_mayores(usuarios) == ["Ana"]

    def test_ignora_sin_edad(self):
        usuarios = [
            {"nombre": "Ana"},
            {"nombre": "Luis", "edad": 22},
        ]
        assert usuarios_mayores(usuarios) == ["Luis"]

    def test_edad_exactamente_18(self):
        assert usuarios_mayores([{"nombre": "X", "edad": 18}]) == ["X"]

    def test_edad_justo_por_debajo(self):
        assert usuarios_mayores([{"nombre": "X", "edad": 17}]) == []

    def test_error_si_no_es_iterable(self):
        with pytest.raises(TypeError):
            usuarios_mayores(None)

    def test_error_si_elemento_no_es_mapeable(self):
        with pytest.raises(TypeError):
            usuarios_mayores([None])


class TestEstadisticas:
    def test_promedio_alto(self):
        resultado = estadisticas([100, 80, 60])
        assert resultado["promedio"] == 80
        assert resultado["estado"] == "ok"

    def test_promedio_bajo(self):
        resultado = estadisticas([10, 20, 30])
        assert resultado["promedio"] == 20
        assert resultado["estado"] == "bajo"

    def test_promedio_exactamente_50_es_bajo(self):
        resultado = estadisticas([50, 50])
        assert resultado["promedio"] == 50
        assert resultado["estado"] == "bajo"

    def test_promedio_justo_por_encima_de_50(self):
        resultado = estadisticas([51])
        assert resultado["promedio"] == 51
        assert resultado["estado"] == "ok"

    def test_un_solo_numero(self):
        resultado = estadisticas([0])
        assert resultado == {"promedio": 0, "estado": "bajo"}

    def test_negativos(self):
        resultado = estadisticas([-10, 10])
        assert resultado["promedio"] == 0
        assert resultado["estado"] == "bajo"

    def test_lista_vacia_divide_por_cero(self):
        with pytest.raises(ZeroDivisionError):
            estadisticas([])

    def test_error_si_no_es_iterable_de_numeros(self):
        with pytest.raises(TypeError):
            estadisticas(None)

    def test_error_si_hay_valores_no_numericos(self):
        with pytest.raises(TypeError):
            estadisticas([1, "a", 3])


class TestCargarConfig:
    def test_config_completa(self):
        assert cargar_config({"timeout": 10, "reintentos": 5}) == {
            "timeout": 10,
            "reintentos": 5,
        }

    def test_usa_valores_por_defecto(self):
        assert cargar_config({}) == {"timeout": 30, "reintentos": 3}

    def test_timeout_por_defecto(self):
        assert cargar_config({"reintentos": 1}) == {
            "timeout": 30,
            "reintentos": 1,
        }

    def test_reintentos_por_defecto(self):
        assert cargar_config({"timeout": 90}) == {
            "timeout": 90,
            "reintentos": 3,
        }

    def test_none_devuelve_sin_config(self):
        assert cargar_config(None) == "sin config"

    def test_timeout_cero_es_valido(self):
        assert cargar_config({"timeout": 0, "reintentos": 0}) == {
            "timeout": 0,
            "reintentos": 0,
        }

    def test_ignora_claves_extra(self):
        resultado = cargar_config({"timeout": 1, "reintentos": 2, "extra": True})
        assert resultado == {"timeout": 1, "reintentos": 2}

    def test_error_si_no_es_dict_ni_none(self):
        with pytest.raises(AttributeError):
            cargar_config("config")


class TestProcesarItems:
    def test_duplica_positivos(self):
        items = [{"valor": 3}, {"valor": 1.5}]
        assert procesar_items(items) == [6, 3.0]

    def test_cero_y_negativos_devuelven_cero(self):
        items = [{"valor": 0}, {"valor": -4}]
        assert procesar_items(items) == [0, 0]

    def test_sin_clave_valor_devuelve_none(self):
        items = [{}, {"otro": 1}]
        assert procesar_items(items) == [None, None]

    def test_mezcla_de_casos(self):
        items = [
            {"valor": 2},
            {"valor": -1},
            {},
            {"valor": 0},
        ]
        assert procesar_items(items) == [4, 0, None, 0]

    def test_lista_vacia(self):
        assert procesar_items([]) == []

    def test_valor_justo_por_encima_de_cero(self):
        assert procesar_items([{"valor": 0.1}]) == [0.2]

    def test_error_si_no_es_iterable(self):
        with pytest.raises(TypeError):
            procesar_items(None)

    def test_error_si_elemento_no_es_dict(self):
        with pytest.raises(TypeError):
            procesar_items([1])

    def test_error_si_valor_no_es_comparable(self):
        with pytest.raises(TypeError):
            procesar_items([{"valor": None}])
