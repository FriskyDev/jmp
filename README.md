# Jump Lists in Linux / OSX

Do you constantly need to jump between different locations with very different paths. Yes, cd and pushd / popd can help you get around sometimes. But I find that I am constantly jumping back and forth between different locations.

This is where jmp lists can help. A jmp list is simply a list of locations that you frequent often. Creating and updating them is simple and fast.

Use jmp locations to:

  * keep track of your current task folders (use work, work1, etc.)
  * go to common locations you fequent
  * remember specific paths you don't use often

The jmp list is saved in a file in your home directory named ".jump_list.txt". This way, the jmp list is persisted across logins.

## Step-by-step guide
First, you need to install jmp. This is as simple as adding a couple of script files and editing your .bashrc.

Create a folder for your scripts: mkdir -p ~/bin/
Copy the scripts into this folder. (see below)
Add the following line near the bottom of you .bashrc file: source ~/bin/jmp.sh
You will need to source your .bashrc or log out/in for the changes to take effect.

## Now let's jmp...
#### To add a new item to your jmp list:
hint: adds the cwd (current work directory) using the name of the folder you are currently in

```bash
jmp -a
jmp --add
```

By default, the folder name is used to identify the jmp location. Optionally you may provide your own name.

this version of the commands adds the current path as "myName" to your jmp list.
```bash
jmp -a myName
jmp --add myName
```

#### To list your current jmp locations:

```
jmp -l
jmp --list
```

#### To remove an entry you no longer want or need:
hint: removes the jmp list item "name" from your list

```
jmp -r name
jmp --remove name
```

#### For help from the command line:

```
jmp -h
jmp --help
```
