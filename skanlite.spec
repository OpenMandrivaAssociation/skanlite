%define url_ver %(echo %version | cut -d. -f1,2)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	An image scanning application
Name:		skanlite
Version:	23.08.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/graphics/skanlite/
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/skanlite-%{version}.tar.xz
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
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html
