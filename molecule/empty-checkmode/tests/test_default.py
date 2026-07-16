import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('telegraf')


def test_telegraf_running_and_enabled(host):
    if host.system_info.distribution in ['opensuse-leap']:
        return
    # Telegraf is never installed in this check-mode scenario, so its systemd
    # unit does not exist. On modern systemd (Ubuntu 24.04, Debian 13, EL10)
    # `systemctl is-enabled/is-active` returns exit code 4 ("not-found"),
    # which testinfra's .is_enabled/.is_running raise on (they only accept
    # 0/1). Assert against the raw command so a missing unit reads as
    # not-enabled / not-active across all systemd versions.
    assert host.run("systemctl is-enabled telegraf").stdout.strip() != "enabled"
    assert host.run("systemctl is-active telegraf").stdout.strip() != "active"


def test_telegraf_dot_conf(host):
    telegraf = host.file("/etc/telegraf/telegraf.conf")
    assert not telegraf.exists

def test_telegraf_dot_d_dir(host):
    telegraf = host.file("/etc/telegraf/telegraf.d")
    assert not telegraf.exists


def test_telegraf_dot_d(host):
    telegraf = host.file("/etc/telegraf/telegraf.d/tail.conf")
    assert not telegraf.exists


def test_telegraf_package(host):
    telegraf = host.package('telegraf')
    assert not telegraf.is_installed
