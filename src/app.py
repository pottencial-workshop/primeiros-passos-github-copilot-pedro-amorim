"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {

   "Futebol": {
      "description": "Treinos e jogos amistosos de futebol",
      "schedule": "Segundas e quintas, 16h - 18h",
      "max_participants": 22,
      "participants": ["alice@mergington.edu", "bruno@mergington.edu"]
   },
   "Voleibol": {
      "description": "Treinos de voleibol e participação em campeonatos escolares",
      "schedule": "Terças e sextas, 16h - 17h30",
      "max_participants": 12,
      "participants": ["carlos@mergington.edu", "lara@mergington.edu"]
   },
   "Oficina de Teatro": {
      "description": "Atividades de interpretação, expressão corporal e montagem de peças",
      "schedule": "Quartas, 15h30 - 17h",
      "max_participants": 20,
      "participants": ["mariana@mergington.edu", "pedro@mergington.edu"]
   },
   "Coral Escolar": {
      "description": "Cantos em grupo e apresentações em eventos da escola",
      "schedule": "Sábados, 10h - 12h",
      "max_participants": 40,
      "participants": ["sofia@mergington.edu", "lucas@mergington.edu"]
   },
   "Clube de Ciências": {
      "description": "Experimentos, feiras de ciências e projetos de pesquisa",
      "schedule": "Quartas, 16h - 17h30",
      "max_participants": 15,
      "participants": ["isabela@mergington.edu", "henrique@mergington.edu"]
   },
   "Clube de Matemática": {
      "description": "Resolução de problemas, preparação para olimpíadas e debates matemáticos",
      "schedule": "Sextas, 16h - 17h30",
      "max_participants": 20,
      "participants": ["raquel@mergington.edu", "mateus@mergington.edu"]
   },
   "Clube de Xadrez": {
      "description": "Aprenda estratégias e participe de torneios de xadrez",
      "schedule": "Sextas, 15h30 - 17h",
      "max_participants": 12,
      "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
   },
   "Aula de Programação": {
      "description": "Aprenda fundamentos de programação e desenvolva projetos de software",
      "schedule": "Terças e quintas, 15h30 - 16h30",
      "max_participants": 20,
      "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
   },
   "Educação Física": {
      "description": "Educação física e atividades esportivas",
      "schedule": "Segundas, quartas e sextas, 14h - 15h",
      "max_participants": 30,
      "participants": ["john@mergington.edu", "olivia@mergington.edu"]
   }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Atividade não encontrada")

    # Get the specificy activity
    activity = activities[activity_name]

    # Add student
    # Validar se o estudante já está inscrito
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Estudante já inscrito nesta atividade")

    activity["participants"].append(email)
    return {"message": f"{email} inscrito(a) em {activity_name} com sucesso"}
