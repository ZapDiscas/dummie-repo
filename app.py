import os

# Vulnerabilidade: Injeção de Comando (CodeQL)
@app.route('/user_info')
def user_info():
    user_id = request.args.get('id')
    # Risco de injeção de comando
    os.system("grep " + user_id + " /etc/passwd")
    return "OK"