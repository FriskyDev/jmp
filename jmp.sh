#!/usr/bin/env bash
 
JMPSCRIPT="${HOME}/bin/jmp.py"
 
function jmp() {
    if [[ ${1} == "-"* ]]; then
        python3 ${JMPSCRIPT} ${@}
        return
    fi
 
    output="$(python3 ${JMPSCRIPT} ${@})"
    if [[ -z "${output}" ]]; then
        if [[ -n "${1}" ]]; then
            echo "err: name '${1}' not in jump list"
        fi
        python3 ${JMPSCRIPT} -l
        false
    elif [[ -d "${output}" ]]; then
        if [ -t 1 ]; then  # if stdout is a terminal, use colors
                echo -e "\\033[34m${output}\\033[0m"
        else
                echo -e "${output}"
        fi
        cd "${output}"
    else
        echo "err: folder '${output}' not found"
        false
    fi
}
 
# this provide tab autocompletion for your jump keys. Tested in bash and zsh
_jmp()
{
    local cur="${COMP_WORDS[COMP_CWORD]}"
    local keys=`awk '{print $1}' ~/.jump_list.txt | tr '[:]' ' ' | grep "^$cur" | tr '\n' ' '`
 
    if [[ ${cur} == * ]] ; then
        COMPREPLY=( $(compgen -W "${keys}" -- ${cur_word}) )
    else
        COMPREPLY=()
    fi
    return 0
}
 
complete -F _jmp jmp
