INSTALLED_APPS += ["taiga_contrib_ldap_auth_ext"]

# Multiple LDAP servers are currently not supported, see
# https://github.com/Monogramm/taiga-contrib-ldap-auth-ext/issues/16
LDAP_PORT = 3890
LDAP_BIND_DN = "uid=admin,ou=people,dc=tranquang,dc=net"
# server and password will be append by droneCI

LDAP_SEARCH_BASE = 'ou=people,dc=tranquang,dc=net'
LDAP_SEARCH_FILTER_ADDITIONAL = '(memberof=cn=lldap_todo,ou=groups,dc=tranquang,dc=net)'

LDAP_GROUP_ADMIN = 'cn=lldap_admin,ou=groups,dc=tranquang,dc=net'

LDAP_USERNAME_ATTRIBUTE = "uid"
LDAP_EMAIL_ATTRIBUTE = "mail"
LDAP_FULL_NAME_ATTRIBUTE = "displayName"

LDAP_SAVE_LOGIN_PASSWORD = False

LDAP_MAP_USERNAME_TO_UID = None

