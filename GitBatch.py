import subprocess
import os

def execute(cmd, wd):
    p = subprocess.Popen(cmd, cwd = wd, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    output, error = p.communicate()
    p.wait()
    return error

def gitInit(repoDir):
    cmd = ['git', 'init']
    execute(cmd, repoDir)

def gitAddAll(repoDir):
    cmd = ['git', 'add', '--all']
    execute(cmd, repoDir)

def gitCommit(repoDir, repoName):
    cmd = ['git', 'commit', '-am', repoName]
    execute(cmd, repoDir)

def createRemoteRepo(repoName, token):
    cmd = 'curl -H "Authorization: token {t}" https://api.github.com/user/repos -d \'{{"name": "{n}", "description":"{d}"}}\''.format(t=token, n=repoName, d = "Created using GitBatch")
    p = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    output, error = p.communicate()
    ostr = str(output)
    if ('"Validation Failed",' in ostr):
        return 'A GitHub repo with the name "'+repoName+'" already exists.'
    if ('"Bad credentials",' in ostr):
        return 'Invalid GitHub token entered.'
    p.wait()
    return ' '

def gitRemoteAdd(repoDir, remoteName, url):
    cmd1 = ['git', 'remote', 'rm', remoteName]
    execute(cmd1, repoDir)
    cmd2 = ['git', 'remote', 'add', remoteName, url]
    execute(cmd2, repoDir)

def gitPush(repoDir, remoteName):
    cmd = ['git', 'push', remoteName, 'master']
    s = str(execute(cmd, repoDir))
    print(s)
    if ('Repository not found.' in s):
        return 'Invalid username.'
    return ' '


def main():
    username = raw_input("Enter your GitHub username:")
    token = raw_input("Enter your GitHub token:")
    wd = os.getcwd()
    dirpaths = [os.path.join(wd,o) for o in os.listdir(wd) if os.path.isdir(os.path.join(wd,o)) and not o.startswith('.')]
    dirnames = [o for o in os.listdir(wd) if os.path.isdir(os.path.join(wd,o)) and not o.startswith('.')]
    c = len(dirnames)
    l = len(dirnames)

    if (l == 1):
        print("----- Found 1 directory in "+wd+" -----")
    else:
        if (l == 0):
            print("Found no directories.")
        else:
            print("----- Found "+str(c)+" directories in "+wd+" -----")
            for x in range (0, len(dirpaths)):
                print('--'+dirnames[x]+'/-- :')
                print("  -> Initializing repo in "+dirnames[x]+"/...")
                gitInit(dirpaths[x])

                print("  -> Staging all files in "+dirnames[x]+"/...")
                gitAddAll(dirpaths[x])

                print("  -> Making a commit in "+dirnames[x]+"...")
                gitCommit(dirpaths[x], dirnames[x])

                print("  -> Creating GitHub repo with name "+dirnames[x]+"...")
                crs = createRemoteRepo(dirnames[x], token)
                if (crs.startswith('A')):
                    c = c - 1
                    print('ERROR: '+crs)
                    continue
                elif (crs.startswith('I')):
                    c = 0
                    print('ERROR: '+crs)
                    break

                print("  -> Adding a remote with name "+dirnames[x]+"...")
                gitRemoteAdd(dirpaths[x], dirnames[x], 'https://github.com/'+username+'/'+dirnames[x])

                print("  -> Pushing your files to the master branch of the "+dirnames[x]+" GitHub repo...")
                ps = gitPush(dirpaths[x], dirnames[x])
                if (ps.startswith('I')):
                    c = 0
                    print('ERROR: '+ps)
                    break

                print('  -> Done with the {l}/ directory.'.format(l=dirnames[x]))

            print('\nOperation Completed.')
            print('{a} out of {b} tasks were successful.'.format(a=str(c), b=str(l)))
            if (c != 0):
                print('Created {a} new Github repositories (for the entered username) and remotes, each named after the corresponding directories.'.format(a=str(c)))
                print('You\'re welcome.\n')


main()
