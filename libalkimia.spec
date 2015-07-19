%define major	4
%define libname	%mklibname alkimia %{major}
%define devname	%mklibname alkimia -d

Summary:	Financial library
Name:		libalkimia
Version:	4.3.2
Release:	10
License:	LGPLv2+
Group:		Office
Url:		http://kde-apps.org/content/show.php/libalkimia?content=137323
Source0:	http://kde-apps.org/CONTENT/content-files/137323-libalkimia-%{version}.tar.bz2
BuildRequires:	gmpxx-devel
BuildRequires:	kdelibs4-devel

%description 
Financial library used by KMyMoney and Scrooge

%package -n %{libname}
Summary:	Financial Library
Group:		System/Libraries
Provides:	%{name} = %{EVRD}

%description -n %{libname}
Financial library used by KMyMoney and Scrooge

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	libalkimia-devel < 4.3.2-2

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_kde_libdir}/%{name}.so.%{major}*

%files -n %{devname}
%{_kde_includedir}/alkimia/
%{_kde_libdir}/%{name}.so
%{_kde_libdir}/pkgconfig/%{name}.pc
%{_datadir}/apps/cmake/modules/FindLibAlkimia.cmake

