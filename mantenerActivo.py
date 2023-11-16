import requests
import time

def realizar_peticion():
    url = 'https://viramsoftapi.onrender.com/docs'
    # Puedes agregar parámetros, encabezados, etc., según lo que requiera la API.

    try:
        response = requests.get(url)
        # Si es una API que requiere autenticación, puedes usar requests.post() u otros métodos según sea necesario.
        
        # Imprime la respuesta para verificar el estado de la petición.
        print(f'Respuesta: {response.status_code}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

if __name__ == "__main__":
    while True:
        realizar_peticion()
        # Espera un tiempo antes de realizar la próxima petición.
        time.sleep(90)  # Espera 5 minutos (ajusta el valor según tus necesidades).
        print("ESTA VIVO!!")
