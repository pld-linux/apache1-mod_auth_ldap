Summary:	This is a LDAP authentication module for Apache
Summary(pl):	Modu³ autentyfikacyjny dla Apache
Summary(pt_BR):	Este módulo provê autenticação LDAP para o Apache
Summary(es):	Este módulo proporciona autenticación LDAP para Apache
Name:		apache-mod_auth_ldap
Version:	1.6.0
Release:	1
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	http://www.rudedog.org/auth_ldap/auth_ldap-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
BuildRequires:	apache
BuildRequires:	apache-devel
BuildRequires:	openldap-devel
URL:		http://www.rudedog.org/auth_ldap/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an authentication module for Apache that allows you to
authenticate HTTP clients using user entries in an LDAP directory.

%description -l pl
W pakiecie znajduje siê modu³ do Apache, który pozwala na autentyfikacjê
klientów HTTP przy u¿yciu LDAP.

%description -l pt_BR
Este módulo permite que você autentique clientes HTTP usando o diretório
LDAP.

%description -l es
Este módulo permite autenticar clientes HTTP usando el directorio
LDAP.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html *.gz
%attr(755,root,root) %{_libdir}/apache/mod_auth_ldap.so
