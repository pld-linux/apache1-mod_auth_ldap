#
# Conditional build:
%bcond_with	ssl	# build with ssl (requires netscape sdk), tls is available with openldap
#
%define	mod_name	auth_ldap
%define apxs	/usr/sbin/apxs1
Summary:	This is a LDAP authentication module for Apache
Summary(cs.UTF-8):	Autentizační modul LDAP pro WWW server Apache
Summary(da.UTF-8):	En LDAP-autenticeringsmodul for Apache
Summary(de.UTF-8):	Ein LDAP Authentifizierungsmodul für Apache
Summary(es.UTF-8):	Este módulo proporciona autenticación LDAP para Apache
Summary(fr.UTF-8):	Module d'authentification LDAP pour Apache
Summary(id.UTF-8):	Module LDAP authentication untuk Apache
Summary(it.UTF-8):	Modulo di autenticazione LDPA per Apache
Summary(ja.UTF-8):	Apache 用の LDAP 認証モジュール
Summary(nb.UTF-8):	En LDAP-autentiseringsmodul for Apache
Summary(pl.UTF-8):	Moduł uwierzytelnienia LDAP dla Apache
Summary(pt.UTF-8):	Um módulo de autenticação de LDAP para o Apache
Summary(pt_BR.UTF-8):	Este módulo provê autenticação LDAP para o Apache
Summary(ru.UTF-8):	Аутентификационный модуль LDAP для сервера Apache
Summary(sl.UTF-8):	Avtentikacijski modul LDAP za Apache
Summary(sv.UTF-8):	En LDAP autentiseringsmodul för Apache
Summary(zh_CN.UTF-8):	这是用于 Apache 的 LDAP 验证模块
Name:		apache1-mod_%{mod_name}
Version:	1.6.1
Release:	0.1
License:	BSD
Group:		Networking/Daemons
Source0:	http://www.rudedog.org/auth_ldap/auth_ldap-%{version}.tar.gz
# Source0-md5:	a78d8c5fc77086562ca056c226c97992
Patch0:		%{name}-makefile.patch
URL:		http://www.rudedog.org/auth_ldap/
BuildRequires:	apache1-devel >= 1.3.39
BuildRequires:	autoconf
BuildRequires:	lynx
BuildRequires:	openldap-devel >= 2.3.0
%{?with_ssl:BuildRequires:	mozldap-devel}
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	apache1(EAPI)
Requires:	apache1-mod_auth
Obsoletes:	apache-mod_auth_ldap < 1.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		_sysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)

%description
This is an authentication module for Apache that allows you to
authenticate HTTP clients using user entries in an LDAP directory.

%description -l cs.UTF-8
Balíček obsahuje autentizační modul pro WWW server Apache, který
umožňuje autentizovat HTTP klienty proti položkám v adresářové službě
LDAP.

%description -l da.UTF-8
Denne pakke indeholder en autenticeringsmodul for webtjeneren Apache -
med auth_ldap installeret kan HTTP-klienter autenticeres mod
brugerinformation i et LDAP-katalog.

%description -l de.UTF-8
Dieses Paket enthält ein Authentifizierungs-Modul für den Apache
Webserver, das Ihnen ermöglicht, HTTP-Clients mit Hilfe von
Benutzereinträgen in einem LDAP-Verzeichniss zu authentifizieren.

%description -l es.UTF-8
Este paquete contiene un módulo de autenticación para el servidor
Apache web que le permite autenticar clientes HTTP usando entradas de
usuario en un directorio LDAP.

%description -l fr.UTF-8
Ce paquetage contient un module d'authentification pour le serveur Web
Apache, qui vous permet d'authentifier les clients HTTP en utilisant
les entrées utilisateur dans un répertoire LDAP.

%description -l id.UTF-8
Ini adalah authentication module untuk Apache yang memungkinkan anda
melakukan otentikasi HTTP client menggunakan user entry di dalam LADP
directory.

%description -l it.UTF-8
Questo pacchetto contiene un modulo di autenticazione per il Web
server Apache che consente di autenticare i client HTTP tramite gli
inserimenti utente in una directory LDPA.

%description -l ja.UTF-8
このパッケージには Apache Web サーバーで LDAP ディレクトリ内のユーザー
エントリを使った HTTP クライアントの認証を可能にするための認証
モジュールが含まれています。

%description -l nb.UTF-8
Denne pakken inneholder en autentiseringsmodul for webtjeneren Apache
- med auth_ldap installert kan HTTP-klienter autentiseres mot
  brukerinformasjon i en LDAP-katalog.

%description -l pl.UTF-8
W pakiecie znajduje się moduł do Apache, który pozwala na
uwierzytelnianie klientów HTTP przy użyciu LDAP.

%description -l pt.UTF-8
Este pacote contém um módulo de autenticação para o servidor Web
Apache que lhe permite autenticar os clientes HTTP usando registos de
utilizadores numa directoria LDAP.

%description -l pt_BR.UTF-8
Este módulo permite que você autentique clientes HTTP usando o
diretório LDAP.

%description -l ru.UTF-8
Это модуль аутентификации для Apache, позволяющий идентифицировать
HTTP-клиентов на основе записей пользователя в каталоге LDAP.

%description -l sv.UTF-8
Detta paket innehåller en autenticeringsmodul för webbservern Apache
som låter dig autenticera HTTP-klienter med använderposter i en
LDAP-katalog.

%description -l zh_CN.UTF-8
这是用于 Apache 的验证模块，它允许您使用 LDAP 目录中的用户项验证 HTTP
客户机。

%prep
%setup -q -n auth_ldap-%{version}
%patch0 -p1
mv -f auth_ldap.c mod_auth_ldap.c

lynx -nolist -dump auth_ldap.html > auth_ldap.txt

%build
%{__autoconf}
%configure \
	--with-apxs=%{apxs} \
	--with-ldap-sdk=openldap \
	--with%{!?with_ssl:out}-ssl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkglibdir},%{_sysconfdir}/conf.d}

install mod_%{mod_name}.so $RPM_BUILD_ROOT%{_pkglibdir}

echo 'LoadModule %{mod_name}_module	modules/mod_%{mod_name}.so' > \
	$RPM_BUILD_ROOT%{_sysconfdir}/conf.d/90_mod_%{mod_name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q apache restart

%postun
if [ "$1" = "0" ]; then
	%service -q apache restart
fi

%triggerpostun -- apache1-mod_%{mod_name} < 1.6.0-1.1
# check that they're not using old apache.conf
if grep -q '^Include conf\.d' /etc/apache/apache.conf; then
	sed -i -e '/^\(Add\|Load\)Module.*mod_%{mod_name}\.\(so\|c\)/d' /etc/apache/apache.conf
fi

%files
%defattr(644,root,root,755)
%doc *.html PROBLEMS auth_ldap.txt
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_%{mod_name}.conf
%attr(755,root,root) %{_pkglibdir}/mod_auth_ldap.so
