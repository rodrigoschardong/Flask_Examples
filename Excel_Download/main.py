from flask import Flask, render_template, send_file
import pandas as pd

app = Flask(__name__)

@app.route('/test')
def index():
    return render_template('index.html')

@app.route('/download')
def download():
    data = {
        'Nome': ['Rodrigo', 'Lucas', 'Fernando', 'Fabio'],
        'Idade': [26, 25, 18, 27],
        'Cidade': ['Porto Alegre', 'Charqueadas', 'Guaíba', 'Rio de Janeiro']
    }
    df = pd.DataFrame(data)
    df.to_excel('data.xlsx', index=False)
    return send_file('data.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
