%define _filter_GLIBC_PRIVATE 1
%define major 1
%define libname %mklibname nih %{major}
%define dbuslibname %mklibname nih-dbus %{major}
%define devname %mklibname nih -d

Name: libnih
Version: 1.0.3
Release: 2
Source0: https://launchpad.net/libnih/%(echo %{version} |cut -d. -f1-2)/%{version}/+download/libnih-%{version}.tar.gz
Summary: Library of small C functions
URL: http://launchpad.net/libnih
License: GPLv2
Group: System/Libraries
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(expat)

%description
libnih is roughly equivalent to other C libraries such as glib, except that
its focus is on a small size and intended for applications that sit very low
in the software stack, especially outside of /usr.

It expressly does not reimplement functions that already exist in libraries
ordinarily shipped in /lib such libc, and does not do foolish things like
invent arbitrary typedefs for perfectly good C types.

%package -n %{libname}
Summary: Library of small C functions
Group: System/Libraries

%description -n %{libname}
libnih is roughly equivalent to other C libraries such as glib, except that
its focus is on a small size and intended for applications that sit very low
in the software stack, especially outside of /usr.

It expressly does not reimplement functions that already exist in libraries
ordinarily shipped in /lib such libc, and does not do foolish things like
invent arbitrary typedefs for perfectly good C types.

%package -n %{dbuslibname}
Summary: Library of small C functions handling D-Bus
Group: System/Libraries

%description -n %{dbuslibname}
D-Bus wrapper based on libnih.

libnih is roughly equivalent to other C libraries such as glib, except that
its focus is on a small size and intended for applications that sit very low
in the software stack, especially outside of /usr.

It expressly does not reimplement functions that already exist in libraries
ordinarily shipped in /lib such libc, and does not do foolish things like
invent arbitrary typedefs for perfectly good C types.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

libnih is roughly equivalent to other C libraries such as glib, except that
its focus is on a small size and intended for applications that sit very low
in the software stack, especially outside of /usr.

It expressly does not reimplement functions that already exist in libraries
ordinarily shipped in /lib such libc, and does not do foolish things like
invent arbitrary typedefs for perfectly good C types.

%prep
%setup -q
if [ "%{_lib}" != "lib" ]; then
	sed -i -e 's,lib/pkgconfig,%{_lib}/pkgconfig,g' */Makefile.am
fi

%configure --enable-threading

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/*
%{_mandir}/man1/nih-dbus-tool.1*

%files -n %{libname}
%{_libdir}/libnih.so.%{major}*

%files -n %{dbuslibname}
%{_libdir}/libnih-dbus.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*.m4
