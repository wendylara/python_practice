"""
Lara Camacho Wendy Joselin
2630056
IM 1-2
Tarea: Manejo de strings en Python

EXECUTIVE SUMMARY

   ¿Qué es un string en python?
   Una cadena de texto (string) es una secuencia de
   caracteres utilizada para representar texto. Los
   strings en Python son inmuables, lo que sinifica
   que no se pueden modificar una vez creados;
   cualquier operación que parezca modificarlos
   en realidad genera una nueva cadena.

   Operaciones básicas: 
   Soportan concatenación (+), multiplicación (*), 
   cálculo de longitud (len()), extracción de
   subcadenas (slicing), búsqueda de patrones 
   (in / find()) y reemplazo.
  
   Importancia de la validación y normalización: 
   Normalizar las entradas (usando strip() y lower()) 
   y validarlas previene errores de ejecución, 
   problemas de seguridad y datos mal formateados.
 
   ¿Qué cubrirá el documento?: 
   Este script cubre 6 problemas distintos que detallan
   el formateo de nombres, validación de correos, 
   verificación de palíndromos, estadísticas de palabras, 
   fortaleza de contraseñas y etiquetas de ancho fijo, 
   con sus casos de prueba.

"""

# PROBLEM 1: Full name formatter (name + initials)
# Description: Normalizes a full name, converts it to Title Case, and extracts 
#              the person's initials.
#
# Inputs:
# - full_name (string): Full name of a person.
#
# Outputs:
# - Formatted name: <Name In Title Case>
# - Initials: <X.X.X.>
#
# Validations:
# - full_name must not be empty after strip().
# - Must contain at least two words (name and surname).
#
# Test cases:
# 1) Normal: "  wendy   joselin lara " -> Formatted: "Wendy Joselin Lara", Initials: "W.J.L."
# 2) Border: "wendy lara" -> Formatted: "Wendy Lara", Initials: "W.L."
# 3) Error: "wendy" -> Error: invalid input (needs at least 2 words)

# Input
print("\n problem 1".upper())

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
raw_input_1 = "  wendy   joselin lara "
full_name_1 = raw_input_1.strip()

if not full_name_1:
    print("Error: invalid input")
else:
    words = full_name_1.split()
    if len(words) < 2:
        print("Error: invalid input")
    else:
        formatted_name = " ".join(words).title()
        initials = ".".join([w[0].upper() for w in words]) + "."
        print(f"Formatted name: {formatted_name}")
        print(f"Initials: {initials}")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
raw_input_2 = "wendy lara"
full_name_2 = raw_input_2.strip()

if not full_name_2:
    print("Error: invalid input")
else:
    words = full_name_2.split()
    if len(words) < 2:
        print("Error: invalid input")
    else:
        formatted_name = " ".join(words).title()
        initials = ".".join([w[0].upper() for w in words]) + "."
        print(f"Formatted name: {formatted_name}")
        print(f"Initials: {initials}")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
raw_input_3 = "wendy"
full_name_3 = raw_input_3.strip()

if not full_name_3:
    print("Error: invalid input")
else:
    words = full_name_3.split()
    if len(words) < 2:
        print("Error: invalid input")
    else:
        formatted_name = " ".join(words).title()
        initials = ".".join([w[0].upper() for w in words]) + "."
        print(f"Formatted name: {formatted_name}")
        print(f"Initials: {initials}")


# PROBLEM 2: Simple email validator (structure + domain)
# Description: Validates if an email address has a correct basic structure 
#              (exactly one '@', at least one '.' after '@', no spaces). 
#              If valid, extracts and displays the domain.
#
# Inputs:
# - email_text (string): Email address to validate.
#
# Outputs:
# - "Valid email: true" or "Valid email: false"
# - If valid: "Domain: <domain_part>"
#
# Validations:
# - email_text must not be empty after strip().
# - Must not contain whitespace.
# - Must contain exactly one '@'.
# - Must contain at least one '.' after the '@'.
#
# Test cases:
# 1) Normal: "wendy.joselin@example.com" -> Valid email: true, Domain: example.com
# 2) Border: "w@l.co" -> Valid email: true, Domain: l.co
# 3) Error: "wendy.lara@com" -> Valid email: false (missing dot after '@')

print("\nproblem 2".upper())

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
email_1 = "wendy.joselin@example.com".strip()
if not email_1 or " " in email_1 or email_1.count("@") != 1:
    print("Valid email: false")
else:
    at_index = email_1.find("@")
    domain_part = email_1[at_index + 1:]
    if "." in domain_part and len(domain_part) > 0:
        print("Valid email: true")
        print(f"Domain: {domain_part}")
    else:
        print("Valid email: false")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
email_2 = "w@l.co".strip()
if not email_2 or " " in email_2 or email_2.count("@") != 1:
    print("Valid email: false")
else:
    at_index = email_2.find("@")
    domain_part = email_2[at_index + 1:]
    if "." in domain_part and len(domain_part) > 0:
        print("Valid email: true")
        print(f"Domain: {domain_part}")
    else:
        print("Valid email: false")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
email_3 = "wendy.lara@com".strip()
if not email_3 or " " in email_3 or email_3.count("@") != 1:
    print("Valid email: false")
else:
    at_index = email_3.find("@")
    domain_part = email_3[at_index + 1:]
    if "." in domain_part and len(domain_part) > 0:
        print("Valid email: true")
        print(f"Domain: {domain_part}")
    else:
        print("Valid email: false")


# PROBLEM 3: Palindrome checker (ignoring spaces and case)
# Description: Determines if a phrase is a palindrome (reads the same forwards 
#              and backwards, ignoring spaces and case).
#
# Inputs:
# - phrase (string): The text phrase to check.
#
# Outputs:
# - "Is palindrome: true" or "Is palindrome: false"
#
# Validations:
# - phrase must not be empty after strip().
# - Minimum length of at least 3 characters after cleaning spaces.
#
# Test cases:
# 1) Normal: "Never odd or even"
# 2) Border: "A man a plan a canal Panama"
# 3) Error: "Hi"

print("\n problem 3".upper())

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
phrase_1 = "Never odd or even"
cleaned_1 = phrase_1.strip().lower().replace(" ", "")
if not phrase_1.strip() or len(cleaned_1) < 3:
    print("Is palindrome: false")
else:
    is_palindrome = (cleaned_1 == cleaned_1[::-1])
    print(f"Is palindrome: {str(is_palindrome).lower()}")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
phrase_2 = "A man a plan a canal Panama"
cleaned_2 = phrase_2.strip().lower().replace(" ", "")
if not phrase_2.strip() or len(cleaned_2) < 3:
    print("Is palindrome: false")
else:
    is_palindrome = (cleaned_2 == cleaned_2[::-1])
    print(f"Is palindrome: {str(is_palindrome).lower()}")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
phrase_3 = "Hi"
cleaned_3 = phrase_3.strip().lower().replace(" ", "")
if not phrase_3.strip() or len(cleaned_3) < 3:
    print("Is palindrome: false")
else:
    is_palindrome = (cleaned_3 == cleaned_3[::-1])
    print(f"Is palindrome: {str(is_palindrome).lower()}")


# PROBLEM 4: Sentence word stats (lengths and first/last word)
# Description: Normalizes a sentence, splits it into words, and displays total word count, 
#              first word, last word, shortest word, and longest word.
#
# Inputs:
# - sentence (string): The sentence to analyze.
#
# Outputs:
# - Word count: <n>
# - First word: <...>
# - Last word: <...>
# - Shortest word: <...>
# - Longest word: <...>
#
# Validations:
# - sentence must not be empty after strip().
# - Must contain at least one valid word after split().
#
# Test cases:
# 1) Normal: "Python programming is fun and powerful"
# 2) Border: "Hello"
# 3) Error: ""

print("\n problem 4".upper())

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
sentence_1 = "Python programming is fun and powerful"
cleaned_1 = sentence_1.strip()

if not cleaned_1:
    print("Error: invalid input (sentence is empty)")
else:
    words_1 = cleaned_1.split()
    if not words_1:
        print("Error: invalid input (no words found)")
    else:
        shortest_1 = min(words_1, key=len)
        longest_1 = max(words_1, key=len)
        print(f"Word count: {len(words_1)}")
        print(f"First word: {words_1[0]}")
        print(f"Last word: {words_1[-1]}")
        print(f"Shortest word: {shortest_1}")
        print(f"Longest word: {longest_1}")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
sentence_2 = "Hello"
cleaned_2 = sentence_2.strip()

if not cleaned_2:
    print("Error: invalid input (sentence is empty)")
else:
    words_2 = cleaned_2.split()
    if not words_2:
        print("Error: invalid input (no words found)")
    else:
        shortest_2 = min(words_2, key=len)
        longest_2 = max(words_2, key=len)
        print(f"Word count: {len(words_2)}")
        print(f"First word: {words_2[0]}")
        print(f"Last word: {words_2[-1]}")
        print(f"Shortest word: {shortest_2}")
        print(f"Longest word: {longest_2}")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
sentence_3 = "   "
cleaned_3 = sentence_3.strip()

if not cleaned_3:
    print("Error: invalid input (sentence is empty)")
else:
    words_3 = cleaned_3.split()
    if not words_3:
        print("Error: invalid input (no words found)")
    else:
        shortest_3 = min(words_3, key=len)
        longest_3 = max(words_3, key=len)
        print(f"Word count: {len(words_3)}")
        print(f"First word: {words_3[0]}")
        print(f"Last word: {words_3[-1]}")
        print(f"Shortest word: {shortest_3}")
        print(f"Longest word: {longest_3}")


# PROBLEM 5: Password strength classifier
# Description: Classifies a password as weak, medium, or strong based on 
#              length, uppercase, lowercase, digits, and special characters.
#
# Inputs:
# - password_input (string): The password to evaluate.
#
# Outputs:
# - "Password strength: weak"
# - "Password strength: medium"
# - "Password strength: strong"
#
# Validations:
# - password_input must not be empty.
# - Verify length with len().
#
# Test cases:
# 1) Normal: "Password123!" -> strong
# 2) Border: "password123" -> medium
# 3) Error: "pass" -> weak

print("\n problem 5".upper())

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
password_1 = "Password123!"
if not password_1:
    print("Password strength: weak")
else:
    length = len(password_1)
    has_upper = any(c.isupper() for c in password_1)
    has_lower = any(c.islower() for c in password_1)
    has_digit = any(c.isdigit() for c in password_1)
    has_symbol = any(not c.isalnum() for c in password_1)

    if length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")
    elif length >= 8 and (has_upper or has_lower) and (has_digit or has_symbol):
        print("Password strength: medium")
    else:
        print("Password strength: weak")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
password_2 = "password123"
if not password_2:
    print("Password strength: weak")
else:
    length = len(password_2)
    has_upper = any(c.isupper() for c in password_2)
    has_lower = any(c.islower() for c in password_2)
    has_digit = any(c.isdigit() for c in password_2)
    has_symbol = any(not c.isalnum() for c in password_2)

    if length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")
    elif length >= 8 and (has_lower or has_upper) and has_digit:
        print("Password strength: medium")
    else:
        print("Password strength: weak")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
password_3 = "pass"
if not password_3:
    print("Password strength: weak")
else:
    length = len(password_3)
    has_upper = any(c.isupper() for c in password_3)
    has_lower = any(c.islower() for c in password_3)
    has_digit = any(c.isdigit() for c in password_3)
    has_symbol = any(not c.isalnum() for c in password_3)

    if length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")
    elif length >= 8 and (has_upper or has_lower) and (has_digit or has_symbol):
        print("Password strength: medium")
    else:
        print("Password strength: weak")


# PROBLEM 6: Product label formatter (fixed-width text)
# Description: Generates a 30-character single-line product label containing 
#              product name and price, padding or truncating as needed.
#
# Inputs:
# - product_name (string)
# - price_value (string or number)
#
# Outputs:
# - "Label: <exactly 30 characters>"
#
# Validations:
# - product_name not empty after strip().
# - price_value must convert to positive number.
#
# Test cases:
# 1) Normal: "Laptop", 1200.50
# 2) Border: "A", 5
# 3) Error: "", 100

print("\n problem 6".upper())

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
product_name_1 = "Laptop"
price_value_1 = 1200.50
cleaned_name_1 = product_name_1.strip()

if not cleaned_name_1:
    print("Error: invalid product name")
else:
    try:
        numeric_price_1 = float(price_value_1)
        if numeric_price_1 < 0:
            print("Error: price must be positive")
        else:
            base_label = f"Product: {cleaned_name_1} | Price: ${numeric_price_1}"
            final_label = base_label[:30].ljust(30)
            print(f"Label: '{final_label}' (Length: {len(final_label)})")
    except ValueError:
        print("Error: invalid price format")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
product_name_2 = "A"
price_value_2 = 5
cleaned_name_2 = product_name_2.strip()

if not cleaned_name_2:
    print("Error: invalid product name")
else:
    try:
        numeric_price_2 = float(price_value_2)
        if numeric_price_2 < 0:
            print("Error: price must be positive")
        else:
            base_label = f"Product: {cleaned_name_2} | Price: ${numeric_price_2}"
            final_label = base_label[:30].ljust(30)
            print(f"Label: '{final_label}' (Length: {len(final_label)})")
    except ValueError:
        print("Error: invalid price format")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
product_name_3 = ""
price_value_3 = 100
cleaned_name_3 = product_name_3.strip()

if not cleaned_name_3:
    print("Error: invalid product name")
else:
    try:
        numeric_price_3 = float(price_value_3)
        if numeric_price_3 < 0:
            print("Error: price must be positive")
        else:
            base_label = f"Product: {cleaned_name_3} | Price: ${numeric_price_3}"
            final_label = base_label[:30].ljust(30)
            print(f"Label: '{final_label}' (Length: {len(final_label)})")
    except ValueError:
        print("Error: invalid price format")


"""
8. CONCLUSIONES

  El manejo adecuado de strings es esencial en la entrada y salida de datos 
  para garantizar que la información ingresada por los usuarios sea limpia y utilizable.
  El uso de métodos como lower(), strip(), split() y join() facilita enormemente 
  la transformación, limpieza y reconstrucción de cadenas de texto de manera eficiente.
  Normalizar el texto antes de compararlo evita errores lógicos causados por 
  espacios accidentales o diferencias entre mayúsculas y minúsculas.
  Diseñar validaciones claras desde el inicio previene la entrada de datos basura 
  y mejora drásticamente la robustez y seguridad del programa.
  Comprender la inmutabilidad de los strings nos enseña que cada modificación 
  genera un nuevo objeto, lo que vuelve crucial el uso correcto de slices e índices.

9. REFERENCIAS

1) W3Schools. (2026). Python Strings Tutorial. Recuperado de https://www.w3schools.com/python/python_strings.asp
2) Soy Dalto. (2023). Métodos de cadenas en Python. YouTube. https://www.youtube.com/watch?v=H2r9-XzV5iM
3) Stack Overflow. (2025). How to reverse a string or check for palindromes in Python. Recuperado de https://stackoverflow.com/questions/
4) GeeksforGeeks. (2025). Python String Methods. Recuperado de https://www.geeksforgeeks.org/python-string-methods/
5) freeCodeCamp Español. (2024). Curso de Python desde cero para Principiantes [Video]. YouTube. https://www.youtube.com/watch?v=4F2m5z59iuE
"""