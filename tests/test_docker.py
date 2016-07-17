
def test_telegraf_running_and_enabled(Service, SystemInfo):
    telegraf = Service("telegraf")
    assert telegraf.is_enabled
    if SystemInfo.distribution == 'centos':
        assert telegraf.is_running


def test_telegraf_dot_conf(File):
    telegraf = File("/etc/telegraf/telegraf.conf")
    assert telegraf.user == "root"
    assert telegraf.group == "root"
    assert telegraf.mode == 0o644
    assert telegraf.contains('[[inputs.cpu]]')


def test_telegraf_package(Package, SystemInfo):
    telegraf = Package('telegraf')
    assert telegraf.is_installed
