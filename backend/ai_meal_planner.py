def generate_meal_plan(diet: str, calories: int):
    return {
        "diet": diet,
        "calories": calories,
        "meals": [
            {"meal": "Breakfast", "description": "Oatmeal with fruits"},
            {"meal": "Lunch", "description": "Grilled chicken salad"},
            {"meal": "Dinner", "description": "Quinoa and vegetables"}
        ]
    }
