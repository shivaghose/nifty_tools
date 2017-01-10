# Show hidden files
#   This function also lets you pass in other args as well to the `ls` call
#   Common additional args are:
#
show_hidden()
{
    # List all the elements in a single column without color and grep
    ls -a1 --color=never "$@" | grep '^\.';
}

# Show the symlinks in a directory
show_symlinks()
{
    ls -l `find ./ -maxdepth 1 -type l -print`
}

