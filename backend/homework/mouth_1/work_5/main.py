country_flags = {
    'kg': {'red', 'yellow'},  
    'ru': {'white', 'blue', 'red'},  
    'us': {'red', 'white', 'blue'},  
    'de': {'black', 'red', 'yellow'},  
    'fr': {'blue', 'white', 'red'},  
    'it': {'green', 'white', 'red'},  
    'jp': {'white', 'red'},  
}

while True:
    user_input = input("Введи цвет или несколько цветов через запятую (или 'выход' чтобы выйти): ").strip().lower()
    
    if user_input == 'выход':
        print("Ну всё, выход.")
        break

    colors = set(color.strip() for color in user_input.split(','))

    if len(colors) == 1:
        color = colors.pop()
        matching_countries = [domain for domain, flag_colors in country_flags.items() if color in flag_colors]
        
        if matching_countries:
            print(f"Страны с цветом '{color}': {', '.join(matching_countries)}")
        else:
            print(f"Цвет '{color}' нигде не встречается, извиняй.")
    
    else:
        matching_countries = [domain for domain, flag_colors in country_flags.items() if colors.issubset(flag_colors)]
        
        if matching_countries:
            print(f"Страны с цветами {', '.join(colors)}: {', '.join(matching_countries)}")
        else:
            print(f"Нет стран с цветами {', '.join(colors)}. Вообще нет.")

    print()