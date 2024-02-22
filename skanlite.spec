%define git 20240222
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define url_ver %(echo %version | cut -d. -f1,2)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	An image scanning application
Name:		skanlite
Version:	24.02.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/graphics/skanlite/
%if 0%{?git:1}
Source0:        https://invent.kde.org/graphics/skanlite/-/archive/%{gitbranch}/skanlite-%{gitbranchd}.tar.bz2#/skanlite-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/skanlite-%{version}.tar.xz
%endif
BuildRequires:	pkgconfig(libpng)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Sane)
BuildRequires:	cmake(KF5TextWidgets)
Provides:	scanner-gui

Requires: sane

%description
Skanlite is an image scanning application that does nothing more than
scan and save images. It is based on libksane, a KDE interface for SANE
library to control flat scanners.

%files -f %{name}.lang
%{_kde5_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/org.kde.skanlite.appdata.xml
%{_iconsdir}/hicolor/*x*/apps/org.kde.skanlite.svg

#------------------------------------------------

%prep
%autosetup -p1 -n skanlite-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake_kde5 \
	-DQT_MAJOR_VERSION=5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html
