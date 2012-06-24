%define	mod_name	auth_ldap
%define apxs	/usr/sbin/apxs1
Summary:	This is a LDAP authentication module for Apache
Summary(cs):	Autentiza�n� modul LDAP pro WWW server Apache
Summary(da):	En LDAP-autenticeringsmodul for Apache
Summary(de):	Ein LDAP Authentifizierungsmodul f�r Apache
Summary(es):	Este m�dulo proporciona autenticaci�n LDAP para Apache
Summary(fr):	Module d'authentification LDAP pour Apache
Summary(id):	Module LDAP authentication untuk Apache
Summary(it):	Modulo di autenticazione LDPA per Apache
Summary(ja):	Apache �Ѥ� LDAP ǧ�ڥ⥸�塼��
Summary(nb):	En LDAP-autentiseringsmodul for Apache
Summary(pl):	Modu� uwierzytelnienia LDAP dla Apache
Summary(pt):	Um m�dulo de autentica��o de LDAP para o Apache
Summary(pt_BR):	Este m�dulo prov� autentica��o LDAP para o Apache
Summary(ru):	������������������ ������ LDAP ��� ������� Apache
Summary(sl):	Avtentikacijski modul LDAP za Apache
Summary(sv):	En LDAP autentiseringsmodul f�r Apache
Summary(zh_CN):	�������� Apache �� LDAP ��֤ģ��
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
Bal��ek obsahuje autentiza�n� modul pro WWW server Apache, kter�
umo��uje autentizovat HTTP klienty proti polo�k�m v adres��ov� slu�b�
LDAP.

%description -l da
Denne pakke indeholder en autenticeringsmodul for webtjeneren Apache -
med auth_ldap installeret kan HTTP-klienter autenticeres mod
brugerinformation i et LDAP-katalog.

%description -l de
Dieses Paket enth�lt ein Authentifizierungs-Modul f�r den Apache
Webserver, das Ihnen erm�glicht, HTTP-Clients mit Hilfe von
Benutzereintr�gen in einem LDAP-Verzeichniss zu authentifizieren.

%description -l es
Este paquete contiene un m�dulo de autenticaci�n para el servidor
Apache web que le permite autenticar clientes HTTP usando entradas de
usuario en un directorio LDAP.

%description -l fr
Ce paquetage contient un module d'authentification pour le serveur Web
Apache, qui vous permet d'authentifier les clients HTTP en utilisant
les entr�es utilisateur dans un r�pertoire LDAP.

%description -l id
Ini adalah authentication module untuk Apache yang memungkinkan anda
melakukan otentikasi HTTP client menggunakan user entry di dalam LADP
directory.

%description -l it
Questo pacchetto contiene un modulo di autenticazione per il Web
server Apache che consente di autenticare i client HTTP tramite gli
inserimenti utente in una directory LDPA.

%description -l ja
���Υѥå������ˤ� Apache Web �����С��� LDAP �ǥ��쥯�ȥ���Υ桼����
����ȥ��Ȥä� HTTP ���饤����Ȥ�ǧ�ڤ��ǽ�ˤ��뤿���ǧ��
�⥸�塼�뤬�ޤޤ�Ƥ��ޤ���

%description -l nb
Denne pakken inneholder en autentiseringsmodul for webtjeneren Apache
- med auth_ldap installert kan HTTP-klienter autentiseres mot
brukerinformasjon i en LDAP-katalog.

%description -l pl
W pakiecie znajduje si� modu� do Apache, kt�ry pozwala na
uwierzytelnianie klient�w HTTP przy u�yciu LDAP.

%description -l pt
Este pacote cont�m um m�dulo de autentica��o para o servidor Web
Apache que lhe permite autenticar os clientes HTTP usando registos de
utilizadores numa directoria LDAP.

%description -l pt_BR
Este m�dulo permite que voc� autentique clientes HTTP usando o
diret�rio LDAP.

%description -l ru
��� ������ �������������� ��� Apache, ����������� ����������������
HTTP-�������� �� ������ ������� ������������ � �������� LDAP.

%description -l sv
Detta paket inneh�ller en autenticeringsmodul f�r webbservern Apache
som l�ter dig autenticera HTTP-klienter med anv�nderposter i en
LDAP-katalog.

%description -l zh_CN
�������� Apache ����֤ģ�飬��������ʹ�� LDAP Ŀ¼�е��û�����֤ HTTP
�ͻ�����

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
