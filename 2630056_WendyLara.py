"""
Lara Camacho Wendy Joselin
2630056
IM 1-2
Tarea: Tipos numéricos, booleanos y toma de decisiones en Python

EXECUTIVE SUMMARY

    Los tipos int y float en Python representan números enteros 
    y números con punto decimal respectivamente, diferenciándose 
    en su precisión y uso en memoria. Un booleano (True/False) 
    es un valor lógico que resulta comúnmente de operaciones 
    de comparación o evaluación relacional. Es fundamental validar 
    rangos y evitar la división entre cero para prevenir fallas 
    críticas en tiempo de ejecución y asegurar la integridad de los datos. 
    Este documento cubre la implementación de seis problemas prácticos 
    orientados a la conversión de temperaturas, cálculos de nómina con 
    horas extra, elegibilidad de descuentos, estadística básica de enteros, 
    aprobación de préstamos financieros y cálculo de índice de masa corporal, 
    empleando validaciones estrictas, estructuras de decisión y un manejo 
    robusto de tipos numéricos y booleanos.

PRINCIPIOS Y BUENAS PRÁCTICAS
    Usar tipos apropiados: int para contadores discretos, float para 
    cantidades continuas y monetarias.

    Evitar duplicar expresiones complejas almacenando resultados intermedios 
    en variables descriptivas.

    Validar datos antes de operar (por ejemplo, verificar rangos positivos y 
    prevenir división por cero).

    Usar nombres de variables claros en lower_snake_case y constantes en 
    UPPER_SNAKE_CASE.

    Documentar explícitamente el significado de los valores booleanos dentro de 
    cada contexto de negocio.

"""

# PROBLEM 1: Temperature converter and range flag
# Description: Converts a temperature in Celsius to Fahrenheit and Kelvin, 
#              and determines a boolean flag if it is a high temperature (>= 30.0).

# Inputs:
# - temp_c (float): Temperature in degrees Celsius.

# Outputs:
# - Fahrenheit: <temp_f>
# - Kelvin: <temp_k>
# - High temperature: true|false

# Validations:
# - temp_c must be convertible to float.
# - Kelvin temperature must not be physically impossible (temp_k >= 0.0).

# Test cases:
# 1) Normal: 32.5 -> Fahrenheit: 90.5, Kelvin: 305.65, High temperature: true
# 2) Border: 30.0 -> Fahrenheit: 86.0, Kelvin: 303.15, High temperature: true
# 3) Error: -300.0 -> Error: invalid input (Kelvin below absolute zero)

print("problem 1".upper())

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
temp_c_1 = 32.5
temp_k_1 = temp_c_1 + 273.15
if temp_k_1 < 0.0:
    print("Error: invalid input")
else:
    temp_f_1 = temp_c_1 * 9 / 5 + 32
    is_high_temperature_1 = (temp_c_1 >= 30.0)
    print(f"Fahrenheit: {temp_f_1}")
    print(f"Kelvin: {temp_k_1}")
    print(f"High temperature: {str(is_high_temperature_1).lower()}")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
temp_c_2 = 30.0
temp_k_2 = temp_c_2 + 273.15
if temp_k_2 < 0.0:
    print("Error: invalid input")
else:
    temp_f_2 = temp_c_2 * 9 / 5 + 32
    is_high_temperature_2 = (temp_c_2 >= 30.0)
    print(f"Fahrenheit: {temp_f_2}")
    print(f"Kelvin: {temp_k_2}")
    print(f"High temperature: {str(is_high_temperature_2).lower()}")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
temp_c_3 = -300.0
temp_k_3 = temp_c_3 + 273.15
if temp_k_3 < 0.0:
    print("Error: invalid input")
else:
    temp_f_3 = temp_c_3 * 9 / 5 + 32
    is_high_temperature_3 = (temp_c_3 >= 30.0)
    print(f"Fahrenheit: {temp_f_3}")
    print(f"Kelvin: {temp_k_3}")
    print(f"High temperature: {str(is_high_temperature_3).lower()}")


# PROBLEM 2: Work hours and overtime payment
# Description: Calculates weekly total pay given regular hours and overtime 
#              (hours > 40 paid at 150%), with a boolean flag for overtime.

# Inputs:
# - hours_worked (float): Total hours worked in a week.
# - hourly_rate (float): Standard pay rate per hour.

# Outputs:
# - Regular pay: <regular_pay>
# - Overtime pay: <overtime_pay>
# - Total pay: <total_pay>
# - Has overtime: true|false

# Validations:
# - hours_worked >= 0 and hourly_rate > 0.

# Test cases:
# 1) Normal: 45.0 hours, 20.0 rate
# 2) Border: 40.0 hours, 15.0 rate
# 3) Error: -5.0 hours, 20.0 rate

print("\nproblem 2".upper())

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
hours_1, rate_1 = 45.0, 20.0
if hours_1 < 0 or rate_1 <= 0:
    print("Error: invalid input")
else:
    reg_hours_1 = min(hours_1, 40.0)
    ot_hours_1 = max(0.0, hours_1 - 40.0)
    reg_pay_1 = reg_hours_1 * rate_1
    ot_pay_1 = ot_hours_1 * rate_1 * 1.5
    tot_pay_1 = reg_pay_1 + ot_pay_1
    has_ot_1 = (hours_1 > 40.0)
    print(f"Regular pay: {reg_pay_1}")
    print(f"Overtime pay: {ot_pay_1}")
    print(f"Total pay: {tot_pay_1}")
    print(f"Has overtime: {str(has_ot_1).lower()}")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
hours_2, rate_2 = 40.0, 15.0
if hours_2 < 0 or rate_2 <= 0:
    print("Error: invalid input")
else:
    reg_hours_2 = min(hours_2, 40.0)
    ot_hours_2 = max(0.0, hours_2 - 40.0)
    reg_pay_2 = reg_hours_2 * rate_2
    ot_pay_2 = ot_hours_2 * rate_2 * 1.5
    tot_pay_2 = reg_pay_2 + ot_pay_2
    has_ot_2 = (hours_2 > 40.0)
    print(f"Regular pay: {reg_pay_2}")
    print(f"Overtime pay: {ot_pay_2}")
    print(f"Total pay: {tot_pay_2}")
    print(f"Has overtime: {str(has_ot_2).lower()}")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
hours_3, rate_3 = -5.0, 20.0
if hours_3 < 0 or rate_3 <= 0:
    print("Error: invalid input")
else:
    reg_hours_3 = min(hours_3, 40.0)
    ot_hours_3 = max(0.0, hours_3 - 40.0)
    reg_pay_3 = reg_hours_3 * rate_3
    ot_pay_3 = ot_hours_3 * rate_3 * 1.5
    tot_pay_3 = reg_pay_3 + ot_pay_3
    has_ot_3 = (hours_3 > 40.0)
    print(f"Regular pay: {reg_pay_3}")
    print(f"Overtime pay: {ot_pay_3}")
    print(f"Total pay: {tot_pay_3}")
    print(f"Has overtime: {str(has_ot_3).lower()}")


# PROBLEM 3: Discount eligibility with booleans
# Description: Determines if a customer qualifies for a discount based on 
#              student status, senior status, or a high purchase total.

# Inputs:
# - purchase_total (float): Total amount of the purchase.
# - is_student_text (string): "YES" or "NO".
# - is_senior_text (string): "YES" or "NO".

# Outputs:
# - Discount eligible: true|false
# - Final total: <final_total>

# Validations:
# - purchase_total >= 0.0
# - Text inputs must normalize to "YES" or "NO".

# Test cases:
# 1) Normal: 1200.0, "NO", "NO"
# 2) Border: 500.0, "YES", "NO"
# 3) Error: 500.0, "MAYBE", "NO"

print("\nproblem 3".upper())

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
tot_1, student_1, senior_1 = 1200.0, "NO", "NO"
st_norm_1 = student_1.strip().upper()
sen_norm_1 = senior_1.strip().upper()
if tot_1 < 0.0 or st_norm_1 not in ("YES", "NO") or sen_norm_1 not in ("YES", "NO"):
    print("Error: invalid input")
else:
    is_stu_1 = (st_norm_1 == "YES")
    is_sen_1 = (sen_norm_1 == "YES")
    disc_elig_1 = is_stu_1 or is_sen_1 or (tot_1 >= 1000.0)
    fin_tot_1 = tot_1 * 0.9 if disc_elig_1 else tot_1
    print(f"Discount eligible: {str(disc_elig_1).lower()}")
    print(f"Final total: {fin_tot_1}")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
tot_2, student_2, senior_2 = 500.0, "YES", "NO"
st_norm_2 = student_2.strip().upper()
sen_norm_2 = senior_2.strip().upper()
if tot_2 < 0.0 or st_norm_2 not in ("YES", "NO") or sen_norm_2 not in ("YES", "NO"):
    print("Error: invalid input")
else:
    is_stu_2 = (st_norm_2 == "YES")
    is_sen_2 = (sen_norm_2 == "YES")
    disc_elig_2 = is_stu_2 or is_sen_2 or (tot_2 >= 1000.0)
    fin_tot_2 = tot_2 * 0.9 if disc_elig_2 else tot_2
    print(f"Discount eligible: {str(disc_elig_2).lower()}")
    print(f"Final total: {fin_tot_2}")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
tot_3, student_3, senior_3 = 500.0, "MAYBE", "NO"
st_norm_3 = student_3.strip().upper()
sen_norm_3 = senior_3.strip().upper()
if tot_3 < 0.0 or st_norm_3 not in ("YES", "NO") or sen_norm_3 not in ("YES", "NO"):
    print("Error: invalid input")
else:
    is_stu_3 = (st_norm_3 == "YES")
    is_sen_3 = (sen_norm_3 == "YES")
    disc_elig_3 = is_stu_3 or is_sen_3 or (tot_3 >= 1000.0)
    fin_tot_3 = tot_3 * 0.9 if disc_elig_3 else tot_3
    print(f"Discount eligible: {str(disc_elig_3).lower()}")
    print(f"Final total: {fin_tot_3}")


# Problem 4: Basic statistics of three integers
# Description: Reads three integers and computes their sum, average, max, min, 
#              and a boolean flag indicating if all numbers are even.

# Inputs:
# - n1, n2, n3 (int): Three integer numbers.

# Outputs:
# - Sum: <sum_value>
# - Average: <average_value>
# - Max: <max_value>
# - Min: <min_value>
# - All even: true|false

# Validations:
# - Inputs must be convertible to integers.

# Test cases:
# 1) Normal: 4, 8, 12
# 2) Border: 3, 4, 5
# 3) Error: "abc", 2, 3

print("\nproblem 4".upper())

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
try:
    n1_1, n2_1, n3_1 = int(4), int(8), int(12)
    sum_v_1 = n1_1 + n2_1 + n3_1
    avg_v_1 = sum_v_1 / 3.0
    max_v_1 = max(n1_1, n2_1, n3_1)
    min_v_1 = min(n1_1, n2_1, n3_1)
    all_ev_1 = (n1_1 % 2 == 0) and (n2_1 % 2 == 0) and (n3_1 % 2 == 0)
    print(f"Sum: {sum_v_1}")
    print(f"Average: {avg_v_1}")
    print(f"Max: {max_v_1}")
    print(f"Min: {min_v_1}")
    print(f"All even: {str(all_ev_1).lower()}")
except ValueError:
    print("Error: invalid input")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
try:
    n1_2, n2_2, n3_2 = int(3), int(4), int(5)
    sum_v_2 = n1_2 + n2_2 + n3_2
    avg_v_2 = sum_v_2 / 3.0
    max_v_2 = max(n1_2, n2_2, n3_2)
    min_v_2 = min(n1_2, n2_2, n3_2)
    all_ev_2 = (n1_2 % 2 == 0) and (n2_2 % 2 == 0) and (n3_2 % 2 == 0)
    print(f"Sum: {sum_v_2}")
    print(f"Average: {avg_v_2}")
    print(f"Max: {max_v_2}")
    print(f"Min: {min_v_2}")
    print(f"All even: {str(all_ev_2).lower()}")
except ValueError:
    print("Error: invalid input")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
try:
    n1_3 = int("abc")
    n2_3 = int(2)
    n3_3 = int(3)
    sum_v_3 = n1_3 + n2_3 + n3_3
    avg_v_3 = sum_v_3 / 3.0
    max_v_3 = max(n1_3, n2_3, n3_3)
    min_v_3 = min(n1_3, n2_3, n3_3)
    all_ev_3 = (n1_3 % 2 == 0) and (n2_3 % 2 == 0) and (n3_3 % 2 == 0)
    print(f"Sum: {sum_v_3}")
    print(f"Average: {avg_v_3}")
    print(f"Max: {max_v_3}")
    print(f"Min: {min_v_3}")
    print(f"All even: {str(all_ev_3).lower()}")
except ValueError:
    print("Error: invalid input")


# Problem 5: Loan eligibility (income and debt ratio)
# Description: Evaluates loan approval based on monthly income, debt ratio 
#              (monthly debt / monthly income), and credit score.

# Inputs:
# - monthly_income (float): Monthly income amount.
# - monthly_debt (float): Monthly debt payments.
# - credit_score (int): Borrower credit score.

# Outputs:
# - Debt ratio: <debt_ratio>
# - Eligible: true|false

# Validations:
# - monthly_income > 0.0 (prevents division by zero).
# - monthly_debt >= 0.0 and credit_score >= 0.

# Test cases:
# 1) Normal: 10000.0, 2000.0, 700
# 2) Border: 8000.0, 3200.0, 650
# 3) Error: 0.0, 500.0, 700

print("\nproblem 5".upper())

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
inc_1, debt_1, score_1 = 10000.0, 2000.0, 700
if inc_1 <= 0.0 or debt_1 < 0.0 or score_1 < 0:
    print("Error: invalid input")
else:
    debt_rat_1 = debt_1 / inc_1
    elig_1 = (inc_1 >= 8000.0 and debt_rat_1 <= 0.4 and score_1 >= 650)
    print(f"Debt ratio: {debt_rat_1}")
    print(f"Eligible: {str(elig_1).lower()}")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
inc_2, debt_2, score_2 = 8000.0, 3200.0, 650
if inc_2 <= 0.0 or debt_2 < 0.0 or score_2 < 0:
    print("Error: invalid input")
else:
    debt_rat_2 = debt_2 / inc_2
    elig_2 = (inc_2 >= 8000.0 and debt_rat_2 <= 0.4 and score_2 >= 650)
    print(f"Debt ratio: {debt_rat_2}")
    print(f"Eligible: {str(elig_2).lower()}")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
inc_3, debt_3, score_3 = 0.0, 500.0, 700
if inc_3 <= 0.0 or debt_3 < 0.0 or score_3 < 0:
    print("Error: invalid input")
else:
    debt_rat_3 = debt_3 / inc_3
    elig_3 = (inc_3 >= 8000.0 and debt_rat_3 <= 0.4 and score_3 >= 650)
    print(f"Debt ratio: {debt_rat_3}")
    print(f"Eligible: {str(elig_3).lower()}")


# Problem 6: Body Mass Index (BMI) and category flag
# Description: Calculates Body Mass Index (BMI) and sets boolean range flags 
#              for underweight, normal weight, and overweight categories.

# Inputs:
# - weight_kg (float): Weight in kilograms.
# - height_m (float): Height in meters.

# Outputs:
# - BMI: <bmi_rounded>
# - Underweight: true|false
# - Normal: true|false
# - Overweight: true|false

# Validations:
# - weight_kg > 0.0 and height_m > 0.0

# Test cases:
# 1) Normal: 70.0 kg, 1.75 m
# 2) Border: 50.0 kg, 1.64 m
# 3) Error: -70.0 kg, 1.75 m

print("\nproblem 6".upper())

# Test Case 1: Normal
print("\nTest Case 1 (Normal)")
w_1, h_1 = 70.0, 1.75
if w_1 <= 0.0 or h_1 <= 0.0:
    print("Error: invalid input")
else:
    bmi_1 = w_1 / (h_1 * h_1)
    bmi_rnd_1 = round(bmi_1, 2)
    is_under_1 = (bmi_1 < 18.5)
    is_norm_1 = (18.5 <= bmi_1 < 25.0)
    is_over_1 = (bmi_1 >= 25.0)
    print(f"BMI: {bmi_rnd_1}")
    print(f"Underweight: {str(is_under_1).lower()}")
    print(f"Normal: {str(is_norm_1).lower()}")
    print(f"Overweight: {str(is_over_1).lower()}")

# Test Case 2: Border
print("\nTest Case 2 (Border)")
w_2, h_2 = 50.0, 1.64
if w_2 <= 0.0 or h_2 <= 0.0:
    print("Error: invalid input")
else:
    bmi_2 = w_2 / (h_2 * h_2)
    bmi_rnd_2 = round(bmi_2, 2)
    is_under_2 = (bmi_2 < 18.5)
    is_norm_2 = (18.5 <= bmi_2 < 25.0)
    is_over_2 = (bmi_2 >= 25.0)
    print(f"BMI: {bmi_rnd_2}")
    print(f"Underweight: {str(is_under_2).lower()}")
    print(f"Normal: {str(is_norm_2).lower()}")
    print(f"Overweight: {str(is_over_2).lower()}")

# Test Case 3: Error
print("\nTest Case 3 (Error)")
w_3, h_3 = -70.0, 1.75
if w_3 <= 0.0 or h_3 <= 0.0:
    print("Error: invalid input")
else:
    bmi_3 = w_3 / (h_3 * h_3)
    bmi_rnd_3 = round(bmi_3, 2)
    is_under_3 = (bmi_3 < 18.5)
    is_norm_3 = (18.5 <= bmi_3 < 25.0)
    is_over_3 = (bmi_3 >= 25.0)
    print(f"BMI: {bmi_rnd_3}")
    print(f"Underweight: {str(is_under_3).lower()}")
    print(f"Normal: {str(is_norm_3).lower()}")
    print(f"Overweight: {str(is_over_3).lower()}")


"""
8. CONCLUSIONES

Los tipos enteros y flotantes se emplean de forma combinada en escenarios 
del mundo real para representar cantidades discretas y continuas con precisión 
matemática. Las expresiones de comparación evalúan condiciones relacionales 
transformando datos numéricos en valores booleanos que controlan la toma de 
decisiones mediante instrucciones condicionales. Validar rangos numéricos y 
prevenir divisiones entre cero es una práctica indispensable para evitar excepciones 
y comportamientos inesperados en el software. Combinar operadores lógicos como 
and, or y not permite modelar reglas de negocio complejas de manera limpia y 
estructurada. Estos patrones de diseño se replican constantemente en sistemas 
comerciales orientados a nóminas, comercios electrónicos, evaluación crediticia y 
control médico.

9. REFERENCIAS

1) Python documentation. Built-in Types: Numeric Types — int, float, complex. Recuperado de https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
2) Python documentation. Boolean type — bool. Recuperado de https://docs.python.org/3/library/stdtypes.html#truth-value-testing
3) W3Schools. Python Operators and Booleans. Recuperado de https://www.w3schools.com/python/python_operators.asp
4) Lutz, M. Learning Python (5th ed.). O'Reilly Media, 2013.
5) GeeksforGeeks. Python Arithmetic and Logical Operators with Examples. Recuperado de https://www.geeksforgeeks.org/python-operators/
"""