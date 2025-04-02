def calcular_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        return "Error: Ingrese valores válidos para peso y altura."
    
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        estado = "Bajo peso"
        recomendacion = (
            "Debe aumentar su consumo calórico diario, priorizando alimentos ricos en proteínas, carbohidratos complejos y grasas saludables. "
            "Incluya en su dieta frutos secos, aguacate, carnes magras, arroz integral y legumbres. "
            "Para el ejercicio, es recomendable enfocarse en entrenamientos de fuerza como levantamiento de pesas y ejercicios de resistencia para ganar masa muscular. "
            "Evite el exceso de cardio y concéntrese en un superávit calórico."
        )
    elif 18.5 <= imc < 24.9:
        estado = "Peso normal"
        recomendacion = (
            "Su peso está dentro del rango saludable. Mantenga una dieta equilibrada con proteínas, carbohidratos y grasas en proporciones adecuadas. "
            "Priorice alimentos frescos y evite los ultraprocesados. Para el ejercicio, realice una combinación de cardio moderado (correr, nadar, bicicleta) y entrenamiento de fuerza. "
            "La clave es la constancia y mantener un equilibrio calórico para evitar fluctuaciones en el peso."
        )
    elif 25 <= imc < 29.9:
        estado = "Sobrepeso"
        recomendacion = (
            "Es recomendable reducir la ingesta de calorías diarias, evitando azúcares refinados y grasas saturadas. "
            "Priorice alimentos como verduras, frutas, proteínas magras y cereales integrales. "
            "Para el ejercicio, lo ideal es combinar sesiones de cardio (como caminatas rápidas, correr o nadar) con entrenamiento de fuerza para mejorar la composición corporal. "
            "Asegúrese de mantener un déficit calórico moderado para lograr una reducción de peso progresiva."
        )
    else:
        estado = "Obesidad"
        recomendacion = (
            "Es importante adoptar un plan de alimentación controlado en calorías, reduciendo el consumo de alimentos ultraprocesados y bebidas azucaradas. "
            "Se recomienda aumentar el consumo de fibra, proteínas magras y grasas saludables. "
            "Para la actividad física, comience con ejercicios de bajo impacto como caminar, nadar o montar bicicleta, y a medida que mejore su resistencia, incorpore entrenamiento de fuerza. "
            "Un déficit calórico bien estructurado es clave para reducir el peso de manera saludable."
        )
    
    return f"IMC: {imc:.2f}, Estado: {estado}\nRecomendación: {recomendacion}"

# Ejemplo de uso
try:
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    resultado = calcular_imc(peso, altura)
    print(resultado)
except ValueError:
    print("Error: Ingrese valores numéricos válidos para peso y altura.")