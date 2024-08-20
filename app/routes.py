from flask import render_template, request, flash, redirect, url_for, session
from app import app
from app.solver import solve
from app.generator import generate_board

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'original_board' not in session:
        session['original_board'] = None

    board = session.get('original_board')
    solution = None

    if request.method == 'POST':
        action = request.form.get('action')
        difficulty = int(request.form.get('difficulty', 40))  #set default difficulty to removing 40 squares

        if action == 'generate':
            board = generate_board(difficulty=difficulty)
            session['original_board'] = board  #save the original board
            solution = None
            flash("New Sudoku board generated. Please solve it and check your answer.", "info")
        else:
            #create sudoku board from the form
            user_board = []
            for i in range(9):
                row = [int(request.form.get(f'cell{i}{j}', '0') or 0) for j in range(9)]
                user_board.append(row)
            
            if action == 'solve':
                solution = solve(session['original_board'])  #solves using the original board
                flash("Sudoku puzzle solved!", "success")

    return render_template('index.html', board=board, solution=solution)