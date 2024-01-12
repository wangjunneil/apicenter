#!/usr/bin/env bash

# color variable
flag_error="\033[31m[-]\033[0m"
flag_succe="\033[32m[+]\033[0m"

cur_dir=$(pwd)
args=$1

clear
echo "+------------------------------------------------------------------------+"
echo "|                          The ApiCenter Script                          |"
echo "+------------------------------------------------------------------------+"
echo "|           For more information please visit https://wangjun.dev        |"
echo "+------------------------------------------------------------------------+"
echo ""

start() {
    nohup python3 app.py 2>&1 & echo $! > pid
    echo -e "${flag_succe} started"
}

stop() {
    kill -9 `cat pid`
    rm -rf pid
    rm -rf nohup.out
    echo -e "${flag_succe} stopped"
}

restart() {
    stop
    start
}

case "${args}" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    *)
        echo -e "Usage: $0 {start|stop|restart}"
        echo
        ;;
esac

exit