import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('telegraf')


def test_telegraf_running_and_enabled(Service, SystemInfo):
    telegraf = Service("telegraf")
    if SystemInfo.distribution not in ['opensuse-leap']:
        assert telegraf.is_enabled
        assert telegraf.is_running


def test_telegraf_dot_conf(File):
    telegraf = File("/etc/telegraf/telegraf.conf")
    assert telegraf.user == "telegraf"
    assert telegraf.group == "telegraf"
    assert telegraf.mode == 0o640
    assert telegraf.contains('interval = "10s"')
    assert telegraf.contains('[[inputs.cpu]]')
    assert telegraf.contains('percpu = true')
    assert telegraf.contains('[[outputs.influxdb]]')
    assert telegraf.contains('["http://influxdb:8086"]')
    assert telegraf.contains('[[inputs.net]]')


def test_telegraf_dot_d_dir(File):
    telegraf = File("/etc/telegraf/telegraf.d")
    assert telegraf.user == "root"
    assert telegraf.group == "root"
    assert telegraf.mode == 0o755
    assert telegraf.is_directory


def test_telegraf_dot_d(File):
    telegraf = File("/etc/telegraf/telegraf.d/percpu-usage.conf")
    assert telegraf.user == "telegraf"
    assert telegraf.group == "telegraf"
    assert telegraf.mode == 0o640
    assert telegraf.contains('[[inputs.cpu]]')
    assert telegraf.contains('totalcpu = false')


def test_telegraf_package(Package):
    telegraf = Package('telegraf')
    assert telegraf.is_installed
