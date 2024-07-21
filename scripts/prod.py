def run():
    import subprocess

    subprocess.run("fuser -k 8000/tcp", shell=True)
    subprocess.run(
        "uvicorn app.main:api --reload --port 8000 --host 0.0.0.0", shell=True
    )
