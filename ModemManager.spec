#
# Conditional build:
%bcond_without	apidocs		# don't build API documentation

Summary:	Mobile broadband modem management service
Summary(pl.UTF-8):	Usługa zarządzająca szerokopasmowymi modemami komórkowymi
Name:		ModemManager
Version:	1.22.0
Release:	1
License:	GPL v2+
Group:		Networking
#Source0Download: https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/tags
Source0:	https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	e967a452eb6f505a645df8c0582a17b7
URL:		https://www.freedesktop.org/wiki/Software/ModemManager
BuildRequires:	dbus-devel >= 1
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.56.0
%if %(locale -a | grep -q '^C\.utf8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildRequires:	gobject-introspection-devel >= 0.9.6
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libgudev-devel >= 232
BuildRequires:	libmbim-devel >= 1.30.0
BuildRequires:	libqmi-devel >= 1.34.0
BuildRequires:	libqrtr-glib-devel >= 1.0.0
BuildRequires:	meson >= 0.53.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.97
BuildRequires:	ppp-plugin-devel >= 3:2.4.5
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	vala >= 2:0.18.0
Requires(post,preun,postun):	systemd-units
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2 >= 1:2.56.0
Requires:	hicolor-icon-theme
Requires:	libgudev >= 232
Requires:	libmbim >= 1.30.0
Requires:	libqmi >= 1.34.0
Requires:	libqrtr-glib >= 1.0.0
Requires:	polkit >= 0.97
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ModemManager service provides a consistent API to operate many
different modems, including mobile broadband (3G) devices.

%description -l pl.UTF-8
Usługa ModemManager zapewnia spójne API do obsługi wielu różnych
modemów, w tym szerokopasmowych modemów komórkowych (3G).

%package -n bash-completion-ModemManager
Summary:	Bash completion for ModemManager commands
Summary(pl.UTF-8):	Dopełnianie składni poleceń ModemManagera
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0
BuildArch:	noarch

%description -n bash-completion-ModemManager
Bash completion for ModemManager commands (mmcli).

%description -n bash-completion-ModemManager -l pl.UTF-8
Dopełnianie składni poleceń ModemManagera (mmcli).

%package libs
Summary:	Library to control and monitor the ModemManager
Summary(pl.UTF-8):	Biblioteka do sterowania i monitorowania ModemManagera
Group:		Libraries
Requires:	glib2 >= 1:2.56.0

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
Requires:	glib2-devel >= 1:2.56.0

%description devel
Header file defining ModemManager D-Bus interface.

%description devel -l pl.UTF-8
Plik nagłówkowy opisujący interfejs D-Bus ModemManagera.

%package apidocs
Summary:	API documentation for ModemManager
Summary(pl.UTF-8):	Dokumentacja API ModemManagera
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
API documentation for ModemManager.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki ModemManagera.

%package -n vala-libmm-glib
Summary:	libmm-glib API for Vala language
Summary(pl.UTF-8):	API libmm-glib dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.18.0
BuildArch:	noarch

%description -n vala-libmm-glib
libmm-glib API for Vala language.

%description -n vala-libmm-glib -l pl.UTF-8
API libmm-glib dla języka Vala.

%prep
%setup -q

%build
%meson build \
	--default-library=shared \
	%{?with_apidocs:-Dgtk_doc=true} \
	-Dsystemdsystemunitdir=%{systemdunitdir} \
	-Dvapi=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%systemd_post ModemManager.service

%preun
%systemd_preun ModemManager.service

%postun
%update_icon_cache hicolor
%systemd_reload

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/mmcli
%attr(755,root,root) %{_sbindir}/ModemManager
%dir %{_libdir}/ModemManager
%dir %{_libdir}/ModemManager/fcc-unlock.d
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-altair-lte.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-anydata.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-broadmobi.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-cinterion.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-dell.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-dlink.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-ericsson-mbm.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-fibocom.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-foxconn.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-generic.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-gosuncn.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-haier.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-huawei.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-intel.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-iridium.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-linktop.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-longcheer.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-option-hso.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-mtk.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-motorola.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-nokia-icera.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-nokia.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-novatel.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-novatel-lte.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-option.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-pantech.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-qcom-soc.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-quectel.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-samsung.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-sierra.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-sierra-legacy.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-simtech.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-telit.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-thuraya.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-tplink.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-ublox.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-via.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-wavecom.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-x22x.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-zte.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-shared-fibocom.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-shared-foxconn.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-shared-icera.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-shared-novatel.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-shared-option.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-shared-sierra.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-shared-telit.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-shared-xmm.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/connection.available.d
%{_datadir}/%{name}/fcc-unlock.available.d
%{_datadir}/%{name}/mm-foxconn-t77w968-carrier-mapping.conf
/lib/udev/rules.d/77-mm-broadmobi-port-types.rules
/lib/udev/rules.d/77-mm-cinterion-port-types.rules
/lib/udev/rules.d/77-mm-dell-port-types.rules
/lib/udev/rules.d/77-mm-dlink-port-types.rules
/lib/udev/rules.d/77-mm-ericsson-mbm.rules
/lib/udev/rules.d/77-mm-fibocom-port-types.rules
/lib/udev/rules.d/77-mm-foxconn-port-types.rules
/lib/udev/rules.d/77-mm-gosuncn-port-types.rules
/lib/udev/rules.d/77-mm-haier-port-types.rules
/lib/udev/rules.d/77-mm-huawei-net-port-types.rules
/lib/udev/rules.d/77-mm-linktop-port-types.rules
/lib/udev/rules.d/77-mm-longcheer-port-types.rules
/lib/udev/rules.d/77-mm-mtk-port-types.rules
/lib/udev/rules.d/77-mm-nokia-port-types.rules
/lib/udev/rules.d/77-mm-qcom-soc.rules
/lib/udev/rules.d/77-mm-quectel-port-types.rules
/lib/udev/rules.d/77-mm-sierra.rules
/lib/udev/rules.d/77-mm-simtech-port-types.rules
/lib/udev/rules.d/77-mm-telit-port-types.rules
/lib/udev/rules.d/77-mm-tplink-port-types.rules
/lib/udev/rules.d/77-mm-ublox-port-types.rules
/lib/udev/rules.d/77-mm-x22x-port-types.rules
/lib/udev/rules.d/77-mm-zte-port-types.rules
/lib/udev/rules.d/80-mm-candidate.rules
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/org.freedesktop.ModemManager1.conf
%dir %{_sysconfdir}/ModemManager
%dir %{_sysconfdir}/ModemManager/fcc-unlock.d
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Bearer.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Call.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Firmware.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Location.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Messaging.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Modem3gpp.ProfileManager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Modem3gpp.Ussd.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Modem3gpp.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.ModemCdma.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Oma.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Sar.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Simple.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Signal.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Time.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Voice.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Sim.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Sms.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.ModemManager1.service
%{_datadir}/polkit-1/actions/org.freedesktop.ModemManager1.policy
%{_iconsdir}/hicolor/22x22/apps/ModemManager.png
%{_mandir}/man1/mmcli.1*
%{_mandir}/man8/ModemManager.8*
%{systemdunitdir}/ModemManager.service

%files -n bash-completion-ModemManager
%defattr(644,root,root,755)
%{bash_compdir}/mmcli

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmm-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmm-glib.so.0
%{_libdir}/girepository-1.0/ModemManager-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmm-glib.so
%{_includedir}/ModemManager
%{_includedir}/libmm-glib
%{_pkgconfigdir}/ModemManager.pc
%{_pkgconfigdir}/mm-glib.pc
%{_datadir}/gir-1.0/ModemManager-1.0.gir

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/ModemManager
%{_gtkdocdir}/libmm-glib
%endif

%files -n vala-libmm-glib
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libmm-glib.deps
%{_datadir}/vala/vapi/libmm-glib.vapi
