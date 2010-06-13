#
%define		ppp_version	2.4.5
#
Summary:	Mobile broadband modem management service
Name:		ModemManager
Version:	0.3.998
Release:	0.1
License:	GPL v2
Group:		Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/ModemManager/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	0da710318e395ff1ba50a7ba224ef31d
URL:		http://www.gnome.org/projects/NetworkManager/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.75
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	ppp-plugin-devel >= 3:%{ppp_version}
BuildRequires:	udev-glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ModemManager service provides a consistent API to operate many
different modems, including mobile broadband (3G) devices.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-pppd-plugin-dir=%{_libdir}/pppd/%{ppp_version}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/ModemManager/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_libdir}/pppd/*.*.*/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/modem-manager
%dir %{_libdir}/ModemManager
%attr(755,root,root) %{_libdir}/ModemManager/libmm-plugin-anydata.so
%attr(755,root,root) %{_libdir}/ModemManager/libmm-plugin-generic.so
%attr(755,root,root) %{_libdir}/ModemManager/libmm-plugin-gobi.so
%attr(755,root,root) %{_libdir}/ModemManager/libmm-plugin-hso.so
%attr(755,root,root) %{_libdir}/ModemManager/libmm-plugin-huawei.so
%attr(755,root,root) %{_libdir}/ModemManager/libmm-plugin-longcheer.so
%attr(755,root,root) %{_libdir}/ModemManager/libmm-plugin-mbm.so
%attr(755,root,root) %{_libdir}/ModemManager/libmm-plugin-moto-c.so
%attr(755,root,root) %{_libdir}/ModemManager/libmm-plugin-nokia.so
%attr(755,root,root) %{_libdir}/ModemManager/libmm-plugin-novatel.so
%attr(755,root,root) %{_libdir}/ModemManager/libmm-plugin-option.so
%attr(755,root,root) %{_libdir}/ModemManager/libmm-plugin-sierra.so
%attr(755,root,root) %{_libdir}/ModemManager/libmm-plugin-simtech.so
%attr(755,root,root) %{_libdir}/ModemManager/libmm-plugin-zte.so
%attr(755,root,root) %{_libdir}/pppd/%{ppp_version}/mm-test-pppd-plugin.so
/lib/udev/rules.d/77-mm-ericsson-mbm.rules
/lib/udev/rules.d/77-mm-longcheer-port-types.rules
/lib/udev/rules.d/77-mm-pcmcia-device-blacklist.rules
/lib/udev/rules.d/77-mm-platform-serial-whitelist.rules
/lib/udev/rules.d/77-mm-simtech-port-types.rules
/lib/udev/rules.d/77-mm-usb-device-blacklist.rules
/lib/udev/rules.d/77-mm-zte-port-types.rules
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/org.freedesktop.ModemManager.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.ModemManager.service
%{_datadir}/polkit-1/actions/org.freedesktop.modem-manager.policy
%{_iconsdir}/hicolor/*/apps/*.png
