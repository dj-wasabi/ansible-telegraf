import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('telegraf')


def test_telegraf_running_and_enabled(host):
    telegraf = host.service("telegraf")
    if host.system_info.distribution not in ['opensuse-leap']:
        assert not telegraf.is_enabled
        assert not telegraf.is_running


def test_telegraf_dot_conf(host):
    telegraf = host.file("/etc/telegraf/telegraf.conf")
    assert not telegraf.exists

def test_telegraf_dot_d_dir(host):
    telegraf = host.file("/etc/telegraf/telegraf.d")
    assert not telegraf.exists


def test_telegraf_dot_d(host):
    telegraf = host.file("/etc/telegraf/telegraf.d/logparser.conf")
    assert not telegraf.exists


def test_telegraf_package(host):
    telegraf = host.package('telegraf')
    assert not telegraf.is_installed
