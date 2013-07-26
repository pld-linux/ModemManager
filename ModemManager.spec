#
# Conditional build:
%bcond_without	apidocs		# don't build API documentation
#
Summary:	Mobile broadband modem management service
Summary(pl.UTF-8):	Usługa zarządzająca szerokopasmowymi modemami komórkowymi
Name:		ModemManager
Version:	1.0.0
Release:	1
License:	GPL v2+
Group:		Networking
Source0:	http://www.freedesktop.org/software/ModemManager/%{name}-%{version}.tar.xz
# Source0-md5:	bb59fda111d8e1038b02ed7e57efe83a
URL:		http://www.freedesktop.org/wiki/Software/ModemManager
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gtk-doc
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libmbim-devel >= 1.4
BuildRequires:	libqmi-devel >= 1.4
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.97
BuildRequires:	ppp-plugin-devel >= 3:2.4.5
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-glib-devel >= 147
BuildRequires:	xz
Requires(post,preun,postun):	systemd-units
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2 >= 1:2.32.0
Requires:	hicolor-icon-theme
Requires:	polkit >= 0.97
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ModemManager service provides a consistent API to operate many
different modems, including mobile broadband (3G) devices.

%description -l pl.UTF-8
Usługa ModemManager zapewnia spójne API do obsługi wielu różnych
modemów, w tym szerokopasmowych modemów komórkowych (3G).

%package libs
Summary:	Library to control and monitor the ModemManager
Summary(pl.UTF-8):	Biblioteka do sterowania i monitorowania ModemManagera
Group:		Libraries
Requires:	glib2 >= 1:2.32.0

%description libs
This package provides library to control and monitor the ModemManager.

%description libs -l pl.UTF-8
Ten pakiet dostarcza bibliotekę do sterowania i monitorowania
ModemManagera.

%package devel
Summary:	Header file defining ModemManager D-Bus interface
Summary(pl.UTF-8):	Plik nagłówkowy opisujący interfejs D-Bus ModemManagera
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.32.0

%description devel
Header file defining ModemManager D-Bus interface.

%description devel -l pl.UTF-8
Plik nagłówkowy opisujący interfejs D-Bus ModemManagera.

%package apidocs
Summary:	API documentation for ModemManager
Summary(pl.UTF-8):	Dokumentacja API ModemManagera
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API documentation for ModemManager.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki ModemManagera.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{__enable_disable apidocs gtk-doc} \
	--disable-silent-rules \
	--disable-static \
	--enable-more-warnings \
	--with-html-dir=%{_gtkdocdir} \
	--with-polkit
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%systemd_service_enable ModemManager.service

%preun
%systemd_preun ModemManager.service

%postun
%update_icon_cache hicolor
%systemd_reload

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mmcli
%attr(755,root,root) %{_sbindir}/ModemManager
%dir %{_libdir}/ModemManager
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-altair-lte.so
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
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-motorola.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-nokia-icera.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-nokia.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-novatel-lte.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-novatel.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-option.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-pantech.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-samsung.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-sierra.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-simtech.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-telit.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-via.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-wavecom.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-x22x.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-zte.so
/lib/udev/rules.d/77-mm-ericsson-mbm.rules
/lib/udev/rules.d/77-mm-huawei-net-port-types.rules
/lib/udev/rules.d/77-mm-longcheer-port-types.rules
/lib/udev/rules.d/77-mm-nokia-port-types.rules
/lib/udev/rules.d/77-mm-pcmcia-device-blacklist.rules
/lib/udev/rules.d/77-mm-platform-serial-whitelist.rules
/lib/udev/rules.d/77-mm-simtech-port-types.rules
/lib/udev/rules.d/77-mm-usb-device-blacklist.rules
/lib/udev/rules.d/77-mm-usb-serial-adapters-greylist.rules
/lib/udev/rules.d/77-mm-x22x-port-types.rules
/lib/udev/rules.d/77-mm-zte-port-types.rules
/lib/udev/rules.d/80-mm-candidate.rules
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/org.freedesktop.ModemManager1.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Bearer.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Firmware.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Location.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Messaging.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Modem3gpp.Ussd.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Modem3gpp.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.ModemCdma.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Simple.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Time.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Sim.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Sms.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.xml
%{_datadir}/dbus-1/interfaces/wip-org.freedesktop.ModemManager1.Modem.Contacts.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.ModemManager1.service
%{_datadir}/polkit-1/actions/org.freedesktop.ModemManager1.policy
%{_iconsdir}/hicolor/*/apps/*.png
%{_mandir}/man8/ModemManager.8*
%{_mandir}/man8/mmcli.8*
%{systemdunitdir}/ModemManager.service

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmm-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmm-glib.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmm-glib.so
%{_includedir}/ModemManager
%{_includedir}/libmm-glib
%{_pkgconfigdir}/ModemManager.pc
%{_pkgconfigdir}/mm-glib.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/ModemManager
%{_gtkdocdir}/libmm-glib
