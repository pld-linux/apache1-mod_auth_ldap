Summary: This is a LDAP authentication module for Apache
Name: auth_ldap
Group: Applications/System
Copyright: GPL
Version: 1.4.0
Release: 1
Source: http://www.rudedog.org/auth_ldap/auth_ldap-%{version}.tar.gz
Patch0: auth_ldap-1.4.0-redhat.patch
Url: http://www.rudedog.org/auth_ldap/
BuildRoot: /var/tmp/%{name}-root
NoSource: 0

%description
This is an authentication module for Apache that allows you to authenticate
HTTP clients using user entries in an LDAP directory.

%prep
%setup -q
%patch0 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/lib/apache/mod_auth_ldap.so
%doc *.html PROBLEMS

%changelog
* Mon Nov 8 1999 Toru Hoshina <t@kondara.org>
- be a NoSrc :-P

* Tue Sep 07 1999 Cristian Gafton <gafton@redhat.com>
- first build for Red Hat Linux 6.1
