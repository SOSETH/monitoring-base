#! /bin/bash

[ -n "$2" ] || exit 1;

is_active=$(systemctl is-active "$2");
echo "$2 is $is_active on $(hostname)"

if [ "$is_active" == active ]; then
	exit 0;
else
	exit 1;
fi
