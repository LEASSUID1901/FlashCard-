from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser React à communiquer avec l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

questions = [
    {"id": 1, "question": "La Tour Eiffel a été construite pour l'Exposition Universelle de 1889.", "answer": "Vrai", "category": "histoire", "difficulty": "easy"},
    {"id": 2, "question": "Le soleil est une planète.", "answer": "Faux", "category": "sciences", "difficulty": "easy"},
    {"id": 3, "question": "L'Australie est à la fois un pays et un continent.", "answer": "Vrai", "category": "géographie", "difficulty": "easy"},
    {"id": 4, "question": "Le Mont Everest est la montagne la plus haute du monde.", "answer": "Vrai", "category": "géographie", "difficulty": "easy"},
    {"id": 5, "question": "Leonardo DiCaprio a gagné son premier Oscar pour Titanic.", "answer": "Faux", "category": "cinéma", "difficulty": "medium"},
    {"id": 6, "question": "Le cœur humain a 4 chambres.", "answer": "Vrai", "category": "sciences", "difficulty": "easy"},
    {"id": 7, "question": "Le Brésil est le seul pays d'Amérique du Sud où on parle portugais.", "answer": "Vrai", "category": "géographie", "difficulty": "medium"},
    {"id": 8, "question": "La Grande Muraille de Chine est visible depuis la lune à l'œil nu.", "answer": "Faux", "category": "histoire", "difficulty": "medium"},
    {"id": 9, "question": "Les dauphins sont des poissons.", "answer": "Faux", "category": "sciences", "difficulty": "easy"},
    {"id": 10, "question": "Le Japon a 4 îles principales.", "answer": "Vrai", "category": "géographie", "difficulty": "medium"},
    {"id": 11, "question": "Shakespeare est né et mort le même jour de l'année.", "answer": "Vrai", "category": "histoire", "difficulty": "hard"},
    {"id": 12, "question": "La vitesse de la lumière est d'environ 300 000 km/s.", "answer": "Vrai", "category": "sciences", "difficulty": "medium"},
    {"id": 13, "question": "Le Titanic a coulé en 1912.", "answer": "Vrai", "category": "histoire", "difficulty": "easy"},
    {"id": 14, "question": "Paris est la ville la plus visitée du monde.", "answer": "Vrai", "category": "géographie", "difficulty": "easy"},
    {"id": 15, "question": "Les chauves-souris sont aveugles.", "answer": "Faux", "category": "sciences", "difficulty": "medium"},
    {"id": 16, "question": "Le diamant est la matière naturelle la plus dure.", "answer": "Vrai", "category": "sciences", "difficulty": "easy"},
    {"id": 17, "question": "L'Afrique est le plus grand continent du monde.", "answer": "Faux", "category": "géographie", "difficulty": "medium"},
    {"id": 18, "question": "Mozart était autrichien.", "answer": "Vrai", "category": "histoire", "difficulty": "medium"},
    {"id": 19, "question": "Le football a été inventé en Angleterre.", "answer": "Vrai", "category": "sport", "difficulty": "easy"},
    {"id": 20, "question": "Les pieuvres ont 8 cœurs.", "answer": "Faux", "category": "sciences", "difficulty": "hard"},
]

@app.get("/questions")
def get_questions(category: str = None, difficulty: str = None):
    result = questions
    if category:
        result = [q for q in result if q["category"] == category]
    if difficulty:
        result = [q for q in result if q["difficulty"] == difficulty]
    return result

@app.get("/questions/{id}")
def get_question(id: int):
    for q in questions:
        if q["id"] == id:
            return q
    return {"error": "Question non trouvée"}

@app.get("/categories")
def get_categories():
    cats = list(set([q["category"] for q in questions]))
    return cats