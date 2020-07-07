#! /bin/sh

[ ! -z $1 ] || exit 1;

is_active=$(systemctl is-active "$1");
echo "$is_active"

if [ "$is_active" == active ]; then
	exit 0;
else
	exit 1;
fi
