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
    gitInit(wd)
    gitAddAll(wd)
    gitCommit(wd, "GitBatch")

main()