import subprocess

def start_server():
    try:
        subprocess.run(["python3", "ServerDJANGO/mysite/manage.py", "runserver", "9090"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error al iniciar el servidor Django:", e)