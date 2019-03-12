# dj-wasabi.telegraf

## Build status:

[![Build Status](https://travis-ci.org/dj-wasabi/ansible-telegraf.svg?branch=master)](https://travis-ci.org/dj-wasabi/ansible-telegraf)

This role will install and configure telegraf.

Telegraf is an agent written in Go for collecting metrics from the system it's running on, or from other services, and writing them into InfluxDB.

Design goals are to have a minimal memory footprint with a plugin system so that developers in the community can easily add support for collecting metrics from well known services (like Hadoop, Postgres, or Redis) and third party APIs (like Mailchimp, AWS CloudWatch, or Google Analytics).

(https://github.com/influxdb/telegraf)

## Requirements

### Supported systems
This role supports the following systems:

 * Red Hat
 * Debian
 * Ubuntu
 * Docker container
 * Windows (Best effort)
 * (Open)Suse

So, you'll need one of those systems.. :-)
Please sent Pull Requests or suggestions when you want to use this role for other systems.

### InfluxDB

You'll need an InfluxDB instance running somewhere on your network. Or 1 of the other output types found on https://github.com/influxdata/telegraf/#output-plugins

### Docker

Docker needs to be installed on the target host. I can recommend these roles to install Docker:

* [jgeusebroek.docker](https://galaxy.ansible.com/jgeusebroek/docker)
* [geerlingguy.docker](https://galaxy.ansible.com/geerlingguy/docker)

This is only the case when the configuration is needed for a Telegraf inside a Docker container (When `telegraf_agent_docker: True`).

## Upgrade
### 0.7.0

There was an issue:

    If I configure a telegraf_plugins_extra, run ansible, delete the plugin and run ansible again, the plugin stays on the machine.

## Role Variables

### Ansible role specific variables

Specifying the version to be installed:

* `telegraf_agent_version`: The version of Telegraf to install. Default: `1.10.0`

How `Telegraf` needs to be installed. There are 3 methods in getting `Telegraf` installed on the target host:

* Via the package manager, like `yum`, `apt` or `zypper` ("repo");
* Via a download from the `https://dl.influxdata.com/` site ("online");
* Already provided and is already available on the target host, but not yet installed/configured ("offline");

This can be configured by setting `telegraf_agent_package_method` to one of the appropriate values ( `repo`, `online` or `offline`).

#### Telegraf Package

These properties set in how and what package will be installed.

* `telegraf_agent_package`: The name of the Telegraf package to install. When `telegraf_agent_package_method` is set to `online` or `offline`, it needs to have the full path of the file. Example: `telegraf_agent_package: /tmp/telegraf.rpm`. Default: `telegraf_agent_package: telegraf`.
* `telegraf_agent_package_method`: The installation method to be used. Can choose between: `repo`, `offline` or `online`.
* `telegraf_agent_package_state`: If the package should be `present` or `latest`. When set to `latest`, `telegraf_agent_version` will be ignored. Default: `present`

### Telegraf agent process configuration.

* `telegraf_agent_interval`: The interval configured for sending data to the server. Default: `10`
* `telegraf_agent_debug`: Run Telegraf in debug mode. Default: `False`
* `telegraf_agent_round_interval`: Rounds collection interval to 'interval' Default: True
* `telegraf_agent_flush_interval`: Default data flushing interval for all outputs. Default: 10
* `telegraf_agent_flush_jitter`: Jitter the flush interval by a random amount. Default: 0
* `telegraf_agent_aws_tags`: Configure AWS ec2 tags into Telegraf tags section Default: `False`
* `telegraf_agent_aws_tags_prefix`: Define a prefix for AWS ec2 tags. Default: `""`
* `telegraf_agent_collection_jitter`: Jitter the collection by a random amount. Default: 0 (since v0.13)
* `telegraf_agent_metric_batch_size`: The agent metric batch size. Default: 1000  (since v0.13)
* `telegraf_agent_metric_buffer_limit`: The agent metric buffer limit. Default: 10000  (since v0.13)
* `telegraf_agent_quiet`: Run Telegraf in quiet mode (error messages only). Default: `False` (since v0.13)
* `telegraf_agent_logfile`: The agent logfile name. Default: '' (means to log to stdout) (since v1.1)
* `telegraf_agent_omit_hostname`: Do no set the "host" tag in the agent. Default: `False` (since v1.1)

### Docker specific role variables:

* `telegraf_agent_docker`: Install Telegraf as a docker container. Default: `False`
* `telegraf_agent_docker_name`: Name of the docker container. Default: `telegraf`
* `telegraf_agent_docker_network_mode`: Networking mode of the docker container. Default: `bridge`
* `telegraf_agent_docker_restart_policy`: Docker container restart policy. Default: `unless-stopped`
* `telegraf_uid_docker`: Override user id. Default: `995`
* `telegraf_gid_docker`: Override group id. Default: `998`

Full agent settings reference: [https://github.com/influxdata/telegraf/blob/master/docs/CONFIGURATION.md#agent-configuration](https://github.com/influxdata/telegraf/blob/master/docs/CONFIGURATION.md#agent-configuration).

## Extra information
### Setting tags

You can set tags for the host running telegraf:

	telegraf_global_tags:
	  - tag_name: some_name
	    tag_value: some_value

Specifying an output. The default is set to localhost, you'll have to specify the correct influxdb server:

	telegraf_agent_output:
	  - type: influxdb
	    config:
	      - urls = ["http://localhost:8086"]
	      - database = "telegraf"
        tagpass:
          - cpu = ["cpu0"]

The config will be printed line by line into the configuration, so you could also use:

	config:
		- # Print an documentation line

and it will be printed in the configuration file.

### Docker specifics

#### Docker image

The official [Influxdata Telegraf image](https://hub.docker.com/_/telegraf) is used. 	`telegraf_agent_version` will translate to the image tag.

#### Docker mounts

Please note that the Docker container bind mounts basicly your whole system (read-only) to monitor the Docker Engine Host from within the container. To be precise:

	- /etc/telegraf:/etc/telegraf:ro
	- /:/hostfs:ro
	- /etc:/hostfs/etc:ro
	- /proc:/hostfs/proc:ro
	- /sys:/hostfs/sys:ro
	- /var/run:/var/run:ro

More information: [https://github.com/influxdata/telegraf/blob/master/docs/FAQ.md](https://github.com/influxdata/telegraf/blob/master/docs/FAQ.md).

#### Example Docker configuration

	telegraf_agent_docker: True
	# Force host networking mode, so Docker Engine Host traffic metrics can be gathered.
	telegraf_agent_docker_network_mode: host
	# Force a specific image tag.
	telegraf_agent_version: 1.10.0-alpine

	telegraf_plugins_default:
	  - plugin: cpu
	    config:
	      - percpu = "true"
	  - plugin: disk
	    tags:
	      - diskmetrics = "true"
	    tagpass:
	      - fstype = [ "ext4", "xfs" ]
	    tagdrop:
	      - path = [ "/etc", "/etc/telegraf", "/etc/hostname", "/etc/hosts", "/etc/resolv.conf" ]
	  - plugin: io
	  - plugin: mem
	  - plugin: system
	  - plugin: swap
	  - plugin: netstat
	  - plugin: processes
	  - plugin: docker
	    config:
	      - endpoint = "unix:///var/run/docker.sock"
	      - timeout = "5s"

## Windows specific Variables

**NOTE**

_Supporting Windows is an best effort (I don't have the possibility to either test/verify changes on the various amount of available Windows instances). PR's specific to Windows will almost immediately be merged, unless some one is able to provide a Windows test mechanism via Travis or other service for Pull Requests._

* `telegraf_win_install_dir`: The directory where Telegraf will be installed.
* `telegraf_win_logfile`: The location to the logfile of Telegraf.
* `telegraf_win_include`: The directory that will contain all plugin configuration.

## Extra information

There are two properties which are similar, but are used differently. Those are:

* `telegraf_plugins_default`
* `telegraf_plugins_extra`

With the property `telegraf_plugins_default` it is set to use the default set of Telegraf plugins. You could override it with more plugins, which should be enabled at default.

	telegraf_plugins_default:
	  - plugin: cpu
	    config:
	      - percpu = true
	  - plugin: disk
	  - plugin: io
	  - plugin: mem
	  - plugin: system
	  - plugin: swap
	  - plugin: netstat

Every telegraf agent has these as a default configuration.

The 2nd parameter `telegraf_plugins_extra` can be used to add plugins specific to the servers goal. It is a hash instead of a list, so that you can merge values from multiple var files together. Following is an example for using this parameter for MySQL database servers:

	cat group_vars/mysql_database
	telegraf_plugins_extra:
		mysql:
		  config:
		  	- servers = ["root:{{ mysql_root_password }}@tcp(localhost:3306)/"]

There is an option to delete extra-plugin files in /etc/telegraf/telegraf.d if they weren't generated by this playbook with `telegraf_plugins_extra_exclusive` variable.

Telegraf plugin options:

* `tags` An k/v tags to apply to a specific input's measurements. Can be used on any stage for better filtering for example in outputs.
* `tagpass`: (added in Telegraf 0.1.5) tag names and arrays of strings that are used to filter metrics by the current plugin. Each string in the array is tested as an exact match against the tag name, and if it matches the metric is emitted.
* `tagdrop`: (added in Telegraf 0.1.5) The inverse of tagpass. If a tag matches, the metric is not emitted. This is tested on metrics that have passed the tagpass test.
* `interval`: How often to gather this metric. Normal plugins use a single global interval, but if one particular plugin should be run less or more often, you can configure that here.

An example might look like this:

	telegraf_plugins_default:
	  - plugin: disk
	    interval: 12
        tags:
          - diskmetrics = "true"
	    tagpass:
	      - fstype = [ "ext4", "xfs" ]
    	  - path = [ "/opt", "/home" ]

If you want to define processors you can simply use `telegraf_processors` variable.  
An example might look like this:
```
telegraf_processors: 
  - processor: rename
  - processor: rename.replace  
    config:
        - tag = "level"
        - dest = "LogLevel"
```

## Dependencies

No dependencies

## Example Playbook

    - hosts: servers
      roles:
         - { role: dj-wasabi.telegraf }

## Contributors

The following have contributed to this Ansible role (Provided with: `git shortlog -s -n`):

* Werner Dijkerman
* Thomas Szymanski
* Jeroen Geusebroek
* or
* Alejandro
* Troy Jendra
* Slawomir Skowron
* gaelL
* Laurent Hoss
* Ismael
* Anthony ARNAUD
* Ilkka Tengvall
* Rick Box
* Steven Wirges
* Jack Ivy
* Emerson Knapp
* zend0
* Angristan
* Miroslav Prasil
* Olivier Boukili
* Pascal
* Romain BUREAU
* Ryan Conway
* Steve Durrheimer
* TheCodeAssassin
* aroglian

Thank you all!

## Molecule

This roles is configured to be tested with Molecule. You can find on this page some more information regarding Molecule: https://werner-dijkerman.nl/2016/07/10/testing-ansible-roles-with-molecule-testinfra-and-docker/

## License

BSD

## Author Information

Please let me know if you have issues. Pull requests are also accepted! :-)

mail: ikben [ at ] werner-dijkerman . nl
