Summary:	This is a LDAP authentication module for Apache
Summary(es):	Este módulo proporciona autenticación LDAP para Apache
Summary(pl):	Modu³ autentyfikacyjny dla Apache
Summary(pt_BR):	Este módulo provê autenticação LDAP para o Apache
Name:		apache-mod_auth_ldap
Version:	1.6.0
Release:	1
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	http://www.rudedog.org/auth_ldap/auth_ldap-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
URL:		http://www.rudedog.org/auth_ldap/
BuildRequires:	apache(EAPI)-devel
BuildRequires:	openldap-devel
Prereq:		apache(EAPI)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_prefix}/lib/apache

%description
This is an authentication module for Apache that allows you to
authenticate HTTP clients using user entries in an LDAP directory.

%description -l es
Este módulo permite autenticar clientes HTTP usando el directorio
LDAP.

%description -l pl
W pakiecie znajduje siê modu³ do Apache, który pozwala na
autentyfikacjê klientów HTTP przy u¿yciu LDAP.

%description -l pt_BR
Este módulo permite que você autentique clientes HTTP usando o
diretório LDAP.

%prep 
%setup -q -n auth_ldap-%{version}
%patch0 -p1

%build
autoconf
%configure \
	--with-apxs=/usr/sbin/apxs \
	--with-ldap-sdk=openldap \
	--without-ssl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf PROBLEMS

%post
/usr/sbin/apxs -e -a -n auth_ldap %{_libexecdir}/mod_auth_ldap.so 1>&2

%preun
if [ "$1" = "0" ]; then
	/usr/sbin/apxs -e -A -n auth_ldap %{_libexecdir}/mod_auth_ldap.so 1>&2
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html *.gz
%attr(755,root,root) %{_libexecdir}/mod_auth_ldap.so
