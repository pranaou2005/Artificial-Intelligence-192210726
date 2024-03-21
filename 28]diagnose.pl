% Define symptoms
symptom(fever).
symptom(cough).
symptom(rash).
symptom(headache).
symptom(fatigue).
symptom(sore_throat).

% Define diseases and their symptoms
disease(flu, [fever, cough, fatigue]).
disease(measles, [fever, cough, rash]).
disease(common_cold, [cough, sore_throat, fatigue]).
disease(migraine, [headache, fatigue]).

% Rules for diagnosis
diagnose(Disease) :-
    disease(Disease, Symptoms),
    has_all_symptoms(Symptoms).

has_all_symptoms([]).
has_all_symptoms([Symptom | Rest]) :-
    symptom(Symptom),
    has_all_symptoms(Rest).


