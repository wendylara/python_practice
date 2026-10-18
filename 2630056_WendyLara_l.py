"""
Lara Camacho Wendy Joselin
2630056
IM 1-2

Tarea: Colecciones de Python (Lista, Tupla, Diccionario) y Procesamiento de Datos

EXECUTIVE SUMMARY

    Las colecciones en Python (listas, tuplas y diccionarios) son estructuras 
    esenciales para almacenar, organizar y manipular grupos de datos. Una lista 
    (list) es una colección ordenada y mutable ideal para conjuntos dinámicos 
    de elementos. Una tupla (tuple) es ordenada pero inmutable, utilizada para 
    agrupar datos fijos que no deben modificarse en tiempo de ejecución. 
    Un diccionario (dict) es una estructura mutable que asocia claves únicas 
    con valores, permitiendo búsquedas y accesos directos de alta eficiencia. 
    La mutabilidad de las listas permite agregar, actualizar y eliminar elementos 
    libremente, mientras que la inmutabilidad de las tuplas garantiza integridad 
    y seguridad de datos. Los diccionarios resultan fundamentales para modelar 
    catálogos, registros de calificaciones o agendas. Este documento aborda seis 
    problemas prácticos con listas, tuplas y diccionarios, incluyendo operaciones 
    CRUD, cálculo de distancias, procesamiento de estadísticas y conteo de frecuencias, 
    acompañados de validaciones estrictas y casos de prueba detallados.

PRINCIPIOS Y BUENAS PRÁCTICAS

- Usar listas cuando se requiera agregar, modificar o eliminar elementos con frecuencia.
- Usar tuplas para agrupar datos fijos e inmutables como coordenadas geográficas o fechas.
- Usar diccionarios cuando se necesite buscar y acceder a la información mediante una clave explícita.
- Evitar modificar la estructura de una lista mientras se itera sobre ella para prevenir errores de índice.
- Definir nombres de claves descriptivos en los diccionarios (por ejemplo, "name", "grades", "price").
- Validar siempre la existencia de elementos o claves antes de intentar acceder a ellos o aplicar operaciones.

"""

# PROBLEM 1: Shopping list basics (list operations)
# Description: Manages a shopping list by parsing an initial item text, adding 
#              a new product, counting total items, and searching for a product.
#
# Inputs:
# - initial_items_text (string): Comma-separated list of initial products.
# - new_item (string): Product to append.
# - search_item (string): Product to locate.
#
# Outputs:
# - Items list: <items_list>
# - Total items: <len_list>
# - Found item: true|false
#
# Validations:
# - initial_items_text, new_item, and search_item must not be empty after strip().
# - Items are stripped of surrounding whitespace.
#
# Test cases:
# 1) Normal: "apple,banana,orange", "grape", "banana"
# 2) Border: "apple", "banana", "apple"
# 3) Error: "   ", "grape", "apple"

print("\nproblem 1".upper())

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
raw_initial_1 = "apple,banana,orange"
new_item_1 = "grape"
search_item_1 = "banana"

if not raw_initial_1.strip() or not new_item_1.strip() or not search_item_1.strip():
    print("Error: invalid input")
else:
    items_list_1 = [item.strip() for item in raw_initial_1.split(",") if item.strip()]
    items_list_1.append(new_item_1.strip())
    total_items_1 = len(items_list_1)
    is_in_list_1 = search_item_1.strip() in items_list_1
    print(f"Items list: {items_list_1}")
    print(f"Total items: {total_items_1}")
    print(f"Found item: {str(is_in_list_1).lower()}")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
raw_initial_2 = "apple"
new_item_2 = "banana"
search_item_2 = "apple"

if not raw_initial_2.strip() or not new_item_2.strip() or not search_item_2.strip():
    print("Error: invalid input")
else:
    items_list_2 = [item.strip() for item in raw_initial_2.split(",") if item.strip()]
    items_list_2.append(new_item_2.strip())
    total_items_2 = len(items_list_2)
    is_in_list_2 = search_item_2.strip() in items_list_2
    print(f"Items list: {items_list_2}")
    print(f"Total items: {total_items_2}")
    print(f"Found item: {str(is_in_list_2).lower()}")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
raw_initial_3 = "   "
new_item_3 = "grape"
search_item_3 = "apple"

if not raw_initial_3.strip() or not new_item_3.strip() or not search_item_3.strip():
    print("Error: invalid input")
else:
    items_list_3 = [item.strip() for item in raw_initial_3.split(",") if item.strip()]
    items_list_3.append(new_item_3.strip())
    total_items_3 = len(items_list_3)
    is_in_list_3 = search_item_3.strip() in items_list_3
    print(f"Items list: {items_list_3}")
    print(f"Total items: {total_items_3}")
    print(f"Found item: {str(is_in_list_3).lower()}")


# PROBLEM 2: Points and distances with tuples
# Description: Uses tuples to represent two 2D points, calculates the Euclidean 
#              distance between them, and computes their midpoint.
#
# Inputs:
# - x1, y1, x2, y2 (float): Coordinates for point A and point B.
#
# Outputs:
# - Point A: (x1, y1)
# - Point B: (x2, y2)
# - Distance: <distance>
# - Midpoint: (mx, my)
#
# Validations:
# - All inputs must be convertible to float.
#
# Test cases:
# 1) Normal: 0.0, 0.0, 3.0, 4.0
# 2) Border: 1.5, 2.5, 1.5, 2.5
# 3) Error: "abc", 0.0, 3.0, 4.0

print("\nproblem 2".upper())

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
try:
    x1_1, y1_1, x2_1, y2_1 = float(0.0), float(0.0), float(3.0), float(4.0)
    point_a_1 = (x1_1, y1_1)
    point_b_1 = (x2_1, y2_1)
    distance_1 = ((x2_1 - x1_1) ** 2 + (y2_1 - y1_1) ** 2) ** 0.5
    midpoint_1 = ((x1_1 + x2_1) / 2.0, (y1_1 + y2_1) / 2.0)
    print(f"Point A: {point_a_1}")
    print(f"Point B: {point_b_1}")
    print(f"Distance: {distance_1}")
    print(f"Midpoint: {midpoint_1}")
except ValueError:
    print("Error: invalid input")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
try:
    x1_2, y1_2, x2_2, y2_2 = float(1.5), float(2.5), float(1.5), float(2.5)
    point_a_2 = (x1_2, y1_2)
    point_b_2 = (x2_2, y2_2)
    distance_2 = ((x2_2 - x1_2) ** 2 + (y2_2 - y1_2) ** 2) ** 0.5
    midpoint_2 = ((x1_2 + x2_2) / 2.0, (y1_2 + y2_2) / 2.0)
    print(f"Point A: {point_a_2}")
    print(f"Point B: {point_b_2}")
    print(f"Distance: {distance_2}")
    print(f"Midpoint: {midpoint_2}")
except ValueError:
    print("Error: invalid input")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
try:
    x1_3, y1_3, x2_3, y2_3 = float("abc"), float(0.0), float(3.0), float(4.0)
    point_a_3 = (x1_3, y1_3)
    point_b_3 = (x2_3, y2_3)
    distance_3 = ((x2_3 - x1_3) ** 2 + (y2_3 - y1_3) ** 2) ** 0.5
    midpoint_3 = ((x1_3 + x2_3) / 2.0, (y1_3 + y2_3) / 2.0)
    print(f"Point A: {point_a_3}")
    print(f"Point B: {point_b_3}")
    print(f"Distance: {distance_3}")
    print(f"Midpoint: {midpoint_3}")
except ValueError:
    print("Error: invalid input")


# PROBLEM 3: Product catalog with dictionary
# Description: Manages a product catalog dictionary, calculates total purchase 
#              cost given a product name and quantity if the item exists.
#
# Inputs:
# - product_name (string): Name of the item to purchase.
# - quantity (int): Number of items to buy.
#
# Outputs:
# - Unit price: <unit_price>
# - Quantity: <quantity>
# - Total: <total_price>
# - Or "Error: product not found" / "Error: invalid input"
#
# Validations:
# - product_name must not be empty after strip().
# - quantity must be greater than 0.
# - product_name must exist as a key in the catalog.
#
# Test cases:
# 1) Normal: "apple", 3
# 2) Border: "banana", 1
# 3) Error: "pear", 2

print("\nproblem 3".upper())

product_prices = {
    "apple": 10.0,
    "banana": 5.0,
    "orange": 8.0
}

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
prod_1, qty_1 = "apple", 3
cleaned_prod_1 = prod_1.strip().lower()
if not cleaned_prod_1 or qty_1 <= 0:
    print("Error: invalid input")
elif cleaned_prod_1 not in product_prices:
    print("Error: product not found")
else:
    unit_price_1 = product_prices[cleaned_prod_1]
    total_price_1 = unit_price_1 * qty_1
    print(f"Unit price: {unit_price_1}")
    print(f"Quantity: {qty_1}")
    print(f"Total: {total_price_1}")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
prod_2, qty_2 = "banana", 1
cleaned_prod_2 = prod_2.strip().lower()
if not cleaned_prod_2 or qty_2 <= 0:
    print("Error: invalid input")
elif cleaned_prod_2 not in product_prices:
    print("Error: product not found")
else:
    unit_price_2 = product_prices[cleaned_prod_2]
    total_price_2 = unit_price_2 * qty_2
    print(f"Unit price: {unit_price_2}")
    print(f"Quantity: {qty_2}")
    print(f"Total: {total_price_2}")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
prod_3, qty_3 = "pear", 2
cleaned_prod_3 = prod_3.strip().lower()
if not cleaned_prod_3 or qty_3 <= 0:
    print("Error: invalid input")
elif cleaned_prod_3 not in product_prices:
    print("Error: product not found")
else:
    unit_price_3 = product_prices[cleaned_prod_3]
    total_price_3 = unit_price_3 * qty_3
    print(f"Unit price: {unit_price_3}")
    print(f"Quantity: {qty_3}")
    print(f"Total: {total_price_3}")


# PROBLEM 4: Student grades with dict and list
# Description: Stores student grade lists in a dictionary, retrieves grades for 
#              a student, calculates their average, and sets a pass flag (>= 70.0).
#
# Inputs:
# - student_name (string): Name of student to lookup.
#
# Outputs:
# - Grades: <grades_list>
# - Average: <average>
# - Passed: true|false
# - Or "Error: student not found"
#
# Validations:
# - student_name must not be empty after strip().
# - student_name must exist in dictionary.
# - Grade list must not be empty.
#
# Test cases:
# 1) Normal: "Alice"
# 2) Border: "Bob"
# 3) Error: "Charlie"

print("\nproblem 4".upper())

student_grades = {
    "Alice": [90.0, 85.0, 95.0],
    "Bob": [70.0, 70.0, 70.0]
}

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
student_1 = "Alice".strip()
if not student_1:
    print("Error: invalid input")
elif student_1 not in student_grades:
    print("Error: student not found")
else:
    grades_1 = student_grades[student_1]
    if not grades_1:
        print("Error: empty grade list")
    else:
        avg_1 = sum(grades_1) / len(grades_1)
        is_passed_1 = (avg_1 >= 70.0)
        print(f"Grades: {grades_1}")
        print(f"Average: {avg_1}")
        print(f"Passed: {str(is_passed_1).lower()}")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
student_2 = "Bob".strip()
if not student_2:
    print("Error: invalid input")
elif student_2 not in student_grades:
    print("Error: student not found")
else:
    grades_2 = student_grades[student_2]
    if not grades_2:
        print("Error: empty grade list")
    else:
        avg_2 = sum(grades_2) / len(grades_2)
        is_passed_2 = (avg_2 >= 70.0)
        print(f"Grades: {grades_2}")
        print(f"Average: {avg_2}")
        print(f"Passed: {str(is_passed_2).lower()}")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
student_3 = "Charlie".strip()
if not student_3:
    print("Error: invalid input")
elif student_3 not in student_grades:
    print("Error: student not found")
else:
    grades_3 = student_grades[student_3]
    if not grades_3:
        print("Error: empty grade list")
    else:
        avg_3 = sum(grades_3) / len(grades_3)
        is_passed_3 = (avg_3 >= 70.0)
        print(f"Grades: {grades_3}")
        print(f"Average: {avg_3}")
        print(f"Passed: {str(is_passed_3).lower()}")


# PROBLEM 5: Word frequency counter (list + dict)
# Description: Converts a sentence to lowercase, splits it into words, cleans 
#              basic punctuation, builds a frequency dict, and finds the most common word.
#
# Inputs:
# - sentence (string): Input sentence to analyze.
#
# Outputs:
# - Words list: <words_list>
# - Frequencies: <freq_dict>
# - Most common word: <word>
#
# Validations:
# - sentence must not be empty after strip().
# - Word list must contain at least one valid word.
#
# Test cases:
# 1) Normal: "Python is fun and Python is powerful"
# 2) Border: "Hello"
# 3) Error: "   "

print("\nproblem 5".upper())

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
sentence_1 = "Python is fun and Python is powerful".strip()
if not sentence_1:
    print("Error: invalid input")
else:
    cleaned_sentence_1 = sentence_1.lower().replace(".", "").replace(",", "").replace("!", "")
    words_list_1 = cleaned_sentence_1.split()
    if not words_list_1:
        print("Error: invalid input")
    else:
        freq_dict_1 = {}
        for word in words_list_1:
            if word in freq_dict_1:
                freq_dict_1[word] += 1
            else:
                freq_dict_1[word] = 1
        most_common_1 = max(freq_dict_1, key=freq_dict_1.get)
        print(f"Words list: {words_list_1}")
        print(f"Frequencies: {freq_dict_1}")
        print(f"Most common word: {most_common_1}")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
sentence_2 = "Hello".strip()
if not sentence_2:
    print("Error: invalid input")
else:
    cleaned_sentence_2 = sentence_2.lower().replace(".", "").replace(",", "").replace("!", "")
    words_list_2 = cleaned_sentence_2.split()
    if not words_list_2:
        print("Error: invalid input")
    else:
        freq_dict_2 = {}
        for word in words_list_2:
            if word in freq_dict_2:
                freq_dict_2[word] += 1
            else:
                freq_dict_2[word] = 1
        most_common_2 = max(freq_dict_2, key=freq_dict_2.get)
        print(f"Words list: {words_list_2}")
        print(f"Frequencies: {freq_dict_2}")
        print(f"Most common word: {most_common_2}")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
sentence_3 = "   ".strip()
if not sentence_3:
    print("Error: invalid input")
else:
    cleaned_sentence_3 = sentence_3.lower().replace(".", "").replace(",", "").replace("!", "")
    words_list_3 = cleaned_sentence_3.split()
    if not words_list_3:
        print("Error: invalid input")
    else:
        freq_dict_3 = {}
        for word in words_list_3:
            if word in freq_dict_3:
                freq_dict_3[word] += 1
            else:
                freq_dict_3[word] = 1
        most_common_3 = max(freq_dict_3, key=freq_dict_3.get)
        print(f"Words list: {words_list_3}")
        print(f"Frequencies: {freq_dict_3}")
        print(f"Most common word: {most_common_3}")


# PROBLEM 6: Simple contact book (dictionary CRUD)
# Description: Implements a simple contact book handling ADD, SEARCH, and 
#              DELETE operations on a dictionary of contact names and phone numbers.
#
# Inputs:
# - action_text (string): "ADD", "SEARCH", or "DELETE".
# - name (string): Contact name.
# - phone (string): Phone number (used for "ADD").
#
# Outputs:
# - Dependent on action or "Error: contact not found" / "Error: invalid input".
#
# Validations:
# - action_text must normalize to "ADD", "SEARCH", or "DELETE".
# - name must not be empty after strip().
# - phone must not be empty for "ADD".
#
# Test cases:
# 1) Normal: "ADD", "Alice", "1234567890"
# 2) Border: "SEARCH", "Bob"
# 3) Error: "DELETE", "Charlie"

print("\nproblem 6".upper())

contacts = {
    "Bob": "9876543210"
}

# Test Case 1: Normal (ADD)
print("\nTest Case 1 (ADD)")
action_1 = "ADD".strip().upper()
name_1 = "Alice".strip()
phone_1 = "1234567890".strip()

if action_1 not in ("ADD", "SEARCH", "DELETE") or not name_1:
    print("Error: invalid input")
elif action_1 == "ADD":
    if not phone_1:
        print("Error: invalid input")
    else:
        contacts[name_1] = phone_1
        print(f"Contact saved: {name_1}, {phone_1}")

# Test Case 2: Border (SEARCH)
print("\nTest Case 2 (SEARCH)")
action_2 = "SEARCH".strip().upper()
name_2 = "Bob".strip()

if action_2 not in ("ADD", "SEARCH", "DELETE") or not name_2:
    print("Error: invalid input")
elif action_2 == "SEARCH":
    if name_2 in contacts:
        print(f"Phone: {contacts[name_2]}")
    else:
        print("Error: contact not found")

# Test Case 3: Error (DELETE - Non-existent contact)
print("\nTest Case 3 (DELETE)")
action_3 = "DELETE".strip().upper()
name_3 = "Charlie".strip()

if action_3 not in ("ADD", "SEARCH", "DELETE") or not name_3:
    print("Error: invalid input")
elif action_3 == "DELETE":
    if name_3 in contacts:
        deleted_phone = contacts.pop(name_3)
        print(f"Contact deleted: {name_3}")
    else:
        print("Error: contact not found")


"""
8. CONCLUSIONES

    * El uso de listas facilita el manejo de colecciones mutables y dinámicas donde los 
    elementos se agregan, eliminan o reordenan de manera frecuente.
    * Las tuplas garantizan la inmutabilidad de los datos, siendo la estructura idónea 
    para agrupar valores fijos como coordenadas geométricas o pares de información.
    * Los diccionarios optimizan las operaciones de búsqueda y recuperación de información 
    al mapear claves únicas con sus respectivos valores con alto rendimiento.
    * La combinación de estructuras compuestas, tales como diccionarios que contienen 
    listas o tuplas, permite modelar problemas complejos del mundo real de forma limpia y legible.
    * Aplicar validaciones previas de existencia de claves o índices previene excepciones 
    en tiempo de ejecución y asegura la solidez del programa.

9. REFERENCIAS

1) W3Schools. (2026). Python Data Structures: Lists, Tuples, and Dictionaries. Recuperado de https://www.w3schools.com/python/python_datatypes.asp
2) Soy Dalto. (2023). Diccionarios y Listas en Python [Video]. YouTube. https://www.youtube.com/watch?v=H2r9-XzV5iM
3) Stack Overflow. (2025). How to handle key missing errors in Python dictionaries. Recuperado de https://stackoverflow.com/questions/
4) GeeksforGeeks. (2025). Python Collections and Data Structures. Recuperado de https://www.geeksforgeeks.org/python-data-structures/
5) freeCodeCamp Español. (2024). Estructuras de datos básicas en Python [Video]. YouTube. https://www.youtube.com/watch?v=4F2m5z59iuE
"""