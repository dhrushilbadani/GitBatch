# GitBatch
A program that automatically creates a GitHub repo for each subdirectory of the directory it is present in. Written in Python.

##Requirements:

1. [Passwordless GitHub login](https://help.github.com/articles/working-with-ssh-key-passphrases/) for your account set up on your terminal. 

2. Personal access token from GitHub - generate one [here](https://github.com/settings/tokens) . (Permissions needed - ```public_repo```)



##Usage:

1. Download the .zip file from the pane on the right >> and extract its contents (Git folks can feel free to fork+pull too).

2. Copy GitBatch.py to the folder containing your subfolders.

3. Execute the program. You can test it using the repo1 and repo2 folders.

##Note:
<ul>
<li>Any existing remotes, which have the same name as a subdirectory, will be overwritten! For example if you have a remote called "remote42" and a subdirectory with the same name, the remote will be overwritten.</li>
<li>Since GitBatch attempts to create a repo with the same name as the directory, it'll crash if there already exists a GitHub repo with the same name as that of the directory.</li>
</ul>
