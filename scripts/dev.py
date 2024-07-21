def run():
    import subprocess

    subprocess.run("fuser -k 3000/tcp", shell=True)
    subprocess.run(
        "uvicorn app.main:api --reload --port 3000 --log-level debug", shell=True
    )
