import pytest
from TP5funciones import *

@pytest.mark.parametrize("dni, value", [
    #cuando tiene 7 o 8 digitos
    ("46473413", True),
    ("45360529", True),
    ("123456789", False),
])
def test_dnivalid(dni, value):
    assert dnivalid(dni)== value


@pytest.mark.parametrize("frase, lon_palabra", [
    #la longitud de la ultima palabra
    ("hola como estas", 5),
    ("ornela condori", 7),
])
def test_length_last_word(frase, lon_palabra):
    assert length_last_word(frase)== lon_palabra


@pytest.mark.parametrize("frase, expected_name", [
    #Indentifica que la primer palabra es el nombre
    ("John Doe", "John"),
    ("Alice Smith", "Alice"),
    ("SingleName", "SingleName"), 
])
def test_first_name(frase, expected_name):
    assert first_name(frase) == expected_name


@pytest.mark.parametrize("numero, multiplo_de, expected_result", [
    #verifica que el primer número sea multiplo del segundo
    (10, 5, True),  
    (7, 3, False), 
    (0, 5, True), 
])
def test_es_multiplo(numero, multiplo_de, expected_result):
    assert es_multiplo(numero, multiplo_de) == expected_result


@pytest.mark.parametrize("temp_maxima, temp_minima, expected_media", [
    #media de la temperatura
    (30, 10, 20.0),
    (15, 15, 15.0),
    (-10, 10, 0.0), 
])
def test_temperatura_media(temp_maxima, temp_minima, expected_media):
    assert temperatura_media(temp_maxima, temp_minima) == expected_media


@pytest.mark.parametrize("texto, expected_result", [
    #une las palabras de una lista
    (["Hello", "World"], "Hello World"),
    (["This", "is", "a", "test"], "This is a test"),
    ([], ""),  # Lista vacía
])
def test_add_space(texto, expected_result):
    assert add_space(texto) == expected_result


@pytest.mark.parametrize("values, expected_result", [
    ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], (9, 1)),
    ([], (None, None)),  # Lista vacía
    ([10], (10, 10)),  # Lista con un solo elemento
])
def test_find_min_max(values, expected_result):
    assert find_min_max(values) == expected_result


@pytest.mark.parametrize("radio, expected_area, expected_perimetro", [
    #el area y perimetro de un circulo a partir del radio
    (5, 78.53981633974483, 31.41592653589793),
    (1, 3.141592653589793, 6.283185307179586),
    (0, 0.0, 0.0),  
])
def test_peri_area_circulo(radio, expected_area, expected_perimetro):
    area, perimetro = peri_area_circulo(radio)
    assert area == expected_area
    assert perimetro == expected_perimetro


@pytest.mark.parametrize("nombre, password, expected_result", [
    #verifica que el nombre y contraseña ingresada sea correcto
    ("usuario1", "asdasd", True),
    ("usuario2", "password", False),
    ("", "asdasd", False),  # Nombre vacío
])
def test_valid_user(nombre, password, expected_result):
    assert valid_user(nombre, password) == expected_result


@pytest.mark.parametrize("frase, expected_result", [
    #diccionario que guarda la longitud de las palabras guardadas
    ("This is a test", {"This": 4, "is": 2, "a": 1, "test": 4}),
    ("Hello world", {"Hello": 5, "world": 5}),
    ("", {}),  # Cadena vacía
])
def test_length_words(frase, expected_result):
    assert length_words(frase) == expected_result


@pytest.mark.parametrize("vector, expected_result", [
    #calcula el modulo de un vector
    ([3, 4], 5.0),  
    ([1, 2, 3], 3.7416573867739413),  
    ([0, 0], 0.0), 
])
def test_vector_modulus(vector, expected_result):
    assert vector_modulus(vector) == expected_result


@pytest.mark.parametrize("number, expected_result", [
    #verifica si un número es o no primo
    (10, False), 
    (17, True),  
    (1, False),  
])
def test_prime_number(number, expected_result):
    assert prime_number(number) == expected_result