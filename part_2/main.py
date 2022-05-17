from flask import Flask, request, render_template
from utils import *
from config import DATA_PATH

app = Flask(__name__)



@app.route('/')
def page_index():
    """Главная страница"""
    cands_data=load_candidates_from_json(DATA_PATH)
    return render_template(
        "list.html",
        cands_data=cands_data)


@app.route('/candidate/<int:pk>/')
def page_cands_name(pk):
    """Личные страницы кандидатов"""
    cand_data=get_candidate_by_id(pk, load_candidates_from_json(DATA_PATH))
    return render_template(
        "single.html",
        cand_data =cand_data)


@app.route('/search/<candidate_name>/')
def page_cand_pk(candidate_name):
    """Поиск по имени кандидата"""
    cands_data=get_candidates_by_name(candidate_name, load_candidates_from_json(DATA_PATH))
    return render_template(
        "search.html",
        cands_num =len(cands_data),
        cands_data=cands_data)


@app.route('/skill/<skill_name>/')
def page_cand_skills(skill_name):
    """Поиск по скилу"""
    cands_data=get_candidates_by_skill(skill_name, load_candidates_from_json(DATA_PATH))
    return render_template(
        "skill.html",
        cands_num =len(cands_data),
        cands_data=cands_data)


app.run(debug=True)