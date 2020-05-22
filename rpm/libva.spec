Name:		libva
Version:	2.0.0
Release:	1%{?dist}
Summary:    Libva is an implementation for VA-API (Video Acceleration API) https://01.org/linuxmedia
License:	MIT
URL:	    https://github.com/intel/libva/
Source0:	${name}-${version}.tar.bz2

BuildRequires: automake

%package devel
Summary: libva development files
%description devel
libva development files

%description
Libva is an implementation for VA-API (Video Acceleration API) https://01.org/linuxmedia

%prep
%autosetup -p1 -n ${name}-${version}/upstream

%build
./autogen.sh --prefix=/usr
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/libva-drm.so.2
%{_libdir}/libva-drm.so.2.0.0
%{_libdir}/libva-wayland.so.2
%{_libdir}/libva-wayland.so.2.0.0
%{_libdir}/libva.so.2
%{_libdir}/libva.so.2.0.0

%files devel
%defattr(-,root,root,-)
%{_libdir}/libva-drm.la
%{_libdir}/libva-wayland.so
%{_libdir}/libva-wayland.la
%{_libdir}/libva.la
%{_libdir}/libva-drm.so
%{_libdir}/libva.so
%{_libdir}/pkgconfig/libva.pc
%{_libdir}/pkgconfig/libva-wayland.pc
%{_libdir}/pkgconfig/libva-drm.pc
%{_includedir}/va/va_dec_jpeg.h
%{_includedir}/va/va_dec_vp8.h
%{_includedir}/va/va_backend_vpp.h
%{_includedir}/va/va_str.h
%{_includedir}/va/va_enc_h264.h
%{_includedir}/va/va_enc_vp8.h
%{_includedir}/va/va_tpi.h
%{_includedir}/va/va_wayland.h
%{_includedir}/va/va_version.h
%{_includedir}/va/va_enc_vp9.h
%{_includedir}/va/va_enc_jpeg.h
%{_includedir}/va/va_backend.h
%{_includedir}/va/va_vpp.h
%{_includedir}/va/va_dec_hevc.h
%{_includedir}/va/va_drm.h
%{_includedir}/va/va_enc_hevc.h
%{_includedir}/va/va_backend_wayland.h
%{_includedir}/va/va_fei_h264.h
%{_includedir}/va/va.h
%{_includedir}/va/va_dec_vp9.h
%{_includedir}/va/va_egl.h
%{_includedir}/va/va_drmcommon.h
%{_includedir}/va/va_fei.h
%{_includedir}/va/va_enc_mpeg2.h
%{_includedir}/va/va_compat.h
