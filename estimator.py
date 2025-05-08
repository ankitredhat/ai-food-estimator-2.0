def estimate_people_by_logic(container_type, food_type):
    volume_map = {
        "small": 2000,
        "medium": 5000,
        "large": 10000
    }

    food_density_factor = {
        "dry": 1.0,
        "semi-solid": 0.85,
        "liquid": 0.75
    }

    per_person_consumption = {
        "dry": 300,
        "semi-solid": 350,
        "liquid": 400
    }

    volume_ml = volume_map.get(container_type, 3000)
    density_factor = food_density_factor.get(food_type, 1.0)
    avg_meal = per_person_consumption.get(food_type, 300)

    effective_volume = volume_ml * density_factor
    estimated_people = round(effective_volume / avg_meal)
    return estimated_people