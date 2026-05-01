%define		major 0
%define		libname %mklibname tpms %{major}
%define		devname %mklibname -d tpms

Summary:		Library providing Trusted Platform Module (TPM) functionality
Name:		libtpms
Version:		0.10.2
Release:		1
Group:	System/Libraries
License:	BSD
Url:		https://github.com/stefanberger/libtpms
Source0:    https://github.com/stefanberger/libtpms/archive/refs/tags/%{name}-%{version}.tar.gz
Patch0:		libtpms-0.10.2-drop-Werror.patch
Patch1:		libtpms-0.10.2-fix-discard-const-error.patch
BuildRequires:		autoconf
BuildRequires:		automake
BuildRequires:		libtool-base
BuildRequires:		slibtool
BuildRequires:		make
BuildRequires:		gettext
BuildRequires:		glibc-devel
BuildRequires:		pkgconfig(nspr)
BuildRequires:		pkgconfig(nss)
BuildRequires:		pkgconfig(openssl)

%description
A library that targets the integration of TPM functionality into hypervisors,
primarily into Qemu.

#-----------------------------------------------------------------------------

%package	 -n %{libname}
Summary:		Main %{name} library
Group:	System/Libraries

%description -n %{libname}
A library that targets the integration of TPM functionality into hypervisors,
primarily into Qemu.

%files	-n %{libname}
%license LICENSE
%doc CHANGES README
%{_libdir}/libtpms.so.%{major}*

#-----------------------------------------------------------------------------

%package -n %{devname}
Summary:		Files for %{name} development
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Header files and documentation for %{name}.

%files -n %{devname}
%license LICENSE
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/tpm_*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
./bootstrap.sh
%configure --disable-static --with-tpm2 --with-openssl
%make_build


%install
%make_install


%check
make check
