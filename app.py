from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/send.data', methods = ['POST'])
def send_data():
    #INPUT
    calcio = request.form['calcio']
    magnesio = request.form['magnesio']
    potassio = request.form['potassio']
    sodio = request.form['sodio']
    hidrogeniomaisaluminio = request.form['hidrogenio-mais-aluminio']
    saturacaoporbases = request.form['saturacao-por-bases']
    camada = request.form['camada-de-solo']

    # OUTPUT
    if calcio == '' or magnesio == '' or potassio == '' or sodio == '' or hidrogeniomaisaluminio == '' \
            or saturacaoporbases == '' or camada == '':
        prognostico_de_calagem = str("Você deixou campos vazios no formulário. Tente novamente sempre digitando um número")
        return render_template('home.html', prognostico_de_calagem=prognostico_de_calagem)

    else:
        calcio = calcio.replace(',', '.')
        magnesio = magnesio.replace(',', '.')
        potassio = potassio.replace(',', '.')
        sodio = sodio.replace(',', '.')
        hidrogeniomaisaluminio = hidrogeniomaisaluminio.replace(',', '.')
        saturacaoporbases = saturacaoporbases.replace(',', '.')
        camada = camada.replace(',', '.')

        calcio = float(calcio)
        magnesio = float(magnesio)
        potassio = float(potassio)
        sodio = float(sodio)
        hidrogeniomaisaluminio = float(hidrogeniomaisaluminio)
        saturacaoporbases = float(saturacaoporbases)
        camada = float(camada)

        necessidade_de_calagem = str(calcula_necessidade_de_calagem(calcio, magnesio, potassio, sodio,
                                                                    hidrogeniomaisaluminio,
                                                                    saturacaoporbases,
                                                                    camada))

        quantidade_de_calagem = necessidade_de_calagem.replace('.', ',')

        prognostico_de_calagem = str(
            'Considerando uma aplicação em área total, recomenda-se para uma profundidade de ' +
            str(round(camada, 0)) + ' cm, aplicar um valor equivalente à ' +
            quantidade_de_calagem + ' t/ha')

        return render_template('home.html', prognostico_de_calagem=prognostico_de_calagem)

if (__name__ == '__main__'):
    app.run(debug=True)