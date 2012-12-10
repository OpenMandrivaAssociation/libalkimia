Summary:	Financial library
Name:		libalkimia
Version:	4.3.1
Release:	%mkrel 1
Source0:	http://kde-apps.org/CONTENT/content-files/137323-libalkimia-%{version}.tar.bz2
License:	LGPLv2+
Group:		Office
URL:		http://kde-apps.org/content/show.php/libalkimia?content=137323
BuildRequires:	kdelibs4-devel
BuildRequires:	gmpxx-devel

%description 
Financial library used by KMyMoney and Scrooge

%files
%defattr(-,root,root)
%{_kde_libdir}/%{name}.so.4*


%package devel
Summary:	Development files for %{name}
Group:		System/Libraries
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

%clean
rm -rf %{buildroot}




%changelog
* Sun Sep 25 2011 Thomas Spuhler <tspuhler@mandriva.org> 4.3.1-1mdv2012.0
+ Revision: 701187
- totally revamped spec file, harmonized with Mageia
- imported package libalkimia

