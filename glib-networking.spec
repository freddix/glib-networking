Summary:	Networking support for GLib
Name:		glib-networking
Version:	2.42.1
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glib-networking/2.42/%{name}-%{version}.tar.xz
# Source0-md5:	2959c3f9b5f2ed838ce373130d8d4500
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib-devel >= 1:2.42.0
BuildRequires:	gnutls-devel
BuildRequires:	gsettings-desktop-schemas-devel >= 3.14.0
BuildRequires:	intltool
BuildRequires:	libproxy-devel
BuildRequires:	libtool
BuildRequires:	p11-kit-devel
BuildRequires:	pkg-config
Requires(post,postun):	glib-gio >= 1:2.40.0
# org.gnome.system.proxy.gschema.xml
Requires:	glib >= 1:2.42.0
Requires:	gsettings-desktop-schemas >= 3.14.0
Requires:	ca-certificates
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains modules that extend the networking support in
GIO. In particular, it contains a libproxy-based GProxyResolver
implementation and a gnutls-based GTlsConnection implementation.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gio/modules/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
gio-querymodules %{_libdir}/gio/modules || :

%postun
umask 022
gio-querymodules %{_libdir}/gio/modules || :

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/glib-pacrunner
%attr(755,root,root) %{_libdir}/gio/modules/libgiognomeproxy.so
%attr(755,root,root) %{_libdir}/gio/modules/libgiognutls.so
%attr(755,root,root) %{_libdir}/gio/modules/libgiolibproxy.so
%{_datadir}/dbus-1/services/org.gtk.GLib.PACRunner.service

