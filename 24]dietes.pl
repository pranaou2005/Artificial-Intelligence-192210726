
disease_diets(cancer, [fruits, vegetables, lean_proteins, whole_grains, nuts]).
disease_diets(diabetes, [low_glycemic_index_foods, lean_proteins, vegetables, whole_grains]).
disease_diets(hypertension, [low_sodium_foods, fruits, vegetables, lean_proteins, whole_grains]).
disease_diets(high_cholesterol, [low_cholesterol_foods, fruits, vegetables, lean_proteins, whole_grains]).

suggest_diet(Disease, Diet) :- disease_diets(Disease, Diet)
