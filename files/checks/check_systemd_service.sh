#!/bin/bash

[ -n "$2" ] || exit 3;

is_active=$(systemctl is-active "$2");

if [ "$is_active" == active ]; then
	echo "SYSTEMD OK: $2 is $is_active on $(hostname)"
	exit 0;
else
	echo "SYSTEMD CRITICAL: $2 is $is_active on $(hostname)"
	exit 2;
fi
