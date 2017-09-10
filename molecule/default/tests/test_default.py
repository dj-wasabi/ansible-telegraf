import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_telegraf_running_and_enabled(Service, SystemInfo):
    telegraf = Service("telegraf")
    assert telegraf.is_enabled
    if SystemInfo.distribution == 'centos':
        assert telegraf.is_running


def test_telegraf_dot_conf(File):
    telegraf = File("/etc/telegraf/telegraf.conf")
    assert telegraf.user == "telegraf"
    assert telegraf.group == "telegraf"
    assert telegraf.mode == 0o640
    assert telegraf.contains('[[inputs.cpu]]')


def test_telegraf_package(Package, SystemInfo):
    telegraf = Package('telegraf')
    assert telegraf.is_installed
