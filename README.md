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
* power: The configuration format is the same as for ipmi. This is for monitoring the PDUs we have at LEE.
* smart: When adding new hosts, check that your disks are listed in files/chek_smartvalues.{db,cfg}.json, otherwise they won't be recognized and therefore not checked...
* sensors: Set sensors to a list of dicts, where each entry has the following attributes:
** name: How should the sensor be called?
** sensor: The sensor to check. Format `CPU2m1=60,80`, i.e. `sensorname-from-lmsensors=warningtemp,crittemp`. For more options, see check_lm_sensors
* websites: Set websites to a list of dicts, where each entry has the following attributes:
** name: The name of the domain to check
** ssl: Whether to use SSL. Implies checking the certificate for validity.
** addr: IPv4 of the website to test
** ssldays: How long does the certificate need to be valid before printing a warning message(i.e. 30 means warn if the cert is valid for less than 30 days.)
** minsize: How big should the result of GET http[s]://addr be?
** t: how often should we check, e.g. 5m
** Example for SSL: `{"name": "cloud.njsm.de", "ssl": "true", "addr": "85.25.143.246", "ssldays": "30", "minsize": "10000", t: 5m}`
** Example for non-SSL: {"name": "www.whatever.de", "minsize": "1000", "addr": "123.456.789.123", "t": 1m, "ssl": "false"}
