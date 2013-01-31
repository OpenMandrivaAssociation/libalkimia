Summary:	Financial library
Name:		libalkimia
Version:	4.3.2
Release:	1
Source0:	http://kde-apps.org/CONTENT/content-files/137323-libalkimia-%{version}.tar.bz2
License:	LGPLv2+
Group:		Office
URL:		http://kde-apps.org/content/show.php/libalkimia?content=137323
BuildRequires:	kdelibs4-devel
BuildRequires:	gmpxx-devel

%define major 4
%define lib %mklibname alkimia %major

%description 
Financial library used by KMyMoney and Scrooge

%package -n %lib
Summary:	Financial Library
Group:		System/Libraries
Provides:	%name = %EVRD

%description -n %lib
Financial library used by KMyMoney and Scrooge

%files -n %lib
%defattr(-,root,root)
%{_kde_libdir}/%{name}.so.%{major}*


%package devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
Requires:	kdelibs4-devel

%description devel
%{summary}.

%files devel
%defattr(-,root,root)
%{_kde_includedir}/alkimia/
%{_kde_libdir}/%{name}.so
%{_kde_libdir}/pkgconfig/%{name}.pc
%{_datadir}/apps/cmake/modules/FindLibAlkimia.cmake

#-----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%changelog
* Sun Sep 25 2011 Thomas Spuhler <tspuhler@mandriva.org> 4.3.1-1mdv2012.0
+ Revision: 701187
- totally revamped spec file, harmonized with Mageia
- imported package libalkimia

