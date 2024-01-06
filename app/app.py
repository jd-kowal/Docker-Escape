from flask import Flask, render_template, render_template_string, request

import subprocess


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    template =  '''
        <h1>This page doesn't exist</h1>
        <h3>%s</h3>
    '''  %(request.url)
    return  render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)

# counter = 0

# for _ in range(10000):
#     # Znalezienie wszystkich podklas klasy 'object'
#     all_subclasses = ''.__class__.__mro__[1].__subclasses__()

#     # Szukanie klasy subprocess.Popen wśród wszystkich podklas
#     popen_class = None
#     for subclass in all_subclasses:
#         if subclass.__name__ == 'Popen' and 'subprocess' in str(subclass):
#             popen_class = subclass
#             break

#     # Sprawdzenie, czy znaleziono klasę subprocess.Popen
#     if popen_class:
#         print("Znaleziono klasę subprocess.Popen:", popen_class)
#         counter += 1
#     else:
#         print("Klasa subprocess.Popen nie została znaleziona.")

# print(counter)
        

