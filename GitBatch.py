import subprocess
import os

def execute(cmd, wd):
    p = subprocess.Popen(cmd, cwd = wd, stdout = subprocess.PIPE)
    output = p.communicate()[0]
    print(output)
    p.wait()

def gitInit(repoDir):
    cmd = ['git', 'init']
    execute(cmd, repoDir)

def gitAddAll(repoDir):
    cmd = ['git', 'add', '--all']
    execute(cmd, repoDir)

def gitCommit(repoDir, repoName):
    cmd = ['git', 'commit', '-am', repoName]
    execute(cmd, repoDir)

def main():
    wd = os.getcwd()
    dirpaths = [os.path.join(wd,o) for o in os.listdir(wd) if os.path.isdir(os.path.join(wd,o))]
    dirnames = [o for o in os.listdir(wd) if os.path.isdir(os.path.join(wd,o))]

    print("Found "+str(len(dirnames))+" directories in "+wd)

    for x in range (0, len(dirpaths)):
        print("- Initializing repo in "+dirnames[x]+"...")
        gitInit(dirpaths[x])
        print("- Staging all files in "+dirnames[x]+"...")
        gitAddAll(dirpaths[x])
        print("- Making a commit in "+dirnames[x]+"...")
        gitCommit(dirpaths[x], dirnames[x])

main()