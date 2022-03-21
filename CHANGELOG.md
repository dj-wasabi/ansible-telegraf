# Changelog

## [Unreleased](https://github.com/dj-wasabi/ansible-telegraf/tree/HEAD)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.13.2...HEAD)

**Implemented enhancements:**

- Adding support for aggregators [\#156](https://github.com/dj-wasabi/ansible-telegraf/pull/156) ([simo-tuomisto](https://github.com/simo-tuomisto))
- Add support for Rocky Linux [\#147](https://github.com/dj-wasabi/ansible-telegraf/pull/147) ([maxwondercorn](https://github.com/maxwondercorn))
- Add Windows feature of upgrade agents [\#146](https://github.com/dj-wasabi/ansible-telegraf/pull/146) ([PeterSzegedi](https://github.com/PeterSzegedi))

**Merged pull requests:**

- Improve usage on SUSE releases [\#155](https://github.com/dj-wasabi/ansible-telegraf/pull/155) ([jeffmahoney](https://github.com/jeffmahoney))
- Add variable for openSUSE RPM repository [\#151](https://github.com/dj-wasabi/ansible-telegraf/pull/151) ([kingphil](https://github.com/kingphil))
- Fixed issues with Windows paths containing spaces & removed redundant "telegraf" folder in path [\#144](https://github.com/dj-wasabi/ansible-telegraf/pull/144) ([treanorjp](https://github.com/treanorjp))

## [0.13.2](https://github.com/dj-wasabi/ansible-telegraf/tree/0.13.2) (2021-03-05)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.13.1...0.13.2)

**Implemented enhancements:**

- Remove telegraf repository after switching to online method [\#142](https://github.com/dj-wasabi/ansible-telegraf/pull/142) ([djerfy](https://github.com/djerfy))

**Merged pull requests:**

- Fix spacing for telegraf\_plugins\_extra example in readme.md [\#143](https://github.com/dj-wasabi/ansible-telegraf/pull/143) ([isclever](https://github.com/isclever))

## [0.13.1](https://github.com/dj-wasabi/ansible-telegraf/tree/0.13.1) (2021-01-06)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.13.0...0.13.1)

**Implemented enhancements:**

- Added GH Action to automatically update CHANGELOG.md [\#141](https://github.com/dj-wasabi/ansible-telegraf/pull/141) ([dj-wasabi](https://github.com/dj-wasabi))

**Fixed bugs:**

- adjustments for Windows \>= 1.15 [\#139](https://github.com/dj-wasabi/ansible-telegraf/pull/139) ([billabongrob](https://github.com/billabongrob))

**Closed issues:**

- Newer versions of Telegraf fail on Windows [\#138](https://github.com/dj-wasabi/ansible-telegraf/issues/138)

**Merged pull requests:**

- Added property telegraf\_agent\_docker\_image\_version for using a specific version of the Docker image [\#137](https://github.com/dj-wasabi/ansible-telegraf/pull/137) ([dj-wasabi](https://github.com/dj-wasabi))
- Apply ansible-lint in pre-commit hook and fix changes [\#136](https://github.com/dj-wasabi/ansible-telegraf/pull/136) ([dj-wasabi](https://github.com/dj-wasabi))
- Using version as version\_compare is deprecated [\#135](https://github.com/dj-wasabi/ansible-telegraf/pull/135) ([dj-wasabi](https://github.com/dj-wasabi))
- Using command instead of shell module [\#134](https://github.com/dj-wasabi/ansible-telegraf/pull/134) ([dj-wasabi](https://github.com/dj-wasabi))

## [0.13.0](https://github.com/dj-wasabi/ansible-telegraf/tree/0.13.0) (2020-10-16)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.12.0...0.13.0)

**Implemented enhancements:**

- Setup the system for individual plugins [\#125](https://github.com/dj-wasabi/ansible-telegraf/issues/125)
- Logparser configuration [\#111](https://github.com/dj-wasabi/ansible-telegraf/issues/111)
- ansible\_fqdn problematic for getting hostname [\#105](https://github.com/dj-wasabi/ansible-telegraf/issues/105)
- FreeBSD support [\#99](https://github.com/dj-wasabi/ansible-telegraf/issues/99)
- Proxy not taken into consideration when using 'online' [\#96](https://github.com/dj-wasabi/ansible-telegraf/issues/96)

**Closed issues:**

- telegraf\_agent\_aws\_tags creates an invalid Telegraf configuration [\#128](https://github.com/dj-wasabi/ansible-telegraf/issues/128)
- Broken on Ubuntu 20.04 [\#121](https://github.com/dj-wasabi/ansible-telegraf/issues/121)
- Broken on RedHat [\#119](https://github.com/dj-wasabi/ansible-telegraf/issues/119)

**Merged pull requests:**

- corrected "Example Docker configuration" to make it work by default [\#132](https://github.com/dj-wasabi/ansible-telegraf/pull/132) ([NotDead](https://github.com/NotDead))
- Removing requirements file and use it from ci-base repo [\#131](https://github.com/dj-wasabi/ansible-telegraf/pull/131) ([dj-wasabi](https://github.com/dj-wasabi))
- Going to Github Actions [\#130](https://github.com/dj-wasabi/ansible-telegraf/pull/130) ([dj-wasabi](https://github.com/dj-wasabi))
- quote aws ec2 global tags [\#129](https://github.com/dj-wasabi/ansible-telegraf/pull/129) ([Puneeth-n](https://github.com/Puneeth-n))
- made service status configurable [\#127](https://github.com/dj-wasabi/ansible-telegraf/pull/127) ([DEvil0000](https://github.com/DEvil0000))
- Plugin dependencies are installed and configured [\#126](https://github.com/dj-wasabi/ansible-telegraf/pull/126) ([carlba](https://github.com/carlba))
- fix debian packagename on state latest [\#124](https://github.com/dj-wasabi/ansible-telegraf/pull/124) ([dwerder](https://github.com/dwerder))
- MacOS support [\#123](https://github.com/dj-wasabi/ansible-telegraf/pull/123) ([carlba](https://github.com/carlba))
- gpgkey yum repo fix [\#122](https://github.com/dj-wasabi/ansible-telegraf/pull/122) ([marcinwito](https://github.com/marcinwito))
- Fix RedHat task list [\#120](https://github.com/dj-wasabi/ansible-telegraf/pull/120) ([rohit-gohri](https://github.com/rohit-gohri))
- added installation method manual - skip installation [\#117](https://github.com/dj-wasabi/ansible-telegraf/pull/117) ([DEvil0000](https://github.com/DEvil0000))
- Support postgresql\_extensible queries [\#116](https://github.com/dj-wasabi/ansible-telegraf/pull/116) ([rlex](https://github.com/rlex))
- Added extra filtering possibilities for a plugin [\#113](https://github.com/dj-wasabi/ansible-telegraf/pull/113) ([dj-wasabi](https://github.com/dj-wasabi))
- Minor changes to get Travis working again [\#112](https://github.com/dj-wasabi/ansible-telegraf/pull/112) ([dj-wasabi](https://github.com/dj-wasabi))
- Download from influxdb [\#109](https://github.com/dj-wasabi/ansible-telegraf/pull/109) ([dj-wasabi](https://github.com/dj-wasabi))
- Don't override package name unless "latest" [\#108](https://github.com/dj-wasabi/ansible-telegraf/pull/108) ([matttrach](https://github.com/matttrach))
- Adding support for arm64 systems [\#106](https://github.com/dj-wasabi/ansible-telegraf/pull/106) ([remkade](https://github.com/remkade))
- Use items\(\) instead of iteritems\(\) [\#104](https://github.com/dj-wasabi/ansible-telegraf/pull/104) ([diego1q2w](https://github.com/diego1q2w))
- Fix: ensure apt-cache is updated before install [\#103](https://github.com/dj-wasabi/ansible-telegraf/pull/103) ([asfaltboy](https://github.com/asfaltboy))
- on FreeBSD the telegeraf.conf is in root of /usr/local/etc. [\#102](https://github.com/dj-wasabi/ansible-telegraf/pull/102) ([langerma](https://github.com/langerma))
- Some changes for fixing FreeBSD [\#101](https://github.com/dj-wasabi/ansible-telegraf/pull/101) ([dj-wasabi](https://github.com/dj-wasabi))
- basic FreeBSD support [\#100](https://github.com/dj-wasabi/ansible-telegraf/pull/100) ([langerma](https://github.com/langerma))
- Added the use\_proxy argument to use a proxy \(or not\) [\#98](https://github.com/dj-wasabi/ansible-telegraf/pull/98) ([dj-wasabi](https://github.com/dj-wasabi))
- Various small changes for molecule [\#97](https://github.com/dj-wasabi/ansible-telegraf/pull/97) ([dj-wasabi](https://github.com/dj-wasabi))

## [0.12.0](https://github.com/dj-wasabi/ansible-telegraf/tree/0.12.0) (2019-03-12)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.11.0...0.12.0)

**Implemented enhancements:**

- Install telegraf from package file instead of repository [\#89](https://github.com/dj-wasabi/ansible-telegraf/issues/89)

**Closed issues:**

- Docker container support [\#82](https://github.com/dj-wasabi/ansible-telegraf/issues/82)

**Merged pull requests:**

- Add processors section in Telegraf config [\#94](https://github.com/dj-wasabi/ansible-telegraf/pull/94) ([ph4r5h4d](https://github.com/ph4r5h4d))
- Updated to Telegraf 1.10.0;Different installation methods [\#93](https://github.com/dj-wasabi/ansible-telegraf/pull/93) ([dj-wasabi](https://github.com/dj-wasabi))
- Updating Telegraf default to 1.9.5 [\#92](https://github.com/dj-wasabi/ansible-telegraf/pull/92) ([sdurrheimer](https://github.com/sdurrheimer))
- Updating Telegraf default to 1.9.4 [\#90](https://github.com/dj-wasabi/ansible-telegraf/pull/90) ([sdurrheimer](https://github.com/sdurrheimer))
- Docker enhancements [\#88](https://github.com/dj-wasabi/ansible-telegraf/pull/88) ([jgeusebroek](https://github.com/jgeusebroek))
- Updating Telegraf default to 1.9.3 [\#87](https://github.com/dj-wasabi/ansible-telegraf/pull/87) ([sdurrheimer](https://github.com/sdurrheimer))
- Added register for installation of packages [\#86](https://github.com/dj-wasabi/ansible-telegraf/pull/86) ([dj-wasabi](https://github.com/dj-wasabi))
- Add Docker container support [\#85](https://github.com/dj-wasabi/ansible-telegraf/pull/85) ([jgeusebroek](https://github.com/jgeusebroek))
- Remove legacy options [\#84](https://github.com/dj-wasabi/ansible-telegraf/pull/84) ([jgeusebroek](https://github.com/jgeusebroek))
- Fix tagpass and tagdrop [\#83](https://github.com/dj-wasabi/ansible-telegraf/pull/83) ([jgeusebroek](https://github.com/jgeusebroek))
- \[bug\] debian - add cache\_valid\_time [\#81](https://github.com/dj-wasabi/ansible-telegraf/pull/81) ([pad92](https://github.com/pad92))
- Updating Telegraf default to 1.9.2 [\#80](https://github.com/dj-wasabi/ansible-telegraf/pull/80) ([sdurrheimer](https://github.com/sdurrheimer))
- Add Yum repo support for Amazon Linux [\#79](https://github.com/dj-wasabi/ansible-telegraf/pull/79) ([anthonysr](https://github.com/anthonysr))
- Fix to work with Fedora Linux [\#78](https://github.com/dj-wasabi/ansible-telegraf/pull/78) ([ikke-t](https://github.com/ikke-t))
- Updating to newer version of Telegraf [\#77](https://github.com/dj-wasabi/ansible-telegraf/pull/77) ([dj-wasabi](https://github.com/dj-wasabi))
- Add support for extra win\_perf\_counters and prevent python u'' strings [\#76](https://github.com/dj-wasabi/ansible-telegraf/pull/76) ([jdivy](https://github.com/jdivy))

## [0.11.0](https://github.com/dj-wasabi/ansible-telegraf/tree/0.11.0) (2018-12-11)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.10.0...0.11.0)

**Closed issues:**

- No telegraf\_plugin\_extra info is added to plugins [\#71](https://github.com/dj-wasabi/ansible-telegraf/issues/71)
- Daemon crash because of empty config.conf and plugin.conf files. [\#63](https://github.com/dj-wasabi/ansible-telegraf/issues/63)
- Pin telegraf to {present, latest, specific-version} [\#59](https://github.com/dj-wasabi/ansible-telegraf/issues/59)
- Ability to add multiple times the same extra-plugin [\#57](https://github.com/dj-wasabi/ansible-telegraf/issues/57)

**Merged pull requests:**

- Renamed the tojson to to\_json [\#74](https://github.com/dj-wasabi/ansible-telegraf/pull/74) ([dj-wasabi](https://github.com/dj-wasabi))
- A few enhancements and fixes to windows support [\#73](https://github.com/dj-wasabi/ansible-telegraf/pull/73) ([jdivy](https://github.com/jdivy))
- Replace 'ec2\_facts' with 'ec2\_metadata\_facts' to fix a deprecation warning [\#72](https://github.com/dj-wasabi/ansible-telegraf/pull/72) ([Rylon](https://github.com/Rylon))
- Added default pluging if nothing is configured [\#70](https://github.com/dj-wasabi/ansible-telegraf/pull/70) ([dj-wasabi](https://github.com/dj-wasabi))
- Added support for \(Open\)Suse [\#69](https://github.com/dj-wasabi/ansible-telegraf/pull/69) ([dj-wasabi](https://github.com/dj-wasabi))
- Added Windows as OS [\#68](https://github.com/dj-wasabi/ansible-telegraf/pull/68) ([dj-wasabi](https://github.com/dj-wasabi))
- Want to use latest [\#67](https://github.com/dj-wasabi/ansible-telegraf/pull/67) ([dj-wasabi](https://github.com/dj-wasabi))
- Some small improvements [\#66](https://github.com/dj-wasabi/ansible-telegraf/pull/66) ([dj-wasabi](https://github.com/dj-wasabi))
- telegraf-extra-plugin.conf.j2: fix template typo [\#65](https://github.com/dj-wasabi/ansible-telegraf/pull/65) ([gaelL](https://github.com/gaelL))
- Using base ci requirements.txt [\#64](https://github.com/dj-wasabi/ansible-telegraf/pull/64) ([dj-wasabi](https://github.com/dj-wasabi))
- Wen copying/removing plugins show only plugin name [\#62](https://github.com/dj-wasabi/ansible-telegraf/pull/62) ([mprasil](https://github.com/mprasil))
- Pin apt key ID [\#61](https://github.com/dj-wasabi/ansible-telegraf/pull/61) ([tszym](https://github.com/tszym))
- Added support for plugins being managed exclusively by this playbook [\#60](https://github.com/dj-wasabi/ansible-telegraf/pull/60) ([gaizeror](https://github.com/gaizeror))

## [0.10.0](https://github.com/dj-wasabi/ansible-telegraf/tree/0.10.0) (2018-08-12)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.9.0...0.10.0)

**Closed issues:**

- Package changed namespace and broke our Tower instance [\#56](https://github.com/dj-wasabi/ansible-telegraf/issues/56)
- PR \#46 break telegraf "Multiple inputs of the same type" [\#48](https://github.com/dj-wasabi/ansible-telegraf/issues/48)
- telegraf\_plugins\_extra is override when multiple call [\#30](https://github.com/dj-wasabi/ansible-telegraf/issues/30)

**Merged pull requests:**

- Updating to Telegraf 1.7.3;Updating changelog [\#58](https://github.com/dj-wasabi/ansible-telegraf/pull/58) ([dj-wasabi](https://github.com/dj-wasabi))
- Added bunch of files [\#55](https://github.com/dj-wasabi/ansible-telegraf/pull/55) ([dj-wasabi](https://github.com/dj-wasabi))
- Fix Deprecation warnings [\#54](https://github.com/dj-wasabi/ansible-telegraf/pull/54) ([dj-wasabi](https://github.com/dj-wasabi))
- Changed 'include' to 'include\_tasks' to remove deprecation warning [\#53](https://github.com/dj-wasabi/ansible-telegraf/pull/53) ([tjend](https://github.com/tjend))
- Add option to remove extra plugin config files [\#52](https://github.com/dj-wasabi/ansible-telegraf/pull/52) ([tjend](https://github.com/tjend))
- Plugins extra hash allow multiple inputs same type [\#50](https://github.com/dj-wasabi/ansible-telegraf/pull/50) ([tjend](https://github.com/tjend))
- Update to 2.4;Using specific versions of libraries [\#49](https://github.com/dj-wasabi/ansible-telegraf/pull/49) ([dj-wasabi](https://github.com/dj-wasabi))

## [0.9.0](https://github.com/dj-wasabi/ansible-telegraf/tree/0.9.0) (2018-05-06)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.8.0...0.9.0)

**Closed issues:**

- Cannot call plugin multiple times anymore [\#39](https://github.com/dj-wasabi/ansible-telegraf/issues/39)

**Merged pull requests:**

- Updating to 0.9.0 [\#47](https://github.com/dj-wasabi/ansible-telegraf/pull/47) ([dj-wasabi](https://github.com/dj-wasabi))
- Convert the telegraf\_plugins\_extra varaible to a hash so that we can … [\#46](https://github.com/dj-wasabi/ansible-telegraf/pull/46) ([tjend](https://github.com/tjend))
- Improved comments, split up role, moved tags and added defaults [\#45](https://github.com/dj-wasabi/ansible-telegraf/pull/45) ([boxrick](https://github.com/boxrick))
- Allow to override RedHat release version [\#43](https://github.com/dj-wasabi/ansible-telegraf/pull/43) ([tszym](https://github.com/tszym))
- Fix Travis Tests [\#42](https://github.com/dj-wasabi/ansible-telegraf/pull/42) ([dj-wasabi](https://github.com/dj-wasabi))
- Fix markdown [\#41](https://github.com/dj-wasabi/ansible-telegraf/pull/41) ([angristan](https://github.com/angristan))
- plugins: be able to specify the filename of extra plugings [\#40](https://github.com/dj-wasabi/ansible-telegraf/pull/40) ([gaelL](https://github.com/gaelL))
- tags: give an option to use AWS tags as telegraf tags [\#32](https://github.com/dj-wasabi/ansible-telegraf/pull/32) ([gaelL](https://github.com/gaelL))

## [0.8.0](https://github.com/dj-wasabi/ansible-telegraf/tree/0.8.0) (2017-10-30)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.7.0...0.8.0)

**Closed issues:**

- PIP dependencies conflicting with native yum packages [\#28](https://github.com/dj-wasabi/ansible-telegraf/issues/28)

**Merged pull requests:**

- Use telegra\_global\_tags for oldest telegraf versions [\#38](https://github.com/dj-wasabi/ansible-telegraf/pull/38) ([tszym](https://github.com/tszym))
-  Fix extra plugins by file  /  Change apt source filename / Change tags by global\_tags  [\#37](https://github.com/dj-wasabi/ansible-telegraf/pull/37) ([aarnaud](https://github.com/aarnaud))
- Remove useless packages on RedHat. fix \#28 [\#36](https://github.com/dj-wasabi/ansible-telegraf/pull/36) ([tszym](https://github.com/tszym))
- Test if LSB codename exists before using it [\#35](https://github.com/dj-wasabi/ansible-telegraf/pull/35) ([tszym](https://github.com/tszym))
- Updating to Molecule V2 [\#31](https://github.com/dj-wasabi/ansible-telegraf/pull/31) ([dj-wasabi](https://github.com/dj-wasabi))

## [0.7.0](https://github.com/dj-wasabi/ansible-telegraf/tree/0.7.0) (2017-02-23)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.6.0...0.7.0)

**Fixed bugs:**

- multiple plugins in telegraf\_plugins\_extra are duplicated [\#22](https://github.com/dj-wasabi/ansible-telegraf/issues/22)
- Deleting extra plugins doesn't delete them [\#8](https://github.com/dj-wasabi/ansible-telegraf/issues/8)

**Merged pull requests:**

- Updating to release 0.7.0 [\#27](https://github.com/dj-wasabi/ansible-telegraf/pull/27) ([dj-wasabi](https://github.com/dj-wasabi))
- Replace action by modules [\#26](https://github.com/dj-wasabi/ansible-telegraf/pull/26) ([tszym](https://github.com/tszym))
- Use yum repository to install telegraf on RedHat [\#25](https://github.com/dj-wasabi/ansible-telegraf/pull/25) ([tszym](https://github.com/tszym))
- Remove for-loop in extra-plugin template [\#24](https://github.com/dj-wasabi/ansible-telegraf/pull/24) ([emersondispatch](https://github.com/emersondispatch))
- Update Debian.yml [\#23](https://github.com/dj-wasabi/ansible-telegraf/pull/23) ([zend0](https://github.com/zend0))
- extra plugins tags [\#21](https://github.com/dj-wasabi/ansible-telegraf/pull/21) ([oboukili](https://github.com/oboukili))
- Input tags support [\#20](https://github.com/dj-wasabi/ansible-telegraf/pull/20) ([szibis](https://github.com/szibis))
- Fix telegraf confguration permissions [\#19](https://github.com/dj-wasabi/ansible-telegraf/pull/19) ([szibis](https://github.com/szibis))

## [0.6.0](https://github.com/dj-wasabi/ansible-telegraf/tree/0.6.0) (2017-01-02)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.5.1...0.6.0)

**Merged pull requests:**

- update the README with the latest v0.13 - v1.1 agent settings [\#17](https://github.com/dj-wasabi/ansible-telegraf/pull/17) ([lhoss](https://github.com/lhoss))
- support missing agent settings upto telegraf v1.1 [\#16](https://github.com/dj-wasabi/ansible-telegraf/pull/16) ([lhoss](https://github.com/lhoss))
- Fixing molecule [\#15](https://github.com/dj-wasabi/ansible-telegraf/pull/15) ([dj-wasabi](https://github.com/dj-wasabi))
- use version\_compare filter … [\#14](https://github.com/dj-wasabi/ansible-telegraf/pull/14) ([lhoss](https://github.com/lhoss))
- set telegraf hostname in defaults. [\#13](https://github.com/dj-wasabi/ansible-telegraf/pull/13) ([airbe](https://github.com/airbe))
- Removed imports [\#12](https://github.com/dj-wasabi/ansible-telegraf/pull/12) ([dj-wasabi](https://github.com/dj-wasabi))
- Fix the Influxdb repo for "hybrid" debian distros \(like "jessie/sid"\) [\#11](https://github.com/dj-wasabi/ansible-telegraf/pull/11) ([Ismael](https://github.com/Ismael))
- Do "become" for the steps that require root access on Debian [\#10](https://github.com/dj-wasabi/ansible-telegraf/pull/10) ([Ismael](https://github.com/Ismael))
- Added new code for correct molecule verification [\#7](https://github.com/dj-wasabi/ansible-telegraf/pull/7) ([dj-wasabi](https://github.com/dj-wasabi))

## [0.5.1](https://github.com/dj-wasabi/ansible-telegraf/tree/0.5.1) (2016-08-24)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.5.0...0.5.1)

**Merged pull requests:**

- fixed issue with ansible not getting the package [\#6](https://github.com/dj-wasabi/ansible-telegraf/pull/6) ([thecodeassassin](https://github.com/thecodeassassin))

## [0.5.0](https://github.com/dj-wasabi/ansible-telegraf/tree/0.5.0) (2016-07-17)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.4.0...0.5.0)

**Closed issues:**

- A new Release for the .deb package url change [\#3](https://github.com/dj-wasabi/ansible-telegraf/issues/3)

**Merged pull requests:**

- Feature/add extra plugins to telegrafd folder [\#5](https://github.com/dj-wasabi/ansible-telegraf/pull/5) ([stvnwrgs](https://github.com/stvnwrgs))

## [0.4.0](https://github.com/dj-wasabi/ansible-telegraf/tree/0.4.0) (2016-02-05)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.3.0...0.4.0)

## [0.3.0](https://github.com/dj-wasabi/ansible-telegraf/tree/0.3.0) (2016-01-13)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.2.0...0.3.0)

## [0.2.0](https://github.com/dj-wasabi/ansible-telegraf/tree/0.2.0) (2015-11-14)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.1.0...0.2.0)

**Merged pull requests:**

- Update etc-opt-telegraf-telegraf.conf.j2 [\#2](https://github.com/dj-wasabi/ansible-telegraf/pull/2) ([aferrari-technisys](https://github.com/aferrari-technisys))
- Improvement and upgrade for v0.2.0 of telegraf [\#1](https://github.com/dj-wasabi/ansible-telegraf/pull/1) ([aferrari-technisys](https://github.com/aferrari-technisys))

## [0.1.0](https://github.com/dj-wasabi/ansible-telegraf/tree/0.1.0) (2015-09-23)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.0.2...0.1.0)

## [0.0.2](https://github.com/dj-wasabi/ansible-telegraf/tree/0.0.2) (2015-09-20)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/0.0.1...0.0.2)

## [0.0.1](https://github.com/dj-wasabi/ansible-telegraf/tree/0.0.1) (2015-09-20)

[Full Changelog](https://github.com/dj-wasabi/ansible-telegraf/compare/03adb259af33123c917cdc960d23aeee07e01fef...0.0.1)



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
