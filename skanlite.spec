Summary:	An image scanning application
Name:		skanlite
Version:	1.1
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/graphics/skanlite/
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	libksane-devel
BuildRequires:	pkgconfig(libpng)

%description
Skanlite is an image scanning application that does nothing more than
scan and save images. It is based on libksane, a KDE interface for SANE
library to control flat scanners.

%files -f %{name}.lang
%{_kde_bindir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop

#------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

