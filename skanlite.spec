Summary:	An image scanning application
Name:		skanlite
Version:	2.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/graphics/skanlite/
Source0:	http://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	libksane-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Sane)
BuildRequires:	cmake(KF5TextWidgets)


%description
Skanlite is an image scanning application that does nothing more than
scan and save images. It is based on libksane, a KDE interface for SANE
library to control flat scanners.

%files -f %{name}.lang
%{_kde5_bindir}/%{name}
%{_datadir}/applications/*.desktop

#------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %{name} --with-html

