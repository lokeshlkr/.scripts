#!/bin/sh

args=($@)
action="$1"
rest="${args[@]:1}"


search(){        
    firefox "https://duckduckgo.com/?q=$rest" 2>/dev/null &
}
browse(){
    if [[ $rest != *"."* ]]; then 
        rest="$rest.com"
    fi
    firefox "https://$rest" 2>/dev/null &
}
sync(){
    if [[ -d ./.git ]] ; then
        git add . && git commit -m "autosync: $rest" && git push origin master && echo -e "\\e[1;32mSync completed.\\e[0;0m"|| echo -e "\\e[1;31mSomething went wrong.\\e[0;0m"
    else
        echo -e "\\e[0;33mNot a git repository.\\e[0;0m"
    fi
}
help(){
    echo -e "\\e[0;34mUsage: s COMMAND [OPTIONS]\\e[1;37m"
    echo -e "\\e[0;32mKnown Commands:\\e[1;37m"
    echo -e "$commands\\e[0;0m"
}
panel(){
    $HOME/working_folder/.scripts/panel/$rest
}
rust(){
    test -d $HOME/working_folder/rust/practice

    if [ $? -eq "0" ]; then
        code $HOME/working_folder/rust/practice
    else
        rustnew
    fi
}
rustnew(){
    cd $HOME/working_folder/rust/
    mv practice "practice_$(date +%Y%m%d_%H%M%S)"
    cargo new practice
    cd practice
    code .
}
vsc(){
    case $rest in
        *"scripts"*)
            code $HOME/working_folder/.scripts ;;
        *"home"*)
            code $HOME ;;
        *"rustnew"*)
            rustnew ;;
        *"rust"*)
            rust ;;
    esac
}
restart(){
    if [[ $rest ]];then
        killall $rest
        sleep 1
        $rest
    else
        echo -e "\\e[0;31mProvide a program to restart.\\e[1;37m"
    fi
}


commands=$(typeset -F | sed s/-f//g | sed s/declare//g)

if [[ (-z "$action") ]]; then
    action="FILLER COMMAND WHEN NO COMMAND IS PROVIDED TO FIX BELOW CASE STATEMENT"
fi

case $commands in
    *"$action"*)
        $action;;
    *)
        help;;
esac