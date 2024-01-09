[![build-test](https://github.com/darkwizard242/ansible-role-nordvpn/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-nordvpn/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-nordvpn/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-nordvpn/actions?query=workflow%3Arelease) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-nordvpn&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-nordvpn) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-nordvpn&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-nordvpn) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-nordvpn&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-nordvpn) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-nordvpn&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-nordvpn) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-nordvpn?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-nordvpn?color=orange&style=flat-square)

# Ansible Role: nordvpn

Role to install (_by default_) [nordvpn](https://nordvpn.com/) package for Debian based and EL based systems or uninstall (_if passed as var_) on **Debian** based and **EL** based systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
# Generic Variables
nordvpn_app_name: nordvpn
nordvpn_desired_state: present

# Debian Family Variables
nordvpn_pre_reqs_debian:
  - gnupg2
nordvpn_pre_reqs_debian_desired_state: present
nordvpn_repo_debian_gpg_key_url: "https://repo.nordvpn.com/gpg/nordvpn_public.asc"
nordvpn_repo_debian: "deb https://repo.nordvpn.com//deb/nordvpn/debian stable main"
nordvpn_repo_debian_filename: "{{ nordvpn_app_name }}"
nordvpn_repo_debian_desired_state: present
```

### Variables table:

Variable                                  | Description
----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
nordvpn_app_name                      | Name of nordvpn package to install by default i.e. `nordvpn`.
nordvpn_desired_state                 | State of the nordvpn_app_name package (i.e. `nordvpn` package itself.). Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
nordvpn_pre_reqs_debian               | Package required by nordvpn on Debain based systems.
nordvpn_pre_reqs_debian_desired_state | State of the nordvpn_pre_reqs_debian_desired_state packages. Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
nordvpn_repo_debian_gpg_key_url       | nordvpn GPG required on Debian based systems.
nordvpn_repo_debian_gpg_key_keyring   | nordvpn Keyring file to store GPG key in.
nordvpn_repo_debian                   | Repository URL for Debian based systems.
nordvpn_repo_debian_filename          | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems. Defaults to the variable value for "{{ nordvpn_app_name }}" which is `nordvpn` by default.
nordvpn_repo_debian_desired_state     | State of Debian family repository file for nordvpn.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **nordvpn** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.nordvpn
```

For customizing behavior of role (for e.g. update to latest available stable version, **nordvpn** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.nordvpn
  vars:
    nordvpn_app_name: latest
```

For customizing behavior of role (for e.g. un-installation of **nordvpn** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.nordvpn
  vars:
    nordvpn_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-nordvpn/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
