%define major	8
%define libname	%mklibname alkimia5 %{major}
%define devname	%mklibname alkimia5 -d

Summary:	Financial library
Name:		libalkimia
Version:	8.0.3
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
BuildRequires:	cmake(Qt5WebKitWidgets)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Package)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Emoticons)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Sonnet)
BuildRequires:	cmake(KF5UnitConversion)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(KF5NewStuffCore)
BuildRequires:	doxygen
BuildRequires:	ninja

%description
Financial library used by KMyMoney and Scrooge

%package -n %{libname}
Summary:	Financial Library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

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
%cmake_kde5 \
	-DSHARE_INSTALL_DIR=%{_datadir}

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang alkimia --all-name

%files -f alkimia.lang
%{_sysconfdir}/xdg/alkimia-quotes.knsrc
%{_sysconfdir}/xdg/kmymoney-quotes.knsrc
%{_sysconfdir}/xdg/skrooge-quotes.knsrc
%{_bindir}/onlinequoteseditor5
%{_libdir}/qt5/qml/org/kde/alkimia
%{_datadir}/alkimia5
%{_datadir}/applications/org.kde.onlinequoteseditor5.desktop
%{_datadir}/icons/hicolor/*/apps/onlinequoteseditor5.*
%{_datadir}/kservices5/plasma-applet-org.wincak.foreigncurrencies2.desktop
%{_datadir}/metainfo/org.wincak.foreigncurrencies2.appdata.xml
%{_datadir}/plasma/plasmoids/org.wincak.foreigncurrencies2

%files -n %{libname}
%{_libdir}/%{name}5.so.%{major}*

%files -n %{devname}
%{_includedir}/alkimia/
%{_libdir}/%{name}5.so
%{_libdir}/pkgconfig/%{name}5.pc
%{_libdir}/cmake/LibAlkimia5-%{major}.0/*.cmake
