%define	mod_name	auth_ldap
%define apxs	/usr/sbin/apxs1
Summary:	This is a LDAP authentication module for Apache
Summary(cs):	Autentizaèní modul LDAP pro WWW server Apache
Summary(da):	En LDAP-autenticeringsmodul for Apache
Summary(de):	Ein LDAP Authentifizierungsmodul für Apache
Summary(es):	Este módulo proporciona autenticación LDAP para Apache
Summary(fr):	Module d'authentification LDAP pour Apache
Summary(id):	Module LDAP authentication untuk Apache
Summary(it):	Modulo di autenticazione LDPA per Apache
Summary(ja):	Apache ÍÑ¤Î LDAP Ç§¾Ú¥â¥¸¥å¡¼¥ë
Summary(nb):	En LDAP-autentiseringsmodul for Apache
Summary(pl):	Modu³ uwierzytelnienia LDAP dla Apache
Summary(pt):	Um módulo de autenticação de LDAP para o Apache
Summary(pt_BR):	Este módulo provê autenticação LDAP para o Apache
Summary(ru):	áÕÔÅÎÔÉÆÉËÁÃÉÏÎÎÙÊ ÍÏÄÕÌØ LDAP ÄÌÑ ÓÅÒ×ÅÒÁ Apache
Summary(sl):	Avtentikacijski modul LDAP za Apache
Summary(sv):	En LDAP autentiseringsmodul för Apache
Summary(zh_CN):	ÕâÊÇÓÃÓÚ Apache µÄ LDAP ÑéÖ¤Ä£¿é
Name:		apache1-mod_%{mod_name}
Version:	1.6.0
Release:	1
License:	BSD
Group:		Networking/Daemons
Source0:	http://www.rudedog.org/auth_ldap/auth_ldap-%{version}.tar.gz
# Source0-md5:	ff7de9027fe8852facd27be93462c5cc
Patch0:		%{name}-makefile.patch
URL:		http://www.rudedog.org/auth_ldap/
BuildRequires:	autoconf
BuildRequires:	apache1-devel
BuildRequires:	openldap-devel
BuildRequires:	%{apxs}
PreReq:		apache1
PreReq:		apache1-mod_auth
Requires(post,preun):	%{apxs}
Obsoletes:	apache-mod_%{mod_name} <= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR)

%description
This is an authentication module for Apache that allows you to
authenticate HTTP clients using user entries in an LDAP directory.

%description -l cs
Balíèek obsahuje autentizaèní modul pro WWW server Apache, kterı
umo¾òuje autentizovat HTTP klienty proti polo¾kám v adresáøové slu¾bì
LDAP.

%description -l da
Denne pakke indeholder en autenticeringsmodul for webtjeneren Apache -
med auth_ldap installeret kan HTTP-klienter autenticeres mod
brugerinformation i et LDAP-katalog.

%description -l de
Dieses Paket enthält ein Authentifizierungs-Modul für den Apache
Webserver, das Ihnen ermöglicht, HTTP-Clients mit Hilfe von
Benutzereinträgen in einem LDAP-Verzeichniss zu authentifizieren.

%description -l es
Este paquete contiene un módulo de autenticación para el servidor
Apache web que le permite autenticar clientes HTTP usando entradas de
usuario en un directorio LDAP.

%description -l fr
Ce paquetage contient un module d'authentification pour le serveur Web
Apache, qui vous permet d'authentifier les clients HTTP en utilisant
les entrées utilisateur dans un répertoire LDAP.

%description -l id
Ini adalah authentication module untuk Apache yang memungkinkan anda
melakukan otentikasi HTTP client menggunakan user entry di dalam LADP
directory.

%description -l it
Questo pacchetto contiene un modulo di autenticazione per il Web
server Apache che consente di autenticare i client HTTP tramite gli
inserimenti utente in una directory LDPA.

%description -l ja
¤³¤Î¥Ñ¥Ã¥±¡¼¥¸¤Ë¤Ï Apache Web ¥µ¡¼¥Ğ¡¼¤Ç LDAP ¥Ç¥£¥ì¥¯¥È¥êÆâ¤Î¥æ¡¼¥¶¡¼
¥¨¥ó¥È¥ê¤ò»È¤Ã¤¿ HTTP ¥¯¥é¥¤¥¢¥ó¥È¤ÎÇ§¾Ú¤ò²ÄÇ½¤Ë¤¹¤ë¤¿¤á¤ÎÇ§¾Ú
¥â¥¸¥å¡¼¥ë¤¬´Ş¤Ş¤ì¤Æ¤¤¤Ş¤¹¡£

%description -l nb
Denne pakken inneholder en autentiseringsmodul for webtjeneren Apache
- med auth_ldap installert kan HTTP-klienter autentiseres mot
brukerinformasjon i en LDAP-katalog.

%description -l pl
W pakiecie znajduje siê modu³ do Apache, który pozwala na
uwierzytelnianie klientów HTTP przy u¿yciu LDAP.

%description -l pt
Este pacote contém um módulo de autenticação para o servidor Web
Apache que lhe permite autenticar os clientes HTTP usando registos de
utilizadores numa directoria LDAP.

%description -l pt_BR
Este módulo permite que você autentique clientes HTTP usando o
diretório LDAP.

%description -l ru
üÔÏ ÍÏÄÕÌØ ÁÕÔÅÎÔÉÆÉËÁÃÉÉ ÄÌÑ Apache, ĞÏÚ×ÏÌÑÀİÉÊ ÉÄÅÎÔÉÆÉÃÉÒÏ×ÁÔØ
HTTP-ËÌÉÅÎÔÏ× ÎÁ ÏÓÎÏ×Å ÚÁĞÉÓÅÊ ĞÏÌØÚÏ×ÁÔÅÌÑ × ËÁÔÁÌÏÇÅ LDAP.

%description -l sv
Detta paket innehåller en autenticeringsmodul för webbservern Apache
som låter dig autenticera HTTP-klienter med använderposter i en
LDAP-katalog.

%description -l zh_CN
ÕâÊÇÓÃÓÚ Apache µÄÑéÖ¤Ä£¿é£¬ËüÔÊĞíÄúÊ¹ÓÃ LDAP Ä¿Â¼ÖĞµÄÓÃ»§ÏîÑéÖ¤ HTTP
¿Í»§»ú¡£

%prep
%setup -q -n auth_ldap-%{version}
%patch0 -p1
mv -f auth_ldap.c mod_auth_ldap.c

%build
%{__autoconf}
%configure \
	--with-apxs=%{apxs} \
	--with-ldap-sdk=openldap \
	--without-ssl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pkglibdir}

install mod_%{mod_name}.so $RPM_BUILD_ROOT%{_pkglibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{apxs} -e -a -n auth_ldap %{_pkglibdir}/mod_auth_ldap.so 1>&2
if [ -f /var/lock/subsys/apache ]; then
	/etc/rc.d/init.d/apache restart 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n auth_ldap %{_pkglibdir}/mod_auth_ldap.so 1>&2
	if [ -f /var/lock/subsys/apache ]; then
		/etc/rc.d/init.d/apache restart 1>&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc *.html PROBLEMS
%attr(755,root,root) %{_pkglibdir}/mod_auth_ldap.so
