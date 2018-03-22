#!/usr/bin/env sh
JMPSCRIPT="${HOME}/bin/jmp.py"
jmp() {
    if [[ ${1} == "-"* ]]; then
        python3 ${JMPSCRIPT} ${@}
        return
    fi
 
    output="$(python3 ${JMPSCRIPT} ${@})"
    if [[ -z "${output}" ]]; then
        echo "err: name '${1}' not in jump list"
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
