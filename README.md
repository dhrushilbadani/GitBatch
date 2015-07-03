# GitBatch
A program that automatically creates a GitHub repo for each subdirectory of the directory it is present in. Written in Python.

-----Requirements:

1. Passwordless GitHub login. (https://help.github.com/articles/working-with-ssh-key-passphrases/)

2. API token from GitHub - generate one at https://github.com/settings/tokens . (Permissions needed - gist, repo, user, write:repo_hook.)



-----Usage:

1. Download GitBatch.py from https://drive.google.com/file/d/0B9ksUMQfjSPJNHNVdXVhWUhhTnM/view?usp=sharing

2. Copy it to the folder containing your subfolders.

3. Execute the program. You can test it using the repo1 and repo2 folders.

--- Note:
Any existing remotes, which have the same name as a subdirectory, will be overwritten! For example if you have a remote called "remote42" and a subdirectory with the same name, the remote will be overwritten!
