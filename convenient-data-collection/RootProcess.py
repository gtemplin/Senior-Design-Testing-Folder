import os
import multiprocessing  # allows for multiple CPU cores to be used to run different programs in parallel 
import subprocess  # allows for other programs/scripts to be called from this program
import contextlib
import select
import urllib3

# CURPATH is an environment variable created by the Dockerfile 
Curpath = os.getenv('CURPATH', '/usr/src/app')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


print("Root process's top ")

# Execute Script, outputs the standard error if applicable 
def execute_script(script_path):
    try:
        subprocess.run(['python', script_path], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_path}: {e}\nError Output:\n{e.stderr}")

def debug_exec_script(script_path):
    # Start the script using Popen and set stdout and stderr to subprocess.PIPE
    process = subprocess.Popen(['python3', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Monitor the stdout and stderr of the process
    while True:
        reads = [process.stdout.fileno(), process.stderr.fileno()]
        ret = select.select(reads, [], [])

        for fd in ret[0]:
            if fd == process.stdout.fileno():
                print(process.stdout.readline().strip())
            if fd == process.stderr.fileno():
                print("ERROR:", process.stderr.readline().strip())

        if process.poll() is not None:
            break

    # Check if the process has exited and any remaining output
    if process.returncode is not None:
        print(f"Process {script_path} completed with return code {process.returncode}")




# Main Function 
if __name__ == '__main__':
    try:
        os.remove(os.path.join(Curpath, ".oauth2_token"))
    except Exception:
        pass
    try:
        os.remove(os.path.join(Curpath, "CommunicationFlag.txt"))
    except Exception:
        pass

    processes = [
        os.path.join(Curpath, 'Sensing.py'),
        os.path.join(Curpath, 'ActuatorControl.py'),
        os.path.join(Curpath, 'DatabaseWrite.py')
    ]
    numProcesses = len(processes)

    print("Starting root process: ")
 # this sets up the parallel processing
    with contextlib.suppress(KeyboardInterrupt):
        print("Inside with")
        pool = multiprocessing.Pool(processes=numProcesses)
        #pool.map(execute_script, processes)
        pool.map(debug_exec_script, processes)
        pool.close()
        pool.join()
