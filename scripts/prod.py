def run():
    import subprocess

    subprocess.run(
        "uvicorn app.main:api --reload --port 8000 --host 0.0.0.0", shell=True
    )
