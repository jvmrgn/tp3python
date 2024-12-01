import os
import subprocess

def executar_script(script):
    script_path = os.path.join('questoes', script)
    subprocess.run(['python', script_path], check=True)

def main():
    for script in os.listdir(os.path.join('questoes')):
        if script.startswith('ex') and script.endswith('.py'):
            print(f"Executando {script}...")
            executar_script(script)

if __name__ == "__main__":
    main()
