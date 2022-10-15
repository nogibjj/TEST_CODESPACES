#!bin/bash
#
help(){ 
        echo "Usage:" $0 'filename' 'segsize'
}

listall='list.txt'
declare -i sgesize=100
if [ -z $1 ]; then
        help
        exit 1
else
        listall=$1
fi

if [ -z $2 ]; then
        help
        exit 2
else
        segsize=$2
fi

declare -i listsize=`cat "${listall}" | wc -l`
declare -i segcount=$(( listsize /segsize ))
declare -i segremain=$(( listsize % segsize ))
prefix=${listall%\.*}
postfix=${listall#*\.}
echo '$listall='$listall
echo '$segsize='$segsize
echo '$listsize='$listsize
echo '$segcount='$segcount
echo '$segremain='$segremain

echo '$prefix='$prefix
echo '$postfix=' $postfix

log="${listall}.log"

echo -n '' >  "${log}"

if [ $segcount -gt 0 ]; then
        for i in 'seq 1 $segcount';do
                num_end=$(( i * segsize ))
                num_begin=$(( num_end - segsize + 1))    
                echo ${num_begin} ${num_end} "${prefix}_${i}-${listsize}-${segsize}_${num_begin}-${num_end}.$postfix"
                echo "${prefix}_${i}-${listsize}-${segsize}_${num_begin}-${num_end}.$postfix" >> "${log}"
                head -n ${num_end} "${listall}" | tail -n ${segsize} > "${prefix}_${i}-${listsize}-${segsize}_${num_begin}-${num_end}.$postfix"
        done
fi

if [ $segremain -gt 0 ]; then
        i=$(( i + 1 ))
        num_end=$listsize
        num_begin=$(( num_end - segremain + 1 ))
        echo ${num_begin} ${num_end} "${prefix}_${i}-${listsize}-${segsize}_${num_begin}-${num_end}.$postfix"
        echo "${prefix}_${i}-${listsize}-${segsize}_${num_begin}-${num_end}.$postfix" >> "${log}"
        head -n ${num_end}  "${listall}"  | tail -n ${segremain} > "${prefix}_${i}-${listsize}-${segsize}_${num_begin}-${num_end}.$postfix" 
fi