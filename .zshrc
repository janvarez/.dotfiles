
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/janvarez/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/janvarez/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/janvarez/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/janvarez/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


. "$HOME/.atuin/bin/env"

eval "$(atuin init zsh)"
