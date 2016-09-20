nifty_catkin_build ()
{
    # If arguments are passed to this function, don't summarize the build
    local summarize_cmd
    if [ "$#" -gt 0 ]; then
        summarize_cmd=""
    else
        summarize_cmd="--summarize"
    fi

    # Use the default workspace if available, otherwise do nothing
    local workspace=${ROS_DIR_PATH:-""}
    local workspace_cmd
    if [[ -z "${param// }" ]]; then
        workspace_cmd="-w $workspace"
    else
        workspace_cmd=""
    fi

    # Other commands you want to run by default
    local misc_cmds="-DCMAKE_EXPORT_COMPILE_COMMANDS=ON"

    catkin build $summarize_cmd $workspace_cmd $misc_cmds $@
}

_nifty_catkin_build ()
{
    # from /usr/share/zsh/site-functions/catkin_tools-completion.bash
    catkin_build_opts="--help --dry-run --this --no-deps --unbuilt --start-with-this --continue-on-failure --force-cmake --pre-clean --get-env --verbose --interleave-output --no-status --summarize --no-notify --env-cache --no-env-cache"

    local cur
    COMPREPLY=()
    cur=${COMP_WORDS[COMP_CWORD]}
    case "$cur" in
      -*)
      COMPREPLY=( $( compgen -W "${catkin_build_opts}" -- $cur ) );;
    esac

    return 0
}

complete -F _nifty_catkin_build nifty_catkin_build

alias cb='nifty_catkin_build'
complete -F _nifty_catkin_build cb
alias runtime='rosrun rqt_runtime_monitor rqt_runtime_monitor'
alias testme="catkin run_tests --no-deps --this"
