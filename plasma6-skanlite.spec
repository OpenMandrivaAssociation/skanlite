%define url_ver %(echo %version | cut -d. -f1,2)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	An image scanning application
Name:		plasma6-skanlite
Version:	24.01.90
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/graphics/skanlite/
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/skanlite-%{version}.tar.xz
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

%description
Skanlite is an image scanning application that does nothing more than
scan and save images. It is based on libksane, a KDE interface for SANE
library to control flat scanners.

%files -f skanlite.lang
%{_bindir}/skanlite
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/org.kde.skanlite.appdata.xml
%{_iconsdir}/hicolor/*x*/apps/org.kde.skanlite.svg

#------------------------------------------------

%prep
%autosetup -p1 -n skanlite-%{?git:master}%{!?git:%{version}}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang skanlite --with-html
