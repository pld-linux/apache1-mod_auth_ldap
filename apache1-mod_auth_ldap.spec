Summary:	This is a LDAP authentication module for Apache
Name:		auth_ldap
Version:	1.4.0
Release:	1
License:	GPL
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source0:	http://www.rudedog.org/auth_ldap/%{name}-%{version}.tar.gz
Patch0:		auth_ldap-redhat.patch
URL:		http://www.rudedog.org/auth_ldap/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an authentication module for Apache that allows you to
authenticate HTTP clients using user entries in an LDAP directory.

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
%defattr(644,root,root,755)
%doc *.html PROBLEMS
%attr(755,root,root) %{_libdir}/apache/mod_auth_ldap.so
