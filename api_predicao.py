from flask import Flask, request
import modelos_para_uso.inferencia as inf

app = Flask(__name__)

@app.route('/pred',methods=['POST'])
def pred_():
    dados = request.json
    list_dados = []
    list_dados.append([dados[x] for x in dados])
    resultado_inferencia = str(inf.inferencia(nome='xgboost').start_ml(list_dados[0]))[1:-1]
    return str(round(float(resultado_inferencia),0))

app.run(host='localhost',port=5001,debug=True)

