dj-wasabi.telegraf
------------------

Below an overview of all changes in the releases.

Version (Release date)

0.5.1 (2016-08-24)

  * fixed issue with ansible not getting the package #6 (By pull request: thecodeassassin (Thanks!))

0.5.0 (2016-07-17)

  * Removed Test Kitchen tests
  * Added Molecule tests and travis make use of them
  * Updated default version to 1.0.0 beta2
  * Feature/add extra plugins to telegrafd folder #5 (By pull request: stvnwrgs (Thanks!))

0.4.0 (2016-02-05)

  * Fixed test for test-kitchen
  * Added travis-ci test for testing default installation when PR is made
  * Fixed Download url for Debian
  * Removed default entry for telegraf_plugins_extra

0.3.0 (2016-01-13)

  * Made it work with telegraf 0.10.0
  * Default installation: 0.10.0

0.2.0 (2015-11-14)

  * Fixed kitchen test setup
  * Adding "net" to the telegraf_plugins_default property
  * Update etc-opt-telegraf-telegraf.conf.j2 #2 (By pull request: aferrari-technisys (Thanks!))
  * Improvement and upgrade for v0.2.0 of telegraf #1 (By pull request: aferrari-technisys (Thanks!))

0.1.0 (2015-09-23)

  * Updated `telegraf_agent_version` to 0.1.9
  * Added restart when package is changed (When updated for example)
  * Added several plugin options:
    * pass
    * drop
    * tagpass
    * tagdrop
    * interval
  * Updated documentation
  

0.0.2 (2015-09-20)

  * Updated README dus to missing colon
  * Forgot to update the meta file
  * Added Changelog file

0.0.1 (2015-09-20)

  * Initial release
