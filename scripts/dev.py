def run():
    import subprocess

    subprocess.run("fuser -k 8000/tcp", shell=True)
    subprocess.run("fastapi dev app/main.py", shell=True)
