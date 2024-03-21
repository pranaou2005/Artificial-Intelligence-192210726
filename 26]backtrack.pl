% Define the colors of fruits
color(apple, red).
color(banana, yellow).
color(grape, purple).
color(orange, orange).
color(watermelon, green).

% Define a predicate to check if a fruit exists and retrieve its color
fruit_color(Fruit, Color) :-
    color(Fruit, Color).

% Define a predicate to check if a color exists and retrieve its corresponding fruits
color_fruit(Color, Fruit) :-
    color(Fruit, Color).

% Define a predicate to find all fruits with a specific color
fruits_with_color(Color, Fruits) :-
    findall(Fruit, color(Fruit, Color), Fruits).

% Define a predicate to find all colors of fruits
all_colors(Colors) :-
    findall(Color, color(_, Color), Colors).
