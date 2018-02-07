#!/bin/bash

log_path="/data4/*"
#script_path="$HOME/codes/my-awk/"
mkdir -p "$HOME/results/d2l_out"
result_path="$HOME/results/d2l_out/"
date_form=2016-01-[0-9]{2}
#date_form="2014-12-02"


for dir in $log_path; do
        if [[ -d $dir && $dir =~ $date_form ]]; then
                new_path="$dir/*"
                month=${dir##*/}
                month=${month%-*}
                mkdir -p "$result_path/$month"
                cd "$result_path/$month"
#               touch $date_name
                date_name=${dir##*/}
                touch $date_name
                echo -n "" > $date_name
                for file in $new_path; do
                        if [[ $file =~ "ssl." ]]; then
                                name_of_file=${file#*.}   #first '.' and left
                #               echo $name_of_file
                                name_of_file=${name_of_file%.*}  #last '.' and right
                #               echo $name_of_file
                                name_of_file=${name_of_file%.*}  #last '.' and right
                                echo -ne $name_of_file"\t" >> $date_name
                                less $file | awk -F"\t" '{print $3} ' >> $date_name
                                echo "done! - $date_name - ${file##*/}"
                        fi
                done
        fi
done
