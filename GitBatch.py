import subprocess
import os

def gitInit(repoDir):
    cmd = ['git', 'init']
    p = subprocess.Popen(cmd, cwd = repoDir, stdout = subprocess.PIPE)
    output = p.communicate()[0]
    print(output)
    p.wait()

def gitAddAll(repoDir):
    cmd = ['git', 'add', '--all']
    p = subprocess.Popen(cmd, cwd = repoDir, stdout = subprocess.PIPE)
    output = p.communicate()[0]
    print(output)
    p.wait()

def gitCommit(repoDir, repoName):
    cmd = ['git', 'commit', '-am', repoName]
    p = subprocess.Popen(cmd, cwd = repoDir, stdout = subprocess.PIPE)
    output = p.communicate()[0]
    print(output)
    p.wait()

def main():
    wd = os.getcwd()
    lst = [os.path.join(wd,o) for o in os.listdir(wd) if os.path.isdir(os.path.join(wd,o))]
    dirnames = [o for o in os.listdir(wd) if os.path.isdir(os.path.join(wd,o))]
    for x in range (0, len(lst)):
        gitInit(wd)
        gitAddAll(wd)
        gitCommit(wd, dirnames[x])

main()