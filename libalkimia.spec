%define major	6
%define libname	%mklibname alkimia %{major}
%define devname	%mklibname alkimia -d
%define date	20170505

Summary:	Financial library
Name:		libalkimia
Version:	6.0.0
Release:	0.%{date}.1
License:	LGPLv2+
Group:		Office
Url:		http://kde-apps.org/content/show.php/libalkimia?content=137323
Source0:	http://kde-apps.org/CONTENT/content-files/libalkimia-%{version}-%{date}.tar.xz
BuildRequires:	gmpxx-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	extra-cmake-modules
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Test)

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
%setup -q -n libalkimia-%{version}-%{date}

%build
%cmake
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{devname}
%{_includedir}/alkimia/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/LibAlkimia-%{major}.0/*.cmake
