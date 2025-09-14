#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define url_ver %(echo %version | cut -d. -f1,2)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	An image scanning application
Name:		skanlite
Version:	25.08.1
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/applications/graphics/skanlite/
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/skanlite/-/archive/%{gitbranch}/skanlite-%{gitbranchd}.tar.bz2#/skanlite-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/skanlite-%{version}.tar.xz
%endif
BuildRequires:	pkgconfig(libpng)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KSaneCore6)
BuildRequires:	cmake(KSaneWidgets6)
Provides:	scanner-gui

Requires: sane

%rename plasma6-skanlite

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Skanlite is an image scanning application that does nothing more than
scan and save images. It is based on libksane, a KDE interface for SANE
library to control flat scanners.

%files -f skanlite.lang
%{_bindir}/skanlite
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/org.kde.skanlite.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.skanlite.svg
