#
# spec file for package freerdp
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define lib_freerdp_version 2
%define lib_winpr_version 2
%define lib_uwac_version 0

%if %{defined suse_version} && !%{defined is_opensuse}
%bcond_with wayland
%bcond_with avcodec
%define SEL 1
%else
%bcond_without wayland
%bcond_with avcodec
%define SEL 0
%endif

Name:           freerdp2
Version:        2.0.0
Release:        0
Summary:        Remote Desktop Protocol client
%if %{defined fedora}
License:        ASL 2.0
%else
License:        Apache-2.0
%endif
%if !%{defined fedora}
Group:          Productivity/Networking/Other
%else
Group:          Applications/Productivity
%endif
Url:            http://www.freerdp.com/
Source0:        FreeRDP-%{version}.tar.xz
BuildRequires:  chrpath
BuildRequires:  cmake >= 2.8
BuildRequires:  cups-devel
BuildRequires:  ed
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
%if %{defined fedora}
BuildRequires:  gsm-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
%else
BuildRequires:  libgsm-devel
BuildRequires:  xorg-x11-devel
BuildRequires:  xorg-x11-libs
%if %{with avcodec}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
%endif
%endif
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libsystemd-journal)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pkg-config)
%if %{with wayland}
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
%endif
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(libudev)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} > 1220
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
%endif
%if 0%{?suse_version} >= 1120
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpulse)
%endif

%description
FreeRDP is a libre implementation of the Remote Desktop Protocol (RDP)
(server and client side) following the Microsoft Open Specifications.
This package provides the X11 client application.

%if %{with wayland}
%package wayland
Summary:        Remote Desktop Viewer Client
%if !%{defined fedora}
Group:          Productivity/Networking/Other
%else
Group:          Applications/Productivity
%endif

%description wayland
FreeRDP is a libre implementation of the Remote Desktop Protocol (RDP)
(server and client side) following the Microsoft Open Specifications.
This package provides the wayland client application.
%endif

%package -n libfreerdp%{lib_freerdp_version}
Summary:        Remote Desktop Viewer client library
%if !%{defined fedora}
Group:          System/Libraries
%else
Group:          System Environment/Libraries
%endif
Provides:       libfreerdp%{lib_freerdp_version} = %{version}-%{release}

%description -n libfreerdp%{lib_freerdp_version}
FreeRDP is a libre implementation of the Remote Desktop Protocol (RDP)
(server and client side) following the Microsoft Open Specifications.
This package provides the core library.

%package -n libfreerdp-server%{lib_freerdp_version}
Summary:        Remote Desktop Server
%if !%{defined fedora}
Group:          Productivity/Networking/Other
%else
Group:          Applications/Productivity
%endif
Provides:       libfreerdp-server%{lib_freerdp_version} = %{version}-%{release}

%description -n libfreerdp-server%{lib_freerdp_version}
FreeRDP is a libre implementation of the Remote Desktop Protocol (RDP)
(server and client side) following the Microsoft Open Specifications.
This package contains the server side functionality and channels.

%package -n libfreerdp-client%{lib_freerdp_version}
Summary:        Remote Desktop Client
%if !%{defined fedora}
Group:          Productivity/Networking/Other
%else
Group:          Applications/Productivity
%endif
Provides:       libfreerdp-client%{lib_freerdp_version} = %{version}-%{release}
Obsoletes:      freerdp-plugins < %{version}-%{release}
Provides:       freerdp-plugins = %{version}-%{release}

%description -n libfreerdp-client%{lib_freerdp_version}
FreeRDP is a libre implementation of the Remote Desktop Protocol (RDP)
(server and client side) following the Microsoft Open Specifications.
This package contains the client side functionality and channels.

%package -n libfreerdp-shadow%{lib_freerdp_version}
Summary:        Remote Desktop Client
%if !%{defined fedora}
Group:          Productivity/Networking/Other
%else
Group:          Applications/Productivity
%endif
Provides:       libfreerdp-shadow%{lib_freerdp_version} = %{version}-%{release}

%description -n libfreerdp-shadow%{lib_freerdp_version}
FreeRDP is a libre implementation of the Remote Desktop Protocol (RDP)
(server and client side) following the Microsoft Open Specifications.
This package provides the base libraries for sharing a running X11
desktop via RDP similar to VNC.

%package devel
Summary:        Development Files for %{name}
%if !%{defined fedora}
Group:          Development/Libraries/C and C++
%else
Group:          Development/Libraries
%endif
Requires:       libfreerdp%{lib_freerdp_version} = %{version}
Requires:       libfreerdp-client%{lib_freerdp_version} = %{version}
Requires:       libfreerdp-shadow%{lib_freerdp_version} = %{version}
Requires:       libfreerdp-server%{lib_freerdp_version} = %{version}

%description devel
FreeRDP is a libre implementation of the Remote Desktop Protocol (RDP)
(server and client side) following the Microsoft Open Specifications.
This package contains development files necessary for developing
applications based on libfreerdp.

%package -n     libwinpr%{lib_winpr_version}
Summary:        Windows Portable Runtime
%if !%{defined fedora}
Group:          Productivity/Networking/Other
%else
Group:          Applications/Productivity
%endif
Provides:       libwinpr = %{version}-%{release}

%description -n libwinpr%{lib_winpr_version}
The windows portable run time - WinPR  - provides API compatibility for
applications targeting non-Windows environments. When on Windows, the
original native API is being used instead of the equivalent WinPR
implementation, without having to modify the code using it.

%package -n     libwinpr-tools%{lib_winpr_version}
Summary:        Windows Portable Runtime
%if !%{defined fedora}
Group:          Productivity/Networking/Other
%else
Group:          Applications/Productivity
%endif

%description -n libwinpr-tools%{lib_winpr_version}
The windows portable run time - WinPR  - provides API compatibility for
applications targeting non-Windows environments. When on Windows, the
original native API is being used instead of the equivalent WinPR
implementation, without having to modify the code using it.
This package contains the tools library that provides additional
functionality like certificate generation.

%package -n     winpr-utils
Summary:        Windows Portable Runtime
%if !%{defined fedora}
Group:          Productivity/Networking/Other
%else
Group:          Applications/Productivity
%endif

%description -n winpr-utils
The windows portable run time - WinPR  - provides API compatibility for
applications targeting non-Windows environments. When on Windows, the
original native API is being used instead of the equivalent WinPR
implementation, without having to modify the code using it.
This package provides some useful utilities based on winpr.

%package -n     libwinpr%{lib_winpr_version}-devel
Summary:        Windows Portable Runtime development files
%if !%{defined fedora}
Group:          Development/Libraries/C and C++
%else
Group:          Development/Libraries
%endif
Requires:       cmake >= 2.8
Requires:       libwinpr%{lib_winpr_version} = %{version}-%{release}
Requires:       libwinpr-tools%{lib_winpr_version} = %{version}-%{release}
Requires:       winpr-utils = %{version}-%{release}
Requires:       pkgconfig

%description -n libwinpr%{lib_winpr_version}-devel
The libwinpr-devel package contains libraries and header files for
developing applications that use libwinpr and libwinpr-tools.

%if %{with wayland}
%package -n     libuwac%{lib_uwac_version}
Summary:        Use wayland as a client
%if !%{defined fedora}
Group:          Productivity/Networking/Other
%else
Group:          Applications/Productivity
%endif
Provides:       libuwac = %{version}-%{release}
Obsoletes:      libuwac < %{version}-%{release}

%description -n libuwac%{lib_uwac_version}
Using wayland as a client (uwac) is a library to provide common
functionality for wayland clients.

%package -n     libuwac%{lib_uwac_version}-devel
Summary:        Remote Desktop Toolkit libuwac development files
%if !%{defined fedora}
Group:          Development/Libraries/C and C++
%else
Group:          Development/Libraries
%endif
Requires:       cmake >= 2.8
Requires:       libuwac%{lib_uwac_version} = %{version}-%{release}
Requires:       pkgconfig

%description -n libuwac%{lib_uwac_version}-devel
The libuwac-devel package contains libraries and header files for
developing applications that use libuwac.
%endif

%package -n     %{name}-shadow-x11
Summary:        FreeRDP shadowing server for X11
%if !%{defined fedora}
Group:          Productivity/Networking/Other
%else
Group:          Applications/Productivity
%endif
Provides:       freerdp-shdaow-x11 = %{version}-%{release}

%description -n %{name}-shadow-x11
FreeRDP is a libre implementation of the Remote Desktop Protocol (RDP)
(server and client side) following the Microsoft Open Specifications.
This package provides the base libraries for sharing a running X11
desktop via RDP similar to VNC.
This package contains a X11 specific command line tool of the FreeRDP
shadowing server.

%prep
%setup -q -n FreeRDP-%{version}
%if 0%{?sles_version} == 11
    cp %{SOURCE1} cmake/
%endif

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RELWITHDEBINFO \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
    -DCMAKE_SKIP_RPATH=TRUE \
    -DCMAKE_SKIP_INSTALL_RPATH=TRUE \
    -DWITH_ALSA=ON \
    -DWITH_CUPS=ON \
    -DWITH_CLIENT=ON \
    -DWITH_PULSE=ON \
    -DWITH_SERVER=ON \
    -DWITH_CHANNELS=ON \
    -DWITH_GSM=ON \
%if 0%{?suse_version} > 1220 || 0%{?fedora}
    -DWITH_GSTREAMER_1_0=ON \
%else
    -DWITH_GSTREAMER_1_0=OFF \
%endif
    -DWITH_IPP=OFF \
    -DWITH_JPEG=ON \
    -DWITH_LIBRARY_VERSIONING=ON \
    -DWITH_OPENSSL=ON \
    -DWITH_PCSC=ON \
    -DWITH_X11=ON \
    -DWITH_XCURSOR=ON \
    -DWITH_XEXT=ON \
    -DWITH_XKBFILE=ON \
    -DWITH_XI=ON \
    -DWITH_XINERAMA=ON \
    -DWITH_XRENDER=ON \
    -DWITH_XV=ON \
    -DWITH_ZLIB=ON \
    -DWITH_CLIENT_INTERFACE=OFF \
%if %{with wayland}
    -DWITH_WAYLAND=ON \
%endif
    -DCHANNEL_URBDRC=ON \
    -DCHANNEL_URBDRC_CLIENT=ON \
    -DBUILD_TESTING=OFF \
%ifarch x86_64
    -DWITH_SSE2=ON \
%else
    -DWITH_SSE2=OFF \
%endif
%if %{defined fedora}
    .
%else
    ..
%endif

make %{?_smp_mflags}

%install
%if !0%{?fedora}
cd build
%endif
make %{?_smp_mflags} DESTDIR=%{buildroot} install

%post   -n libfreerdp%{lib_freerdp_version} -p /sbin/ldconfig
%postun -n libfreerdp%{lib_freerdp_version} -p /sbin/ldconfig
%post   -n libfreerdp-client%{lib_freerdp_version} -p /sbin/ldconfig
%postun -n libfreerdp-client%{lib_freerdp_version} -p /sbin/ldconfig
%post   -n libfreerdp-server%{lib_freerdp_version} -p /sbin/ldconfig
%postun -n libfreerdp-server%{lib_freerdp_version} -p /sbin/ldconfig
%post   -n libfreerdp-shadow%{lib_freerdp_version} -p /sbin/ldconfig
%postun -n libfreerdp-shadow%{lib_freerdp_version} -p /sbin/ldconfig
%post -n libwinpr%{lib_winpr_version} -p /sbin/ldconfig
%postun -n libwinpr%{lib_winpr_version} -p /sbin/ldconfig
%post -n libwinpr-tools%{lib_winpr_version} -p /sbin/ldconfig
%postun -n libwinpr-tools%{lib_winpr_version} -p /sbin/ldconfig
%if %{with wayland}
%post -n libuwac%{lib_uwac_version} -p /sbin/ldconfig
%postun -n libuwac%{lib_uwac_version} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%{_bindir}/xfreerdp
%if %{defined fedora}
%{_mandir}/man1/xfreerdp.1.*
%else
%{_mandir}/man1/xfreerdp.1%{ext_man}
%endif

%if %{with wayland}
%files wayland
%defattr(-,root,root)
%{_bindir}/wlfreerdp
%endif

%files shadow-x11
%defattr(-,root,root)
%{_bindir}/freerdp-shadow-cli

%files -n winpr-utils 
%defattr(-,root,root)
%{_bindir}/winpr-*

%files -n libfreerdp%{lib_freerdp_version}
%defattr(-,root,root)
%{_libdir}/libfreerdp.so.*

%files -n libfreerdp-client%{lib_freerdp_version}
%defattr(-,root,root)
%{_libdir}/libfreerdp-client.so.*

%files -n libfreerdp-server%{lib_freerdp_version}
%{_libdir}/libfreerdp-server.so.*
%defattr(-,root,root)

%files -n libfreerdp-shadow%{lib_freerdp_version}
%{_libdir}/libfreerdp-shadow.so.*
%{_libdir}/libfreerdp-shadow-subsystem.so.*
%defattr(-,root,root)

%files devel
%defattr(-,root,root)
%doc LICENSE
%{_libdir}/cmake/FreeRDP%{lib_freerdp_version}
%{_libdir}/cmake/FreeRDP-Client%{lib_freerdp_version}
%{_libdir}/cmake/FreeRDP-Server%{lib_freerdp_version}
%{_libdir}/cmake/FreeRDP-Shadow%{lib_freerdp_version}
%{_includedir}/freerdp%{lib_freerdp_version}
%{_libdir}/libfreerdp*.so
%{_libdir}/pkgconfig/freerdp%{lib_freerdp_version}.pc
%{_libdir}/pkgconfig/freerdp-client%{lib_freerdp_version}.pc
%{_libdir}/pkgconfig/freerdp-server%{lib_freerdp_version}.pc
%{_libdir}/pkgconfig/freerdp-shadow%{lib_freerdp_version}.pc

%files -n libwinpr%{lib_winpr_version}
%defattr(-,root,root)
%{_libdir}/libwinpr.so.*

%files -n libwinpr-tools%{lib_winpr_version}
%defattr(-,root,root)
%{_libdir}/libwinpr-tools.so.*

%files -n libwinpr%{lib_winpr_version}-devel
%defattr(-,root,root)
%doc LICENSE
%{_libdir}/cmake/WinPR%{lib_winpr_version}
%{_includedir}/winpr%{lib_winpr_version}
%{_libdir}/libwinpr.so
%{_libdir}/libwinpr-tools.so
%{_libdir}/pkgconfig/winpr%{lib_winpr_version}.pc
%{_libdir}/pkgconfig/winpr-tools%{lib_winpr_version}.pc

%if %{with wayland}
%files -n libuwac%{lib_uwac_version}
%defattr(-,root,root)
%doc LICENSE
%{_libdir}/libuwac*.so.*

%files -n libuwac%{lib_uwac_version}-devel
%defattr(-,root,root)
%{_libdir}/cmake/uwac%{lib_uwac_version}
%{_includedir}/uwac%{lib_uwac_version}
%{_libdir}/libuwac.so
%{_libdir}/pkgconfig/uwac%{lib_uwac_version}.pc
%endif

%changelog
* Thu May 19 2016 FreeRDP Team <team@freerdp.com> - 2.0.0-0
- Initial version

