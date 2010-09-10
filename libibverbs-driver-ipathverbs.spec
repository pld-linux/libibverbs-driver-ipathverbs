Summary:	Userspace driver for the QLogic InfiniBand HCAs
Summary(pl.UTF-8):	Sterownik przestrzeni użytkownika dla kart QLogic InfiniBand HCA
Name:		libibverbs-driver-ipathverbs
Version:	1.2
Release:	1
License:	BSD or GPL v2
Group:		Libraries
#Source0Download: http://www.openfabrics.org/downloads/ipath/
Source0:	http://www.openfabrics.org/downloads/libipathverbs/libipathverbs-%{version}.tar.gz
# Source0-md5:	5fc6b28891b76129d9146683c24091ad
URL:		http://openib.org/
BuildRequires:	libibverbs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libipathverbs is a userspace driver for QLogic InfiniBand HCAs. It
works as a plug-in module for libibverbs that allows programs to use
QLogic hardware directly from userspace.

Currently the driver supports the following HCAs:
- InfiniPath QLE7140 (PCIe)
- InfiniPath QMI7140 (PCIe)
- InfiniPath QHT7040 (HyperTransport)
- InfiniPath QHT7140 (HyperTransport)

It uses ib_ipath kernel driver.

%description -l pl.UTF-8
libipathverbs to sterownik przestrzeni użytkownika dla kart QLogic
InfiniBand HCA. Działa jako moduł ładowany przez libibverbs,
pozwalający programom na dostęp z przestrzeni użytkownika do sprzętu
QLogic.

Obecnie sterownik obsługuje następujące kontrolery HCA:
- InfiniPath QLE7140 (PCIe)
- InfiniPath QMI7140 (PCIe)
- InfiniPath QHT7040 (HyperTransport)
- InfiniPath QHT7140 (HyperTransport)

Wykorzystuje sterownik jądra ib_ipath.

%package static
Summary:	Static version of ipathverbs driver
Summary(pl.UTF-8):	Statyczna wersja sterownika ipathverbs
Group:		Development/Libraries
Requires:	libibverbs-static

%description static
Static version of ipathverbs driver, which may be linked directly into
application.

%description static -l pl.UTF-8
Statyczna wersja sterownika ipathverbs, którą można wbudować bezpośrednio
w aplikację.

%prep
%setup -q -n libipathverbs-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened by -rmav2.so name
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libipathverbs.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_libdir}/libipathverbs-rdmav2.so
%{_sysconfdir}/libibverbs.d/ipath.driver

%files static
%defattr(644,root,root,755)
%{_libdir}/libipathverbs.a
