# Icinga checks

This repos contains the configuration of all icinga checks and is used by both
the icinga master and the icinga client.
Checks configured automatically:
* ceph
* mem
* iostat
* raid
* load
* ssh
* apt
* icinga
* procs
* users

Checks configured manually:
* ipmi: Set ipmi_hosts to a list of dicts, where each entry has the following attributes:
** name: The (icinga'd) name of the host the IPMI belongs to (replace . by \_)
** ip: The IP the IPMI is available on
