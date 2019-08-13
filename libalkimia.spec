%define major	7
%define libname	%mklibname alkimia5 %{major}
%define devname	%mklibname alkimia5 -d

Summary:	Financial library
Name:		libalkimia
Version:	8.0.1
Release:	1
License:	LGPLv2+
Group:		Office
Url:		http://kde-apps.org/content/show.php/libalkimia?content=137323
Source0:	https://download.kde.org/stable/alkimia/%{version}/alkimia-%{version}.tar.xz
BuildRequires:	gmpxx-devel
BuildRequires:	extra-cmake-modules
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebKitWidgets)

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
%setup -q -n alkimia-%{version}

%build
%cmake
%make_build

%install
%make_install -C build

%files -n %{libname}
%{_libdir}/%{name}5.so.%{major}*

%files -n %{devname}
%{_includedir}/alkimia/
%{_libdir}/%{name}5.so
%{_libdir}/pkgconfig/%{name}5.pc
%{_libdir}/cmake/LibAlkimia5-%{major}.0/*.cmake
