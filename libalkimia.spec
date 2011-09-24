# Spec File based on Fedora
Name:    	libalkimia
Summary: 	Financial library
Version: 	4.3.1
Release: 	%mkrel 1

License: 	LGPLv2+
URL:     	http://kde-apps.org/content/show.php/libalkimia?content=137323
Source0: 	http://kde-apps.org/CONTENT/content-files/137323-libalkimia-%{version}.tar.bz2

BuildRequires: 	gmp-devel
BuildRequires: 	libgmpxx-devel
BuildRequires: 	kdelibs4-devel
BuildRequires:	doxygen
Group:		System/Libraries 

%description
Financial library

%package 	devel
Summary: 	Development files for %{name}
Requires: 	%{name} = %{version}-%{release}
Requires: 	kdelibs4-devel

%description
Financial library


%prep
%setup -q


%build
%cmake_kde4
%make



%install
rm -rf %{buildroot}
%{makeinstall_std} -C build



%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libalkimia)" = "%{version}" 


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%{_libdir}/libalkimia.so.4*

%files devel
%{_includedir}/alkimia/
%{_libdir}/libalkimia.so
%{_libdir}/pkgconfig/libalkimia.pc
%{_datadir}/apps/cmake/modules/FindLibAlkimia.cmake



