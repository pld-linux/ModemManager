Summary:	Mobile broadband modem management service
Summary(pl.UTF-8):	Usługa zarządzająca szerokopasmowymi modemami komórkowymi
Name:		ModemManager
Version:	0.6.0.0
Release:	1
License:	GPL v2+
Group:		Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/ModemManager/0.6/%{name}-%{version}.tar.xz
# Source0-md5:	f32640f6672d997ec0887307186e9639
URL:		http://www.gnome.org/projects/NetworkManager/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.86
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.18
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.95
BuildRequires:	ppp-plugin-devel >= 3:2.4.5
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-glib-devel
BuildRequires:	xz
Requires:	dbus-glib >= 0.86
Requires:	glib2 >= 1:2.18
Requires:	hicolor-icon-theme
Requires:	polkit >= 0.95
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ModemManager service provides a consistent API to operate many
different modems, including mobile broadband (3G) devices.

%description -l pl.UTF-8
Usługa ModemManager zapewnia spójne API do obsługi wielu różnych
modemów, w tym szerokopasmowych modemów komórkowych (3G).

%package devel
Summary:	Header file defining ModemManager D-Bus interface
Summary(pl.UTF-8):	Plik nagłówkowy opisujący interfejs D-Bus ModemManagera
Group:		Development/Libraries
# doesn't require base

%description devel
Header file defining ModemManager D-Bus interface.

%description devel -l pl.UTF-8
Plik nagłówkowy opisujący interfejs D-Bus ModemManagera.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	--enable-more-warnings \
	--with-polkit \
	--with-pppd-plugin-dir=%{_libdir}/pppd/plugins
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/pppd/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/modem-manager
%dir %{_libdir}/ModemManager
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-anydata.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-cinterion.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-generic.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-gobi.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-hso.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-huawei.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-iridium.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-linktop.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-longcheer.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-mbm.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-moto-c.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-nokia.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-novatel.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-option.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-samsung.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-sierra.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-simtech.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-wavecom.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-x22x.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-zte.so
%attr(755,root,root) %{_libdir}/pppd/plugins/mm-test-pppd-plugin.so
/lib/udev/rules.d/77-mm-ericsson-mbm.rules
/lib/udev/rules.d/77-mm-longcheer-port-types.rules
/lib/udev/rules.d/77-mm-nokia-port-types.rules
/lib/udev/rules.d/77-mm-pcmcia-device-blacklist.rules
/lib/udev/rules.d/77-mm-platform-serial-whitelist.rules
/lib/udev/rules.d/77-mm-simtech-port-types.rules
/lib/udev/rules.d/77-mm-usb-device-blacklist.rules
/lib/udev/rules.d/77-mm-x22x-port-types.rules
/lib/udev/rules.d/77-mm-zte-port-types.rules
/lib/udev/rules.d/80-mm-candidate.rules
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/org.freedesktop.ModemManager.conf
%{_datadir}/dbus-1/interfaces/mm-mobile-error.xml
%{_datadir}/dbus-1/interfaces/mm-modem-connect-error.xml
%{_datadir}/dbus-1/interfaces/mm-modem-error.xml
%{_datadir}/dbus-1/interfaces/mm-serial-error.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager.Modem.Cdma.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager.Modem.Firmware.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager.Modem.Gsm.Card.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager.Modem.Gsm.Contacts.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager.Modem.Gsm.Hso.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager.Modem.Gsm.Network.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager.Modem.Gsm.SMS.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager.Modem.Gsm.Ussd.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager.Modem.Gsm.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager.Modem.Location.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager.Modem.Simple.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager.Modem.Time.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager.Modem.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.ModemManager.service
%{_datadir}/polkit-1/actions/org.freedesktop.modem-manager.policy
%{_iconsdir}/hicolor/*/apps/*.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/mm
