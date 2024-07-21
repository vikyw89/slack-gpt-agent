def run():
    import subprocess

    subprocess.run("black .", shell=True)
    subprocess.run("ruff format .", shell=True)
