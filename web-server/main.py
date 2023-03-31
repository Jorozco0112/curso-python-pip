import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return ''' <head>
		<title>Mi página de ejemplo</title>
	</head>
	<body>
	Aquí va el contenido
	</body> 
    '''
def run():
    store.get_categories()

if __name__ == '__main__':
    run()

