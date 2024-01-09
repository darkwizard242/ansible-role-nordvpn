import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

PACKAGE = 'nordvpn'
PACKAGE_BINARY = '/usr/bin/nordvpn'
REPO_DEBIAN_FILE = '/etc/apt/sources.list.d/nordvpn.list'


def test_nordvpn_package_installed(host):
    """
    Tests if nordvpn package is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_nordvpn_binary_exists(host):
    """
    Tests if nordvpn binary exists.
    """
    host.file(PACKAGE_BINARY).exists


def test_nordvpn_binary_which(host):
    """
    Tests the output to confirm nordvpn's binary location.
    """
    assert host.check_output('which nordvpn') == PACKAGE_BINARY


def test_nordvpn_repofile_exists(host):
    """
    Tests if nordvpn repo file exists.
    """
    assert host.file(REPO_DEBIAN_FILE).exists


def test_nordvpn_repofile_isfile(host):
    """
    Tests if nordvpn repo file is file type.
    """
    assert host.file(REPO_DEBIAN_FILE).is_file
